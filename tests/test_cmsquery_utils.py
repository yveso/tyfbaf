import pytest
from tyfbaf.cmsquery_utils import (
    SI,
    CmsQueryBuilder,
    CmsQueryBuilderUtils,
    InfoObjectsQueryBuilder,
    ScheduleStatus,
)


@pytest.fixture
def basic_CmsQueryBuilder():
    return CmsQueryBuilder("Foo")


class TestCmsQueryBuilder:
    def test_init(self, basic_CmsQueryBuilder: CmsQueryBuilder):
        assert basic_CmsQueryBuilder.table_name == "Foo"
        assert basic_CmsQueryBuilder.fields == []
        assert basic_CmsQueryBuilder.constraints == []

    def test_select_takes_argument(self, basic_CmsQueryBuilder: CmsQueryBuilder):
        basic_CmsQueryBuilder.select(["a", "b", "c"])
        assert basic_CmsQueryBuilder.fields == ["a", "b", "c"]

    def test_where_takes_argument(self, basic_CmsQueryBuilder: CmsQueryBuilder):
        basic_CmsQueryBuilder.where(["a", "b", "c"])
        assert basic_CmsQueryBuilder.constraints == ["a", "b", "c"]

    def test_query_uses_star_and_empty_constraints_when_no_method_is_called(
        self, basic_CmsQueryBuilder: CmsQueryBuilder
    ):
        assert basic_CmsQueryBuilder.query() == "SELECT * FROM Foo"

    def test_query_fields_with_strings_work_as_expected(
        self, basic_CmsQueryBuilder: CmsQueryBuilder
    ):
        basic_CmsQueryBuilder.select(["A", "B"])
        assert basic_CmsQueryBuilder.query() == "SELECT A, B FROM Foo"

    def test_query_fields_with_si_enum_work_as_expected(
        self, basic_CmsQueryBuilder: CmsQueryBuilder
    ):
        basic_CmsQueryBuilder.select([SI.ID])
        assert basic_CmsQueryBuilder.query() == "SELECT SI_ID FROM Foo"

    def test_query_fields_with_strings_and_si_enum_work_as_expected(
        self, basic_CmsQueryBuilder: CmsQueryBuilder
    ):
        basic_CmsQueryBuilder.select(["A", SI.ID])
        assert basic_CmsQueryBuilder.query() == "SELECT A, SI_ID FROM Foo"

    def test_query_constraints_work_as_expected(
        self, basic_CmsQueryBuilder: CmsQueryBuilder
    ):
        basic_CmsQueryBuilder.where(["Constraint", "Constraint2"])
        assert (
            basic_CmsQueryBuilder.query()
            == "SELECT * FROM Foo WHERE Constraint AND Constraint2"
        )


class TestInfoObjectsQueryBuilder:
    def test_table_name_is_correct(self):
        info_objects = InfoObjectsQueryBuilder()
        assert info_objects.table_name == "CI_INFOOBJECTS"


@pytest.mark.parametrize(
    "status, value",
    [
        (ScheduleStatus.RUNNING, 0),
        (ScheduleStatus.COMPLETED, 1),
        (ScheduleStatus.FAILED, 3),
        (ScheduleStatus.PAUSED, 8),
        (ScheduleStatus.PENDING, 9),
    ],
)
def test_ScheduleStatus_values(status: ScheduleStatus, value: int):
    assert status.value == value


class TestCmsQueryBuilderUtils:
    def test_only_instances(self):
        assert CmsQueryBuilderUtils.only_instances == "SI_INSTANCE = 1"

    def test_schedule_status_is(self):
        assert (
            CmsQueryBuilderUtils.schedule_status_is(ScheduleStatus.FAILED)
            == "SI_SCHEDULE_STATUS = 3"
        )


@pytest.mark.parametrize(
    "field, value",
    [
        (SI.ID, "SI_ID"),
        (SI.KIND, "SI_KIND"),
        (SI.NAME, "SI_NAME"),
        (SI.PARENT_ID, "SI_PARENTID"),
        (SI.SCHEDULE_INFO, "SI_SCHEDULEINFO"),
    ],
)
def test_SI_values(field: SI, value: int):
    assert field.value == value
