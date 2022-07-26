from datetime import datetime, timedelta


def main(users_dict):
    """
    Takes as input a dictionary of user: birthday pairs. Then outputs a dictionary of weekday: usernames pairs for the
    week to come. If run on Monday, the week starts with the previous Saturday and ends on Friday. If run on any other
    day the week starts with this day and ends in 7 days. People with birthdays on the weekend are put on Monday.

    :param users_dict: stores names of users as a string and birthdays as a datetime object
    :return: a dictionary that stores weekdays and usernames of people who have birthdays on that day
    """
    this_week_birthdays = {}
    if datetime.now().date().weekday() == 0:
        start_of_week = datetime.now().date() - timedelta(days=2)
    else:
        start_of_week = datetime.now().date()
    delta = timedelta(weeks=1)
    end_of_week = start_of_week + delta

    for user in users:
        this_years_birthday = user["birthday"].replace(year=start_of_week.year)
        if start_of_week <= this_years_birthday.date() < end_of_week:
            if this_years_birthday.date().weekday() == 6 or this_years_birthday.date().weekday() == 5:
                if "Monday" not in this_week_birthdays:
                    this_week_birthdays["Monday"] = [user["name"]]
                else:
                    this_week_birthdays["Monday"].append(user["name"])
            else:
                weekday = this_years_birthday.date().strftime("%A")
                if weekday not in this_week_birthdays:
                    this_week_birthdays[f"{weekday}"] = [user["name"]]
                else:
                    this_week_birthdays[f"{weekday}"].append(user["name"])

    return this_week_birthdays


if __name__ == "__main__":
    users = [{"name": "Dina", "birthday": datetime(2022, 7, 27)}, {"name": "Dima", "birthday": datetime(2021, 7, 29)},
             {"name": "Dylan", "birthday": datetime(2021, 7, 27)}, {"name": "Bred", "birthday": datetime(2027, 7, 29)},
             {"name": "Kate", "birthday": datetime(2020, 7, 30)}, {"name": "Ted", "birthday": datetime(2019, 7, 31)},
             {"name": "Miryam", "birthday": datetime(1998, 7, 30)}, {"name": "Ruslan", "birthday": datetime(1980, 7, 31)},
             {"name": "Ginger", "birthday": datetime(2018, 7, 24)}, {"name": "Henry", "birthday": datetime(2017, 7, 23)},
             {"name": "Mary", "birthday": datetime(1988, 7, 24)}, {"name": "Barney", "birthday": datetime(1977, 7, 23)},
             {"name": "Diana", "birthday": datetime(2016, 8, 1)}, {"name": "Trevor", "birthday": datetime(2015, 8, 2)},
             {"name": "Tracy", "birthday": datetime(2014, 8, 3)}, {"name": "Peter", "birthday": datetime(2013, 8, 4)}]

    birthdays = main(users)
    for day, users in birthdays.items():
        print(f"{day}: ", end="")
        print(*users, sep=", ")
