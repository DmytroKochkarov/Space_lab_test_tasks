from datetime import datetime, timedelta
from typing import List

def new_schedule(days: int, work_days: int, rest_days: int, start_date: datetime) -> List[datetime]:
    schedule = []
    curr_date = start_date
    for i in range(days):
        if i % (work_days + rest_days) < work_days:
            schedule.append(curr_date)
        curr_date += timedelta(days=1)
    return schedule

start_date = datetime(2020, 1, 30)
schedule = new_schedule(days=5, work_days=2, rest_days=1, start_date=start_date)
print(schedule)