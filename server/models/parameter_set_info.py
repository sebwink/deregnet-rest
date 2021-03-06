# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from deregnet_rest.models.base_model_ import Model
from deregnet_rest import util


class ParameterSetInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, id: str=None, set_parameters: List[str]=None):  # noqa: E501
        """ParameterSetInfo - a model defined in Swagger

        :param description: The description of this ParameterSetInfo.  # noqa: E501
        :type description: str
        :param id: The id of this ParameterSetInfo.  # noqa: E501
        :type id: str
        :param set_parameters: The set_parameters of this ParameterSetInfo.  # noqa: E501
        :type set_parameters: List[str]
        """
        self.swagger_types = {
            'description': str,
            'id': str,
            'set_parameters': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'set_parameters': 'set_parameters'
        }

        self._description = description
        self._id = id
        self._set_parameters = set_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ParameterSetInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParameterSetInfo of this ParameterSetInfo.  # noqa: E501
        :rtype: ParameterSetInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this ParameterSetInfo.

        Description of the run  # noqa: E501

        :return: The description of this ParameterSetInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ParameterSetInfo.

        Description of the run  # noqa: E501

        :param description: The description of this ParameterSetInfo.
        :type description: str
        """

        self._description = description

    @property
    def id(self) -> str:
        """Gets the id of this ParameterSetInfo.

        Id of the score object  # noqa: E501

        :return: The id of this ParameterSetInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ParameterSetInfo.

        Id of the score object  # noqa: E501

        :param id: The id of this ParameterSetInfo.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def set_parameters(self) -> List[str]:
        """Gets the set_parameters of this ParameterSetInfo.


        :return: The set_parameters of this ParameterSetInfo.
        :rtype: List[str]
        """
        return self._set_parameters

    @set_parameters.setter
    def set_parameters(self, set_parameters: List[str]):
        """Sets the set_parameters of this ParameterSetInfo.


        :param set_parameters: The set_parameters of this ParameterSetInfo.
        :type set_parameters: List[str]
        """
        if set_parameters is None:
            raise ValueError("Invalid value for `set_parameters`, must not be `None`")  # noqa: E501

        self._set_parameters = set_parameters
