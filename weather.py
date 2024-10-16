import json
import calendar

def read_data(filename):
	try:
		with open(filename, 'r') as f:
			x = json.load(f)
			return x
	except FileNotFoundError:
		return {}
	except:
		print("An unexpected error occurred")
		return {}

def write_data(data, filename):
	try:
		with open(filename, 'r') as f:
			existing_data = json.load(f)		
		existing_data.update(data)
	except FileNotFoundError:
		existing_data = {}
	existing_data.update(data)
	try:
		with open(filename, 'w') as f:
			json.dump(existing_data,f)
	except:
		print("Unexpected error")
		
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
	total_rain = 0.00
	for date_val in data:
		if date_val[:8] == date:
			total_rain += data[date_val]['r']
	return total_rain
	
def report_daily(data, date):
	daily_report =  "========================= DAILY REPORT ========================\n"
	daily_report += "Date                      Time  Temperature  Humidity  Rainfall\n"
	daily_report += "====================  ========  ===========  ========  ========\n"
	
	for date_val in data:
		if date_val[:8] == date[:8]:
			year = date_val[:4]
			month = int(date_val[4:6])
			day = int(date_val[6:8])
			hour = date_val[8:10]
			minute = date_val[10:12]
			second = date_val[12:14].ljust(3)
			
			month_name = calendar.month_name[month]
			formatted_date = f'{month_name} {day}, {year}'.ljust(21)
			
			temp = str(data[date_val]['t']).rjust(11)
			hum = str(data[date_val]['h']).rjust(9)
			rain = data[date_val]['r']
			
			daily_report += '{0} {1}:{2}:{3} {4} {5}      {6:.2f}\n'.format(
							formatted_date, hour, minute, second, temp, hum, rain)
	return daily_report
	
def report_historical(data):
	daily_report =  "============================== HISTORICAL REPORT ===========================\n"
	daily_report += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
	daily_report += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
	daily_report += "====================  ===========  ===========  ========  ========  ========\n"
	dates_in = []
	for date_val in data:
			if dates_in.count(date_val[:8]) == 0:
				dates_in.append(date_val[:8])
				year = date_val[:4]
				month = int(date_val[4:6])
				day = int(date_val[6:8])
				
				month_name = calendar.month_name[month]
				formatted_date = f'{month_name} {day}, {year}'.ljust(21)
				
				min_temp = str(min_temperature(data, date_val)).rjust(11)
				min_hum = str(min_humidity(data, date_val)).rjust(9)
				max_temp = str(max_temperature(data, date_val)).rjust(12)
				max_hum = str(max_humidity(data, date_val)).rjust(9).ljust(14)
				total_rain = tot_rain(data, date_val[:8])
				
				daily_report += '{0} {1} {2} {3} {4} {5:.2f}\n'.format(
								formatted_date, min_temp, max_temp, min_hum, max_hum, total_rain)
	return daily_report
