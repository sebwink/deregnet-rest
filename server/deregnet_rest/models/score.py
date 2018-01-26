# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from deregnet_rest.models.base_model_ import Model
from deregnet_rest import util


class Score(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, node_ids: List[str]=None, score_values: List[float]=None):  # noqa: E501
        """Score - a model defined in Swagger

        :param description: The description of this Score.  # noqa: E501
        :type description: str
        :param node_ids: The node_ids of this Score.  # noqa: E501
        :type node_ids: List[str]
        :param score_values: The score_values of this Score.  # noqa: E501
        :type score_values: List[float]
        """
        self.swagger_types = {
            'description': str,
            'node_ids': List[str],
            'score_values': List[float]
        }

        self.attribute_map = {
            'description': 'description',
            'node_ids': 'node_ids',
            'score_values': 'score_values'
        }

        self._description = description
        self._node_ids = node_ids
        self._score_values = score_values

    @classmethod
    def from_dict(cls, dikt) -> 'Score':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Score of this Score.  # noqa: E501
        :rtype: Score
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this Score.

        Description of the score  # noqa: E501

        :return: The description of this Score.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Score.

        Description of the score  # noqa: E501

        :param description: The description of this Score.
        :type description: str
        """

        self._description = description

    @property
    def node_ids(self) -> List[str]:
        """Gets the node_ids of this Score.


        :return: The node_ids of this Score.
        :rtype: List[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids: List[str]):
        """Sets the node_ids of this Score.


        :param node_ids: The node_ids of this Score.
        :type node_ids: List[str]
        """
        if node_ids is None:
            raise ValueError("Invalid value for `node_ids`, must not be `None`")  # noqa: E501

        self._node_ids = node_ids

    @property
    def score_values(self) -> List[float]:
        """Gets the score_values of this Score.


        :return: The score_values of this Score.
        :rtype: List[float]
        """
        return self._score_values

    @score_values.setter
    def score_values(self, score_values: List[float]):
        """Sets the score_values of this Score.


        :param score_values: The score_values of this Score.
        :type score_values: List[float]
        """
        if score_values is None:
            raise ValueError("Invalid value for `score_values`, must not be `None`")  # noqa: E501

        self._score_values = score_values