import json
import calendar

def read_data(filename):
	try:
		with open(filename) as f:
			x = json.load(f)
			return x
	except:
		return {}

def write_data(data, filename):
		with open(filename, 'a') as f:
			json.dump(data, f)		
		
def max_temperature(data, date):
	date = date[:8]
	max_temperature = -999
	for date_val in data:
		if date_val[:8] == date:
			if data[date_val]['t'] > max_temperature:
				max_temperature = data[date_val]['t']
	return max_temperature
			
def min_temperature(data, date):
	date = date[:8]
	min_temperature = 999
	for date_val in data:
		if date_val[:8] == date:
			if data[date_val]['t'] < min_temperature:
				min_temperature = data[date_val]['t']
	return min_temperature
	
def max_humidity(data, date):
	date = date[:8]
	max_humidity = -999
	for date_val in data:
		if date_val[:8] == date:
			if data[date_val]['h'] > max_humidity:
				max_humidity = data[date_val]['h']
	return max_humidity
			
def min_humidity(data, date):
	date = date[:8]
	min_humidity = 999
	for date_val in data:
		if date_val[:8] == date:
			if data[date_val]['h'] < min_humidity:
				min_humidity = data[date_val]['h']
	return min_humidity		
	
def tot_rain(data, date):
	total_rain = 0
	for date_val in data:
		if date_val[:8] == date:
			total_rain += data[date_val]['r']
	return total_rain
	
def report_daily(data, date):
	daily_report = "========================= DAILY REPORT ========================"
	daily_report += "\nDate                      Time  Temperature  Humidity  Rainfall"
	daily_report += "\n====================  ========  ===========  ========  ========"
	
	for date_val in data:
		if date_val[:8] == date[:8]:
			year = date_val[:4]
			month = int(date_val[4:6])
			day = date_val[6:8]
			hour = date_val[8:10]
			minute = date_val[10:12]
			second = date_val[12:14].ljust(3)
			
			month_name = calendar.month_name[month]
			formatted_date = f'{month_name} {int(day):02d}, {year}'.ljust(21)
			
			temp = str(data[date_val]['t']).rjust(11)
			hum = str(data[date_val]['h']).rjust(9)
			rain = data[date_val]['r']
			
			daily_report += '\n{0} {1}:{2}:{3} {4} {5}      {6:.2f}'.format(
							formatted_date, hour, minute, second, temp, hum, rain)
	return daily_report
