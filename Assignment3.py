'''Ali Nasrallah, Data Science Bootcamp 3'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Question 1
url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)
df.hour_beginning = pd.to_datetime(df['hour_beginning'])
df = df.loc[df['hour_beginning'].dt.day_name()!='Sunday']
df = df.loc[df['hour_beginning'].dt.day_name()!='Saturday']
plt.figure(figsize=(12,6))
plt.plot(df['hour_beginning'].dt.day_name(), df['Pedestrians'], color='blue')
plt.title('Pedestrian Counts on Different Days of the Week')
plt.xlabel('Days of the Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()



#Question 2
url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)
df.hour_beginning = pd.to_datetime(df['hour_beginning'])
df = df.loc[df['hour_beginning'].dt.year==2019]
df.sort_values(by='weather_summary')

encode = {'cloudy': 3, 'clear-night': 1, 'clear-day': 0, 'partly-cloudy': 2, 'fog': 4, 'rain': 5, 'snow': 6, 'sleet': 7}
    
df['weather_encoded'] = df['weather_summary'].map(encode)


correlation_matrix = df[['Pedestrians', 'weather_encoded']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matirx of Pedestrians and Weather Conditions')
plt.tight_layout()
plt.show()



#Question 3
def categorize(hour):
    if hour >= 20 and hour < 24:
        return 'night'
    elif hour >= 17 and hour < 20:
        return 'evening'
    elif hour >= 12 and hour < 17:
        return 'afternoon'
    else:
        return 'morning'
    
url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)
df.hour_beginning = pd.to_datetime(df['hour_beginning'])
df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize)
df.groupby(df['time_of_day'])['Pedestrians'].sum()
plt.figure(figsize=(12,6))
plt.plot(df['time_of_day'], df['Pedestrians'], color='blue')
plt.title('Pedestrian Counts on Different Days of the Week')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()





