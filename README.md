Birthdays Calendar
==================

Helps you not to forget about the birthdays of your significant others.

Takes as input a dictionary of names and birthday dates, where the name is represented with a string and date is 
represented with a datetime object. Then it outputs a list of people who have birthdays on the following week.
People whose birthday this year is on the weekend (Saturdays and Sundays) are displayed on Mondays.

If the script is run on Monday, the week starts on the previous Saturday and ends on Friday. Otherwise, the week starts
on the day it gets run and lasts for 7 days. The list is displayed starting with the day of the run. 
