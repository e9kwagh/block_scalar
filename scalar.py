"""scalar.py"""
from datetime import datetime
import csv


def read_hourly_prices(file_path):
    """
    block_and_scalar
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [
            {
                "date": (
                    datetime.strptime(data_row["date"], "%Y-%m-%d %H:%M:%S")
                    if isinstance(data_row["date"], str)
                    else data_row["date"]
                ),
                "price": float(data_row["price"]),
            }
            for data_row in reader
        ]
    return data


def block_and_scalar(hourly_prices):
    """block_and_scalar"""

    hourly_data = {}

    for data_row in hourly_prices:
        hour_key = data_row["date"].strftime("%H:00:00")
        if hour_key not in hourly_data:
            hourly_data[hour_key] = {"sum": 0, "count": 0}
        hourly_data[hour_key]["sum"] += data_row["price"]
        hourly_data[hour_key]["count"] += 1

    block_and_scalar_data = []

    for data_row in hourly_prices:
        hour_key = data_row["date"].strftime("%H:00:00")
        block_value = round(
            hourly_data[hour_key]["sum"] / hourly_data[hour_key]["count"], 2
        )
        scalar = round(
            data_row["price"] / block_value
            if hourly_data[hour_key]["count"] != 0
            else 0,
            2,
        )

        block_and_scalar_data.append(
            {
                "date": data_row["date"].strftime("%Y-%m-%d %H:00:00"),
                "block_value": block_value,
                "scalar": scalar,
            }
        )

    return block_and_scalar_data


def write_block_and_scalar_to_csv(data, output_file_path):
    """
    CSV file.
    """
    with open(output_file_path, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["date", "block_value", "scalar"])
        writer.writeheader()
        writer.writerows(data)


def file():
    """solution_dam"""
    results = block_and_scalar(read_hourly_prices("hourly_prices.csv"))
    write_block_and_scalar_to_csv(results, "scalar_results.csv")


if __name__ == "__main__":
    file()
