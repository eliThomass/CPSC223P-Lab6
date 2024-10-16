import weather
import json
import os

program_finish = False
filename = ''
weather_dict = {}

while not program_finish:
	try:
		print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
		print("1. Set data filename\n")
		print("2. Add weather data\n")
		print("3. Print daily report\n")
		print("4. Print historical report\n")
		print("9. Exit the program\n")
		
		choice = input("Enter menu choice: ")
		
		if choice == '1':
			filename = input("Enter data filename: ")
			weather_dict = weather.read_data(filename)
		elif choice == '2':
			date = input("Enter date (YYYYMMDD): ")
			date += input("Enter time (hhmmss): ")
			temp = int(input("Enter temperature: "))
			hum = int(input("Enter humidity: "))
			rain = float(input("Enter rainfall: "))
			weather_add = {date: {'t': temp, 'h': hum, 'r':rain}}
			print(weather_add)
			weather.write_data(weather_add, filename)
			weather_dict = weather.read_data(filename)
		elif choice == '3':
			date = input("Enter date (YYYYMMDD): ")
			print(weather.report_daily(weather_dict, date))
		elif choice == '4':
			print(weather.report_historical(weather_dict))
		elif choice == '9' or choice == 'quit':
			program_finish = True
		else:
			
	except Exception as e:
		print(f"Unexpected error: {e}")
