from __future__ import annotations

from enum import Enum
from typing import List, Union


class CmsQueryBuilder:
    """Base class for building CMS queries."""

    def __init__(self, table_name: str) -> None:
        """Constructor

        Args:
            table_name (str): The table name.
        """
        self.table_name = table_name
        self.fields = []
        self.constraints = []

    def select(self, fields: List[Union[str, SI]]) -> CmsQueryBuilder:
        """Define the set of desired fields in your query.
        '*' will be used, if no fields are defined.

        Args:
            fields (List[Union[str, SI]]): The fields. You can pass strings or use the SI enum (or even mix them).

        Returns:
            CmsQueryBuilder: The object itself, so you can chain the function calls. 😎
        """
        self.fields = fields
        return self

    def where(self, constraints: List[str]) -> CmsQueryBuilder:
        """Define the set of desired constraints in your query.

        Args:
            constraints (List[str]): The constraints.

        Returns:
            CmsQueryBuilder: The object itself, so you can chain the function calls. 😎
        """
        self.constraints = constraints
        return self

    def query(self) -> str:
        """Will construct the CMS query-

        Returns:
            str: The query.
        """
        the_query = " ".join(
            [
                "SELECT",
                ", ".join(
                    field if isinstance(field, str) else field.value
                    for field in self.fields
                )
                if self.fields
                else "*",
                "FROM",
                self.table_name,
            ]
        )
        if self.constraints:
            the_query += " WHERE "
            the_query += " AND ".join(self.constraints)

        return the_query


class InfoObjectsQueryBuilder(CmsQueryBuilder):
    """A QueryBuilder for the CI_INFOOBJECTS table."""

    def __init__(self) -> None:
        """Constructor."""
        super().__init__(table_name="CI_INFOOBJECTS")


class ScheduleStatus(Enum):
    """Enum for the Schedule Status.
    You won't have to remember those values anymore! 🤗
    """

    RUNNING = 0
    COMPLETED = 1
    FAILED = 3
    PAUSED = 8
    PENDING = 9


class CmsQueryBuilderUtils:
    """Snippets for constructing CMS queries."""

    only_instances = "SI_INSTANCE = 1"

    @staticmethod
    def schedule_status_is(status: ScheduleStatus) -> str:
        """Snippet for setting a schedule status.

        Args:
            status (ScheduleStatus): The status, via the ScheduleStatus enum. For example 'ScheduleStatus.FAILED'.

        Returns:
            str: The snippet. For example 'SI_SCHEDULE_STATUS = 3'.
        """
        return f"SI_SCHEDULE_STATUS = {status.value}"


class SI(Enum):
    """Enum for the CMS query field.
    You can get autocompletion. 😎"""

    ID = "SI_ID"
    KIND = "SI_KIND"
    NAME = "SI_NAME"
    PARENT_ID = "SI_PARENTID"
    SCHEDULE_INFO = "SI_SCHEDULEINFO"
