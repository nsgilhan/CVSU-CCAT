import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

API_KEY = '9c6118629362ebced9a077786c905ee9'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("800x800")

# Load images
sunny_img = ImageTk.PhotoImage(Image.open("sunny.jpg").resize((800, 800)))
rainy_img = ImageTk.PhotoImage(Image.open("rainy.jpg").resize((800, 800)))

# Background label
background_label = tk.Label(root, image=sunny_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Entry for city
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Weather info label
weather_label = tk.Label(root, font=("Arial", 12), bg='gray', justify='left')
weather_label.pack(pady=20)

# Weather fetch function
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    params = {
        'q': f"{city},PH",
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)

        if response.status_code == 200:
            weather = data['weather'][0]['description'].lower()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            print("Ang weather ay " + weather);
            weather_info = (
                f"City: {city.title()}\n"
                f"Weather: {weather.capitalize()}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind: {wind} m/s"
            )
            weather_label.config(text=weather_info)

            # Update image
            if "rain" in weather or "storm" in weather or "drizzle" in weather:
                bg_image = rainy_img
            else:
                bg_image = sunny_img
            background_label.config(image=bg_image)
            background_label.image = bg_image  # keep reference

        else:
            messagebox.showerror("Error", f"City not found: {city}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")

# Button to trigger weather check
get_weather_btn = tk.Button(root, text="The weather is", command=get_weather)
get_weather_btn.pack(pady=10)

root.mainloop()
