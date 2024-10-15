import weather


filename = input("File name: ")
datas = weather.read_data(filename)

report = weather.report_historical(datas)
print(report)

total_rains = weather.tot_rain(data={"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}}, date='20210205')
print(total_rains)
