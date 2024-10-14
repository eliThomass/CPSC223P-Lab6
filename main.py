import weather


filename = input("File name: ")
datas = weather.read_data(filename)

report = weather.report_historical(datas)
print(report)
