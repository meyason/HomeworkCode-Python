#日付year-month-day-wdayから辞書を作成してwday-month-day-wdayを出力
date_str = input("year-month-day-wday = ") 
y, m, d, w = date_str.split("-")                     #文字列を-で分割

date_dict = {"year":y, "month":m, "day":d, "wday":w} #date_dictを作成

print("-".join([
    date_dict["wday"],
    date_dict["month"],
    date_dict["day"],
    date_dict["year"]
    ]))