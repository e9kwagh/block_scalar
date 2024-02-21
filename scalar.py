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

def peek_hours(date):
    return 

def month_cal():
    """month_cal"""
    datas = extractor()
    month_avg = []
    all_month_date = [] 

    # for month in months:
    #     t_date = f"2022-{month}"
    #     months_data = [
    #         date["date"].split(" ")[0]
    #         for date in datas
    #         if date["date"].startswith(t_date)
    #     ]
    #     months_data = sorted(list(set(months_data)))
    #     all_month_date.append(months_data)
    #     # month_avg = {"date": t_date, "peak_price": 0, "off_peak": 0}
    #     monthly_list = []

    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    for month in months:
        m_date = f"2022-{month}"
        # month_data = [row for row in datas if row["date"].startswith(m_date)]
        months_data = [
            date["date"].split(" ")[0]
            for date in datas
            if date["date"].startswith(m_date)
        ]
        months_data = sorted(list(set(months_data)))
        
        for hour in range(0, 24):
            hour_str = f"0{hour}:00:00" if hour <= 9 else f"{hour}:00:00"
            # data_data = [row for row in datas if row["date"].startswith(month_str)]
            
            for day in range(1, len(months_data) + 1):
                new_day = f"0{day}" if day <= 9 else f"{day}"              
                date_val = f"{m_date}-{new_day} {hour_str}"      
                current_month = [row for row in datas if row["date"].startwith(date_val) ]
           
    return len(months_data)  
    

def check_peak(date):
    datas = extractor()
    date_str, time_str = date.split(" ")
    hour = time_str.split(':')[0]

    day_data =[float(row["price"]) for row in datas if row["date"].startswith(date_str) ]
    if int(hour) <6 and int(hour)>21 :
        day_off_peak_hour = round(
        (sum([i for i in day_data[0:6]]) + sum([i for i in day_data[22:]]))
        / (len(day_data[0:6]) + len(day_data[22:])),
        2,
    )
        return day_off_peak_hour
    else : 
        day_peak_hour = round(sum([i for i in day_data[6:22]]) / len(day_data[6:22]), 2)
    
        return day_peak_hour        


                
if __name__ == "__main__":
    # print(month_cal())
    print(check_peak("2022-01-01 01:00:00"))
 












 # for day in len(1,month+1) :
            
    # print("months_data =",months_data)
    # print("months_data =",all_month_date)
       

        # for dates in months_data:
        #     for date in  dates :
        #         day_data = one_day_data(date)[0]
        #         monthly_list.append(day_data)
    
        # month_avg["peak_price"] = round(
        #     sum([row["peak_hour"] for row in monthly_list]) / len(monthly_list), 2
        # )
        # month_avg["off_peak"] = round(
        #     sum([row["off_peak"] for row in monthly_list]) / len(monthly_list), 2
        # )
        # all_month_avg.append(month_avg)
    # print("monthly_list",monthly_list)
    # return all_month_avg

