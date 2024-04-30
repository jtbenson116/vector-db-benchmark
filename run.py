import fnmatch
import traceback
from typing import List

import stopit
import typer
import os, sys
import time
import datetime
import json

from benchmark.config_read import read_dataset_config, read_engine_configs
from benchmark.dataset import Dataset
from engine.base_client import IncompatibilityError
from engine.clients.client_factory import ClientFactory
import power_capture

app = typer.Typer()


@app.command()
def run(
    engines: List[str] = typer.Option(["*"]),
    datasets: List[str] = typer.Option(["*"]),
    power: List[str] = typer.Option(["*"]),
    host: str = "localhost",
    skip_upload: bool = False,
    skip_search: bool = False,
    exit_on_error: bool = True,
    timeout: float = 86400.0,
):
    """
    Example:
        python3 run.py --engines *-m-16-* --engines qdrant-* --datasets glove-*
    """
    print("Starting at", str(datetime.datetime.now()), "with timeout=", timeout)
    time.sleep(5)

    all_engines = read_engine_configs()
    all_datasets = read_dataset_config()

    selected_engines = {
        name: config
        for name, config in all_engines.items()
        if any(fnmatch.fnmatch(name, engine) for engine in engines)
    }
    selected_datasets = {
        name: config
        for name, config in all_datasets.items()
        if any(fnmatch.fnmatch(name, dataset) for dataset in datasets)
    }

    for engine_name, engine_config in selected_engines.items():
        for dataset_name, dataset_config in selected_datasets.items():
            print(f"Running experiment: {engine_name} - {dataset_name}")

            # make sure ipmi cap server is available
            print(f"Starting power capture session... {power}")
            power_capture.power_capture(power[0])
            print("pinging ipmicap power monitor...")
            if not power_capture.power_capture.ping():
                raise Exception("could not ping the ipmicap power mon server")
            psession_id = power_capture.power_capture.start()

            os.environ["DATA_PATH"] = dataset_config['path']
            client = ClientFactory(host).build_client(engine_config)
            dataset = Dataset(dataset_config)
            dataset.download()
            try:
                with stopit.ThreadingTimeout(timeout) as tt:
                    client.run_experiment(dataset, skip_upload, skip_search)

                # If the timeout is reached, the server might be still in the
                # middle of some background processing, like creating the index.
                # Next experiment should not be launched. It's better to reset
                # the server state manually.
                if tt.state != stopit.ThreadingTimeout.EXECUTED:
                    print(
                        f"Timed out {engine_name} - {dataset_name}, "
                        f"exceeded {timeout} seconds"
                    )
                    exit(2)
                print("stopping power capture...")
                power_stats = power_capture.power_capture.stop(psession_id, all_stats=True)
                print(f"power stats: {power_stats}")
                power_json = f"./results/{engine_name}-{dataset.config.name}-power.json"
                if os.path.exists(power_json):
                    outfile = open(power_json, "r+")
                    file_data = json.load(outfile)
                else:
                    outfile = open(power_json, "w")
                    file_data = {}
                file_data[str(datetime.datetime.now())] = power_stats
                outfile.seek(0)
                json.dump(file_data, outfile)
                outfile.close()
                
            except IncompatibilityError as e:
                print(f"Skipping {engine_name} - {dataset_name}, incompatible params")
                continue
            except KeyboardInterrupt as e:
                traceback.print_exc()
                exit(1)
            except Exception as e:
                print(f"Experiment {engine_name} - {dataset_name} interrupted")
                traceback.print_exc()
                if exit_on_error:
                    raise e
                continue
    print("done")
    os._exit(0)


if __name__ == "__main__":
    app()
