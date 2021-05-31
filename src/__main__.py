from cowin import find_vaccine
import time
from datetime import date

district_ids = ["363", "391"]
MINUTES = 5 * 60

if __name__ == '__main__':
    while True:
        date_to = date.today().strftime("%d-%m-%Y")
        for district in district_ids:
            find_vaccine(district, date_to)
        time.sleep(MINUTES)
