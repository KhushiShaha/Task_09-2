
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Crime_Data_2023_-_Part_1_Offenses_(With_Lat_&_Long_Info).csv", parse_dates=["Occurred On"])
df["hour"] = df["Occurred On"].dt.hour
df["weekday"] = df["Occurred On"].dt.day_name()

# Hourly crime pattern
hourly = df.groupby("hour").size()
hourly.plot(kind="bar", title="Crimes by Hour", xlabel="Hour of Day", ylabel="Count")
plt.tight_layout()
plt.savefig("crimes_by_hour.png")
plt.clf()

# Weekly pattern
weekly = df.groupby("weekday").size().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
weekly.plot(kind="bar", title="Crimes by Day of Week", xlabel="Day", ylabel="Count")
plt.tight_layout()
plt.savefig("crimes_by_day.png")
