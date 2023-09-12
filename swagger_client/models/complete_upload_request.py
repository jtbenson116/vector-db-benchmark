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

class CompleteUploadRequest(object):
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
        'file_name': 'str',
        'bucket': 'str',
        'upload_id': 'str',
        'parts': 'list[object]'
    }

    attribute_map = {
        'file_name': 'fileName',
        'bucket': 'bucket',
        'upload_id': 'uploadId',
        'parts': 'parts'
    }

    def __init__(self, file_name=None, bucket=None, upload_id=None, parts=None):  # noqa: E501
        """CompleteUploadRequest - a model defined in Swagger"""  # noqa: E501
        self._file_name = None
        self._bucket = None
        self._upload_id = None
        self._parts = None
        self.discriminator = None
        if file_name is not None:
            self.file_name = file_name
        if bucket is not None:
            self.bucket = bucket
        if upload_id is not None:
            self.upload_id = upload_id
        if parts is not None:
            self.parts = parts

    @property
    def file_name(self):
        """Gets the file_name of this CompleteUploadRequest.  # noqa: E501

        file name  # noqa: E501

        :return: The file_name of this CompleteUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CompleteUploadRequest.

        file name  # noqa: E501

        :param file_name: The file_name of this CompleteUploadRequest.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def bucket(self):
        """Gets the bucket of this CompleteUploadRequest.  # noqa: E501

        bucket name  # noqa: E501

        :return: The bucket of this CompleteUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CompleteUploadRequest.

        bucket name  # noqa: E501

        :param bucket: The bucket of this CompleteUploadRequest.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def upload_id(self):
        """Gets the upload_id of this CompleteUploadRequest.  # noqa: E501

        num of parts which the file split.  # noqa: E501

        :return: The upload_id of this CompleteUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this CompleteUploadRequest.

        num of parts which the file split.  # noqa: E501

        :param upload_id: The upload_id of this CompleteUploadRequest.  # noqa: E501
        :type: str
        """

        self._upload_id = upload_id

    @property
    def parts(self):
        """Gets the parts of this CompleteUploadRequest.  # noqa: E501


        :return: The parts of this CompleteUploadRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this CompleteUploadRequest.


        :param parts: The parts of this CompleteUploadRequest.  # noqa: E501
        :type: list[object]
        """

        self._parts = parts

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
        if issubclass(CompleteUploadRequest, dict):
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
        if not isinstance(other, CompleteUploadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other