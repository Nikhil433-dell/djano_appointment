import datetime









date = "2022-03-29 12:34"
date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")

end_time = date + datetime.timedelta(minutes=45)

print(date)
print(end_time)