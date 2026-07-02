import time
import schedule
from storage import load_data, save_data
from scraper import scrape

def sale_ended():
    save_data()

def sale_started():
    summary = load_data()
    new = scrape()
    print(
        f"\n------------------------- PODSUMOWANIE --------------------------\n"
        f"{summary['name']}\n"
        f"{summary['actual_price']}\n"
        f"{summary['price_before']}\n"
        f"Ilość: {summary['amount']}\n"
        f"Sprzedanych: {summary['percentage_of_sales']}%\n"
        f"------------------------- NOWA PROMOCJA -------------------------\n"
        f"{new['name']}\n"
        f"{new['actual_price']}\n"
        f"{new['price_before']}\n"
        f"Ilość: {new['amount']}\n"
        f"-----------------------------------------------------------------"
    )

def main():
    schedule.every().day.at("9:59").do(sale_ended)
    schedule.every().day.at("10:01").do(sale_started)
    schedule.every().day.at("21:59").do(sale_ended)
    schedule.every().day.at("22:01").do(sale_started)

    while True:
        schedule.run_pending()
        time.sleep(1)
    


if __name__ == "__main__":
    main()