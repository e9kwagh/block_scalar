"""hourly_price
"""

import os
import csv


def extractor():
    """
    extractor
    """
    filepath = os.path.abspath("hourly_prices.csv")
    with open(filepath, "r", encoding="utf-8-sig") as hour:
        hour_prices = list(csv.DictReader(hour))
    return hour_prices


def one_day_data(date):
    """one day data"""
    datas = extractor()
    single_day = [
        {"date": data["date"].split(" ")[0], "price": float(data["price"])}
        for data in datas
        if data["date"].startswith(date)
    ]

    day_price_list = [float(data["price"]) for data in single_day]
    return single_day, day_price_list


def one_day_peak(date):
    price_list = one_day_data(date)[1]
    day_peak_hour = round(sum([i for i in price_list[6:22]]) / len(price_list[6:22]), 2)
    day_off_peak_hour = round(
        (sum([i for i in price_list[0:6]]) + sum([i for i in price_list[22:]]))
        / (len(price_list[0:6]) + len(price_list[22:])),
        2,
    )
    day_avg = {"date": date, "peak_hour": day_peak_hour, "off_peak": day_off_peak_hour}
    return day_avg




def month_cal():
    """month_cal"""
    datas = extractor()
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    all_month_avg = []

    for month in months:
        t_date = f"2022-{month}"
        months_data = [
            date["date"].split(" ")[0]
            for date in datas
            if date["date"].startswith(t_date)
        ]
        months_data = sorted(list(set(months_data)))

        month_avg = {"date": t_date, "peak_price": 0, "off_peak": 0}
        monthly_list = []

        for date in months_data:
            day_data = one_day_peak(date)
            monthly_list.append(day_data)

        month_avg["peak_price"] = round(
            sum([row["peak_hour"] for row in monthly_list]) / len(monthly_list), 2
        )
        month_avg["off_peak"] = round(
            sum([row["off_peak"] for row in monthly_list]) / len(monthly_list), 2
        )
        all_month_avg.append(month_avg)

    return all_month_avg






def file():
    """file"""
    results = month_cal()
    with open("block.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
        fieldnames = ["date", "peak_price", "off_peak"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(
            [
                {
                    "date": result["date"],
                    "peak_price": result["peak_price"],
                    "off_peak": result["off_peak"],
                }
                for result in results
            ]
        )


if __name__ == "__main__":
    # date = one_day_data("2022-01-01")
    # print(one_day_peak("2022-01-01"))
    print(file())
    print(one_day_peak("2022-01-01"))
