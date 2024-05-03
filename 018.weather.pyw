import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import tkinter as tk
from tkinter import *
from tkinter import Label
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
import threading
import sqlite3
import os
import sv_ttk
import datetime

lat = 48.837686896793855
lon = 2.4084635621532913

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession("./data/weatherdata/.weathercache", expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/meteofrance"
params = {
	"latitude": lat,
	"longitude": lon,
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "uv_index_max", "precipitation_sum", "wind_speed_10m_max", "wind_direction_10m_dominant"],
	"timezone": "Europe/London"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
daily_uv_index_max = daily.Variables(3).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(4).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(5).ValuesAsNumpy()
#daily_wind_direction_10m_dominant = daily.Variables(6).ValuesAsNumpy()
#print("win_dir : " + str(daily_wind_direction_10m_dominant))

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["weather_code"] = daily_weather_code
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["uv_index_max"] = daily_uv_index_max
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
#daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant

# error with Wind Dir: struct.error: unpack_from requires a buffer of at least 4294967294 bytes for unpacking 4 bytes at offset 4294967290 (actual buffer size is 416)
#print(daily_data)

#{
#	'date': DatetimeIndex(
#	['2024-02-29 00:00:00+00:00', '2024-03-01 00:00:00+00:00', '2024-03-02 00:00:00+00:00', '2024-03-03 00:00:00+00:00'], dtype='datetime64[ns, UTC]', freq='D'),
#	'weather_code': array([55., 61., 61., 55.], dtype=float32),
#	'temperature_2m_max': array([11.2695, 11.2695, 10.2695,  8.2325], dtype=float32),
#	'temperature_2m_min': array([7.7695   , 4.6695   , 5.4824996, 1.8825   ], dtype=float32),
#	'uv_index_max': array([2.1000001, 9.900001 , 8.3      , 1.7      ], dtype=float32),
#	'precipitation_sum': array([20.5484  , 28.820242, 20.532627, 11.792404], dtype=float32),
#	'wind_speed_10m_max': array([185.14575, 202.34814, 196.3436 , 243.06569], dtype=float32)
#}

daily_dataframe = pd.DataFrame(data = daily_data)
#print(daily_dataframe)

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('./data/weatherdata/.airqualitycache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
	"latitude": lat,
	"longitude": lon,
	"hourly": ["pm10", "pm2_5", "carbon_monoxide", "nitrogen_dioxide", "sulphur_dioxide", "ozone", "aerosol_optical_depth", "dust", "ammonia", "alder_pollen", "birch_pollen", "grass_pollen", "mugwort_pollen", "olive_pollen", "ragweed_pollen"],
	"past_hours": 1,
	"forecast_hours": 24
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_pm10 = hourly.Variables(0).ValuesAsNumpy()
hourly_pm2_5 = hourly.Variables(1).ValuesAsNumpy()
hourly_carbon_monoxide = hourly.Variables(2).ValuesAsNumpy()
hourly_nitrogen_dioxide = hourly.Variables(3).ValuesAsNumpy()
hourly_sulphur_dioxide = hourly.Variables(4).ValuesAsNumpy()
hourly_ozone = hourly.Variables(5).ValuesAsNumpy()
hourly_aerosol_optical_depth = hourly.Variables(6).ValuesAsNumpy()
hourly_dust = hourly.Variables(7).ValuesAsNumpy()
hourly_ammonia = hourly.Variables(8).ValuesAsNumpy()
hourly_alder_pollen = hourly.Variables(9).ValuesAsNumpy()
hourly_birch_pollen = hourly.Variables(10).ValuesAsNumpy()
hourly_grass_pollen = hourly.Variables(11).ValuesAsNumpy()
hourly_mugwort_pollen = hourly.Variables(12).ValuesAsNumpy()
hourly_olive_pollen = hourly.Variables(13).ValuesAsNumpy()
hourly_ragweed_pollen = hourly.Variables(14).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["pm10"] = hourly_pm10
hourly_data["pm2_5"] = hourly_pm2_5
hourly_data["carbon_monoxide"] = hourly_carbon_monoxide
hourly_data["nitrogen_dioxide"] = hourly_nitrogen_dioxide
hourly_data["sulphur_dioxide"] = hourly_sulphur_dioxide
hourly_data["ozone"] = hourly_ozone
hourly_data["aerosol_optical_depth"] = hourly_aerosol_optical_depth
hourly_data["dust"] = hourly_dust
hourly_data["ammonia"] = hourly_ammonia
hourly_data["alder_pollen"] = hourly_alder_pollen
hourly_data["birch_pollen"] = hourly_birch_pollen
hourly_data["grass_pollen"] = hourly_grass_pollen
hourly_data["mugwort_pollen"] = hourly_mugwort_pollen
hourly_data["olive_pollen"] = hourly_olive_pollen
hourly_data["ragweed_pollen"] = hourly_ragweed_pollen

root = tk.Tk()
root.title("Weather Forecast")
root.iconbitmap("./data/icons/python1.ico")
root.geometry("468x760") 
#root.minsize(468, 760)
root.resizable(False, False)

geolocator = Nominatim(user_agent="weatherapp")
latlon = str(lat)+","+str(lon)
location = geolocator.reverse(latlon)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')

myLabel = Label(root, text=city+" "+zipcode)
myLabel.grid(row=0, column=0, columnspan=4, padx=20, pady=5)
myLabel = Label(root, text="Aujourd'hui")
myLabel.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
myLabel = Label(root, text="Demain")
myLabel.grid(row=1, column=2, columnspan=2, padx=20, pady=5)

forecastIndexes = [0,1,2,3,45,48,51,53,55,56,57,61,63,65,66,67,71,73,75,77,80,81,82,85,86,95,96,99] 	
forecastIcons = [
	"10000_clear_large.png",
	"11000_mostly_clear_large.png",
	"11010_partly_cloudy_large.png",
	"11020_mostly_cloudy_large.png",
	"21000_fog_light_large.png",
	"20070_fog_rime_large.png",
	"40000_drizzle_large.png",
	"40000_drizzle_large.png",
	"40000_drizzle_large.png",
	"60000_freezing_rain_drizzle_large.png",
	"60000_freezing_rain_drizzle_large.png",
	"42000_rain_light_large.png",
	"40010_rain_large.png",
	"42010_rain_heavy_large.png",
	"51000_snow_light_large.png",
	"50000_snow_large.png",
	"51010_snow_heavy_large.png",
	"50010_flurries_large.png",
	"42140_rain_light_partly_cloudy_large.png",
	"42080_rain_partly_cloudy_large.png",
	"42020_rain_heavy_partly_cloudy_large.png",
	"51000_snow_light_large.png",
	"51010_snow_heavy_large",
	"80020_tstorm_mostly_cloudy_large.png",
	"80000_tstorm_large.png",
	"80090_tstorm_hail_large.png"
]

iconwidth = 72
iconheight = 72
def loadIcon(rownbr,colnbr,value):
	indexLookup = forecastIndexes.index(value)
	iconpath = "./data/weatherdata/icons/"+forecastIcons[indexLookup]
	print(iconpath) 
	icon = Image.open(iconpath)
	resized = icon.resize((iconwidth, iconheight))
	resized_icon = ImageTk.PhotoImage(resized)
	myLabel = Label(image=resized_icon)
	myLabel.grid(row=rownbr, column=colnbr, columnspan=2, padx=20, pady=5)
	myLabel.image = resized_icon

dataColors = ["#00ff0c","#83cd06","#ff9e00","#ff4d00","#ff0000","#ac0087","#6200ff"]
def getIconColor(val,max):
	print("input value : " + str(val) + " max value = " + str(max))
	#normalized = val/max
	normalized = val/(max/6)
	
	index = round(normalized)
	
	if val < 0:
		index = -1
	
	if index > 6:
		index = 6
	
	if index < 0:
		#Freezing temperatures
		color = "#008aff"
	else:
		color = dataColors[index]
		
	print("output value : " + str(index))
	return color

# Parcourir les données quotidiennes et afficher chaque entrée dans une étiquette
currow = 2
for i, (key, value) in enumerate(daily_data.items()):
	if i != 0:  # Ne pas afficher la première entrée
		if currow == 2:
			#Icons
			value1 = round(value[0])
			value2 = round(value[2])
			loadIcon(currow,0,value1)
			loadIcon(currow,2,value2)
		else:
			value1 = round(value[0],1)
			value2 = round(value[1],1)
			if currow == 3:
				#Tmax
				pretxt = "Tmax : "
				postxt = " °c"
				val_max = 35
			if currow == 4:
				#Tmin
				pretxt = "Tmin : "
				postxt = " °c"
				val_max = 35
			if currow == 5:
				#SunUV
				pretxt = "UV : "
				postxt = ""
				val_max = 12
			if currow == 6:
				#Precipitation
				pretxt = "Pluie : "
				postxt = " mm"
				val_max = 200
			if currow == 7:
				#WindSpeed
				value1 = value1/10
				value2 = value2/10
				value1 = round(value1,1)
				value2 = round(value2,1)
				pretxt = "Vent : "
				postxt = " km/h"
				val_max = 200
			
			print("asking colorindex for " + pretxt)
			color1 = getIconColor(value1,val_max)
			color2 = getIconColor(value2,val_max)
			label_text1 = pretxt+str(value1)+postxt # Texte de l'étiquette
			label_text2 = pretxt+str(value2)+postxt # Texte de l'étiquette
			myLabel = Label(root, text=label_text1) # Créer l'étiquette
			myLabel.grid(row=currow, column=0, padx=20, pady=5)
			myLabel = Label(root, text="●", padx=0, pady=0, fg=color1, font=('Times New Roman', 15, 'bold'))
			myLabel.grid(row=currow, column=1, padx=0, pady=0)
			myLabel = Label(root, text=label_text2) # Créer l'étiquette
			myLabel.grid(row=currow, column=2, padx=20, pady=5)
			myLabel = Label(root, text="●", padx=0, pady=0, fg=color2, font=('Times New Roman', 15, 'bold'))
			myLabel.grid(row=currow, column=3, padx=0, pady=0)
		
		currow += 1




# Parcourir les données quotidiennes et afficher chaque entrée dans une étiquette
airQualityIndex = [[],["pm10 : "," µg/m³",150],["pm2.5 : "," µg/m³",75],["CO : "," µg/m³",10000],["NO₂ : "," µg/m³",340],["SO₂ : "," µg/m³",750],["Ozone : "," µg/m³",380],["Aérosols : "," µg/m³",10],["Poussière : "," µg/m³",10],["NH₃ : "," µg/m³",70],["Pollen d'Aulne : "," µg/m³",3],["Pollen de Bouleau : "," µg/m³",3],["Pollen d'Herbes : "," µg/m³",3],["Pollen d'Armoise : "," µg/m³",3],["Pollen d'Olivier : "," µg/m³",3],["Pollen d'Ambrosia : "," µg/m³",3]]

#"date"
#"pm10"
#"pm2_5"
#"carbon_monoxide"
#"nitrogen_dioxide"
#"sulphur_dioxide"
#"ozone"
#"aerosol_optical_depth"
#"dust"
#"ammonia"
#"alder_pollen"
#"birch_pollen"
#"grass_pollen"
#"mugwort_pollen"
#"olive_pollen"
#"ragweed_pollen"

exclude_list = ["date","european_aqi","european_aqi_pm2_5","european_aqi_pm10","european_aqi_nitrogen_dioxide","european_aqi_ozone","european_aqi_sulphur_dioxide"]
keys_list = list(hourly_data.keys())
for key, value in hourly_data.items():
	for index, item in enumerate(value):
		if key not in exclude_list:
			if index == 0:
				key_position = keys_list.index(key)		
				val_max = airQualityIndex[key_position][2]
				value = round(item,1)
				color = getIconColor(value,val_max)
				print("asking colorindex for " + airQualityIndex[key_position][0])
				label_text = airQualityIndex[key_position][0] + str(value) + airQualityIndex[key_position][1] # Texte de l'étiquette
				myLabel = Label(root, text=label_text) # Créer l'étiquette
				myLabel.grid(row=currow, column=0, padx=20, pady=0)
				myLabel = Label(root, text="●", padx=0, pady=0, fg=color, font=('Times New Roman', 15, 'bold'))
				myLabel.grid(row=currow, column=1, padx=0, pady=0)
			if index == 24:
				key_position = keys_list.index(key)
				val_max = airQualityIndex[key_position][2]
				value = round(item,1)
				color = getIconColor(value,val_max)
				print("asking colorindex for " + airQualityIndex[key_position][0])
				label_text = airQualityIndex[key_position][0] + str(value) + airQualityIndex[key_position][1] # Texte de l'étiquette
				myLabel = Label(root, text=label_text) # Créer l'étiquette
				myLabel.grid(row=currow, column=2, padx=20, pady=0)
				myLabel = Label(root, text="●", padx=0, pady=0, fg=color, font=('Times New Roman', 15, 'bold'))
				myLabel.grid(row=currow, column=3, padx=0, pady=0)
				currow += 1
		#else:
			#print(str(value))
			#pass

sv_ttk.set_theme("dark")
root.mainloop()


