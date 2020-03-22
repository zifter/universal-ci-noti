import datetime
from unittest.mock import patch

import pytest
from universal_ci_noti.noti.consumer.impl.working_hours_filter.default_provider import (
    WorkingHoursProviderDefault,
)
from universal_ci_noti.noti.consumer.impl.working_hours_filter.filter import (
    WorkingHoursFilter,
)

pytestmark = [pytest.mark.asyncio]


@pytest.mark.parametrize(
    "name,dt,result",
    [
        (
            "1 jan, hangover",
            datetime.datetime(year=2020, month=1, day=1, hour=13, minute=00),
            True,
        ),
        (
            "21 march, saturday",
            datetime.datetime(year=2020, month=3, day=21, hour=13, minute=00),
            True,
        ),
        (
            "22 march, sunday",
            datetime.datetime(year=2020, month=3, day=22, hour=13, minute=00),
            True,
        ),
        (
            "23 march, monday, too early",
            datetime.datetime(year=2020, month=3, day=23, hour=8, minute=00),
            True,
        ),
        (
            "23 march, monday, too too late",
            datetime.datetime(year=2020, month=3, day=23, hour=22, minute=00),
            True,
        ),
        (
            "23 march, monday",
            datetime.datetime(year=2020, month=3, day=23, hour=13, minute=00),
            False,
        ),
        (
            "23 march, monday",
            datetime.datetime(year=2020, month=3, day=23, hour=9, minute=00),
            False,
        ),
        (
            "23 march, monday",
            datetime.datetime(year=2020, month=3, day=23, hour=20, minute=00),
            False,
        ),
    ],
)
@patch(
    "universal_ci_noti.noti.consumer.impl.working_hours_filter.filter.WorkingHoursFilter.now"
)
async def test_working_filter_with_default_prodiver(mock, name, dt, result):
    mock.return_value = dt
    flr = WorkingHoursFilter(WorkingHoursProviderDefault())
    assert await flr.filter() is result
