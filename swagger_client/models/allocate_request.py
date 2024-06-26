# coding: utf-8

"""
    GSI Floating-Point 32 API

    **Introduction**<br> GSI Technology’s floating-point similarity search API provides an accessible gateway to running searches on GSI’s Gemini® Associative Processing Unit (APU).<br> It works in conjunction with the GSI system management solution which enables users to work with multiple APU boards simultaneously for improved performance.<br><br> **Dataset and Query Format**<br> Dataset embeddings can be in 32- or 64-bit floating point format, and any number of features, e.g. 256 or 512 (there is no upper limit).<br> Query embeddings must have the same floating-point format and number of features as used in the dataset.<br> GSI performs the search and delivers the top-k most similar results.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AllocateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'num_of_boards': 'int',
        'max_num_of_threads': 'int',
        'allocation_name': 'str'
    }

    attribute_map = {
        'num_of_boards': 'numOfBoards',
        'max_num_of_threads': 'maxNumOfThreads',
        'allocation_name': 'allocationName'
    }

    def __init__(self, num_of_boards=None, max_num_of_threads=None, allocation_name=None):  # noqa: E501
        """AllocateRequest - a model defined in Swagger"""  # noqa: E501
        self._num_of_boards = None
        self._max_num_of_threads = None
        self._allocation_name = None
        self.discriminator = None
        self.num_of_boards = num_of_boards
        if max_num_of_threads is not None:
            self.max_num_of_threads = max_num_of_threads
        if allocation_name is not None:
            self.allocation_name = allocation_name

    @property
    def num_of_boards(self):
        """Gets the num_of_boards of this AllocateRequest.  # noqa: E501

        Number of boards to allocate.  # noqa: E501

        :return: The num_of_boards of this AllocateRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_of_boards

    @num_of_boards.setter
    def num_of_boards(self, num_of_boards):
        """Sets the num_of_boards of this AllocateRequest.

        Number of boards to allocate.  # noqa: E501

        :param num_of_boards: The num_of_boards of this AllocateRequest.  # noqa: E501
        :type: int
        """
        if num_of_boards is None:
            raise ValueError("Invalid value for `num_of_boards`, must not be `None`")  # noqa: E501

        self._num_of_boards = num_of_boards

    @property
    def max_num_of_threads(self):
        """Gets the max_num_of_threads of this AllocateRequest.  # noqa: E501

        Specifies the number of threads to use during a search operation. The minimum number of threads is at least 4 + 1, 4 for each APUC (APU CORE) in a single board and another one for CPU.  # noqa: E501

        :return: The max_num_of_threads of this AllocateRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_num_of_threads

    @max_num_of_threads.setter
    def max_num_of_threads(self, max_num_of_threads):
        """Sets the max_num_of_threads of this AllocateRequest.

        Specifies the number of threads to use during a search operation. The minimum number of threads is at least 4 + 1, 4 for each APUC (APU CORE) in a single board and another one for CPU.  # noqa: E501

        :param max_num_of_threads: The max_num_of_threads of this AllocateRequest.  # noqa: E501
        :type: int
        """

        self._max_num_of_threads = max_num_of_threads

    @property
    def allocation_name(self):
        """Gets the allocation_name of this AllocateRequest.  # noqa: E501


        :return: The allocation_name of this AllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._allocation_name

    @allocation_name.setter
    def allocation_name(self, allocation_name):
        """Sets the allocation_name of this AllocateRequest.


        :param allocation_name: The allocation_name of this AllocateRequest.  # noqa: E501
        :type: str
        """

        self._allocation_name = allocation_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AllocateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AllocateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
