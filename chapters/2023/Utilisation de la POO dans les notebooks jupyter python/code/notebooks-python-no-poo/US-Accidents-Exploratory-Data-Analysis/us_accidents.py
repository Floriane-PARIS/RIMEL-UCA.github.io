# Jovian Commit Essentials
# Please retain and execute this cell without modifying the contents for `jovian.commit` to work
!pip install jovian --upgrade -q
import jovian
jovian.set_project('us-accidents-41a0c')
jovian.set_colab_id('1vyTk8_JXkhMrNVH5PBvsS4LXmQyFNUZZ')
pip install opendatasets --upgrade --quiet
import opendatasets as od

download_url = 'https://www.kaggle.com/sobhanmoosavi/us-accidents'

od.download(download_url)
data_filename = './us-accidents/US_Accidents_Dec20_Updated.csv'
import pandas as pd
df = pd.read_csv(data_filename)
df
df.info()
df.describe()
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)
missing_percentages = df.isna().sum().sort_values(ascending=False) / len(df)
missing_percentages
type(missing_percentages)
missing_percentages[missing_percentages != 0].plot(kind='barh')
df.columns
df.City
cities = df.City.unique()
len(cities)
cities_by_accident = df.City.value_counts()
cities_by_accident
cities_by_accident[:20]
type(cities_by_accident)
cities_by_accident[:20].plot(kind='barh')
import seaborn as sns
sns.set_style("darkgrid")
sns.histplot(cities_by_accident, log_scale=True)
cities_by_accident[cities_by_accident == 1]
df.Start_Time
df.Start_Time = pd.to_datetime(df.Start_Time)
sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)
sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)
sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sns.distplot(sundays_start_time.dt.hour, bins=24, kde=False, norm_hist=True)
monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]
sns.distplot(monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)
df_2019 = df[df.Start_Time.dt.year == 2019]
sns.distplot(df_2019.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)
df.Start_Lat
df.Start_Lng
sample_df = df.sample(int(0.1 * len(df)))
sns.scatterplot(x=sample_df.Start_Lng, y=sample_df.Start_Lat, size=0.001)
import folium
lat, lon = df.Start_Lat[0], df.Start_Lng[0]
lat, lon
for x in df[['Start_Lat', 'Start_Lng']].sample(100).iteritems():
    print(x[1])
zip(list(df.Start_Lat), list(df.Start_Lng))
from folium.plugins import HeatMap
sample_df = df.sample(int(0.001 * len(df)))
lat_lon_pairs = list(zip(list(sample_df.Start_Lat), list(sample_df.Start_Lng)))
map = folium.Map()
HeatMap(lat_lon_pairs).add_to(map)
map







import jovian
jovian.commit()

