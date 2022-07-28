from datetime import datetime, timedelta
from typing import List, Dict


def main(users_dict: List[Dict[str, datetime]]) -> None:
    """
    Takes as input a dictionary of user: birthday pairs. Then outputs and prints a list of lists with names of people whose
    birthdays are in the range of the next seven days. Indices of the sublists correspond to the days of the week (the
    weekend is omitted).
    If run on Monday, the week starts with the previous Saturday and ends on Friday. If run on any other
    day the week starts with this day and ends in 7 days. People with birthdays on the weekend are put on Monday.
    :param users_dict: stores names of users as a string and birthdays as a datetime object
    :return: a list of lists where sublists store the names of people who have birthdays this week
    """
    start = datetime.now().date()
    if start.weekday() == 0:
        start_of_week = start - timedelta(days=2)
    else:
        start_of_week = start
    week_delta = timedelta(weeks=1)
    end_of_week = start_of_week + week_delta

    result = [[], [], [], [], []]
    for user in users_dict:
        this_years_birthday = user["birthday"].replace(year=start_of_week.year).date()
        birthday_weekday = this_years_birthday.weekday()
        if start_of_week <= this_years_birthday < end_of_week:
            if birthday_weekday > 4:
                result[0].append(user["name"])
            else:
                result[birthday_weekday].append(user["name"])

    weekday_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for delta in range(0, 7):
        weekday = (start + timedelta(days=delta)).weekday()
        if weekday <= 4:
            user_names = result[weekday]
            if len(user_names) > 0:
                print(f"{weekday_labels[weekday]}: {', '.join(user_names)}")


if __name__ == "__main__":
    users = [{"name": "Mary", "birthday": datetime(1993, 7, 23)}, {"name": "Jim", "birthday": datetime(1994, 7, 24)},
             {"name": "Sam", "birthday": datetime(1990, 7, 25)}, {"name": "Kate", "birthday": datetime(1988, 7, 26)},
             {"name": "Olha", "birthday": datetime(1993, 7, 27)}, {"name": "Mary", "birthday": datetime(1999, 7, 28)},
             {"name": "Volodymyr", "birthday": datetime(1990, 7, 29)}, {"name": "Mary", "birthday": datetime(1979, 7, 30)},
             {"name": "Stasy", "birthday": datetime(1995, 7, 31)}, {"name": "Ivan", "birthday": datetime(1969, 8, 1)},
             {"name": "Daria", "birthday": datetime(1990, 8, 2)}, {"name": "Timur", "birthday": datetime(1997, 8, 3)},
             {"name": "Eugen", "birthday": datetime(1996, 8, 4)}, {"name": "Yana", "birthday": datetime(1993, 8, 5)},
             {"name": "Andrew", "birthday": datetime(1991, 7, 28)}, {"name": "Serhiy", "birthday": datetime(1998, 7, 29)},
             {"name": "Mattew", "birthday": datetime(1978, 7, 30)}, {"name": "Ksenia", "birthday": datetime(1995, 7, 31)},
             {"name": "Trevor", "birthday": datetime(1989, 8, 1)}, {"name": "Vlad", "birthday": datetime(1993, 7, 29)}
             ]
    main(users)