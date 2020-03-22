import datetime

from .filter import WorkingHoursProvider


class WorkingHoursProviderDefault(WorkingHoursProvider):
    async def is_working_hours(self, dt: datetime.datetime) -> bool:
        if dt.date().weekday() == 5:
            # at friday working day is a bit smaller =)
            return 9 <= dt.time().hour <= 19

        # default working hours
        return 9 <= dt.time().hour <= 20

    async def is_weekend(self, dt: datetime.date) -> bool:
        return dt.weekday() >= 5  # saturday and sunday, by default we are not in Israel

    async def is_holiday(self, dt: datetime.date) -> bool:
        return (dt.month, dt.day) in {
            (1, 1),  # first january
            (12, 25),  # christmas
        }
