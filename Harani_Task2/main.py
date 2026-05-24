import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "3874d7204ebc8f273a33efe76a1226e3"

def get_weather():
    city = entry_city.get()

    if city == "":
        messagebox.showerror("Error", "Enter city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        result_label.config(
            text=f"Temp: {temp}°C\nHumidity: {humidity}%\nCondition: {condition}"
        )

    except:
        messagebox.showerror("Error", "Failed to fetch data")

# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City").pack()
entry_city = tk.Entry(root)
entry_city.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()