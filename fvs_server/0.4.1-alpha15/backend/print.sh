#!/usr/bin/env bash
docker ps --format "table {{.Names}} \t {{.Ports}}"
