import time
import schedule
from storage import load_data, save_data
from scraper import scrape

def sale_ended():
    save_data()

def sale_started():
    data = scrape()
    print(data['name'])

def main():
    schedule.every().day.at("09:59").do(sale_ended)
    schedule.every().day.at("10:01").do(sale_started)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()