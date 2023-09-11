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

class SearchRequestPrefilters(object):
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
        'prefilter_base64': 'str',
        'prefilter_mask_type': 'str'
    }

    attribute_map = {
        'prefilter_base64': 'prefilterBase64',
        'prefilter_mask_type': 'prefilterMaskType'
    }

    def __init__(self, prefilter_base64=None, prefilter_mask_type=None):  # noqa: E501
        """SearchRequestPrefilters - a model defined in Swagger"""  # noqa: E501
        self._prefilter_base64 = None
        self._prefilter_mask_type = None
        self.discriminator = None
        if prefilter_base64 is not None:
            self.prefilter_base64 = prefilter_base64
        if prefilter_mask_type is not None:
            self.prefilter_mask_type = prefilter_mask_type

    @property
    def prefilter_base64(self):
        """Gets the prefilter_base64 of this SearchRequestPrefilters.  # noqa: E501

        Binary data represent the bitmask in base64 format. Bits order should be little endian.  # noqa: E501

        :return: The prefilter_base64 of this SearchRequestPrefilters.  # noqa: E501
        :rtype: str
        """
        return self._prefilter_base64

    @prefilter_base64.setter
    def prefilter_base64(self, prefilter_base64):
        """Sets the prefilter_base64 of this SearchRequestPrefilters.

        Binary data represent the bitmask in base64 format. Bits order should be little endian.  # noqa: E501

        :param prefilter_base64: The prefilter_base64 of this SearchRequestPrefilters.  # noqa: E501
        :type: str
        """

        self._prefilter_base64 = prefilter_base64

    @property
    def prefilter_mask_type(self):
        """Gets the prefilter_mask_type of this SearchRequestPrefilters.  # noqa: E501

        mask type \"BYTE\" will contain the whole bitmask while mask type \"INTEGER\" is represented by array of dataset indices which will need to be constructed into bitmask.  # noqa: E501

        :return: The prefilter_mask_type of this SearchRequestPrefilters.  # noqa: E501
        :rtype: str
        """
        return self._prefilter_mask_type

    @prefilter_mask_type.setter
    def prefilter_mask_type(self, prefilter_mask_type):
        """Sets the prefilter_mask_type of this SearchRequestPrefilters.

        mask type \"BYTE\" will contain the whole bitmask while mask type \"INTEGER\" is represented by array of dataset indices which will need to be constructed into bitmask.  # noqa: E501

        :param prefilter_mask_type: The prefilter_mask_type of this SearchRequestPrefilters.  # noqa: E501
        :type: str
        """
        allowed_values = ["BYTE", "INTEGER"]  # noqa: E501
        if prefilter_mask_type not in allowed_values:
            raise ValueError(
                "Invalid value for `prefilter_mask_type` ({0}), must be one of {1}"  # noqa: E501
                .format(prefilter_mask_type, allowed_values)
            )

        self._prefilter_mask_type = prefilter_mask_type

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
        if issubclass(SearchRequestPrefilters, dict):
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
        if not isinstance(other, SearchRequestPrefilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other