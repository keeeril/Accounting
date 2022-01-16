from application.people import get_employees
from application.salary import calculate_salary
import datetime


if __name__ == '__main__':
    dt_now = datetime.datetime.now()
    print(dt_now)
    command = input('Enter command: ')
    if command == 'salary':
        calculate_salary()
    if command == 'people':
        get_employees()
