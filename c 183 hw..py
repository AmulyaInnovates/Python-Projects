import requests
import json
import tkinter as tk

# Create the root window
root = tk.Tk()
root.geometry("400x400")
root.title("Country Details")
root.config(bg="purple")

# Create the Capital City Name label
city_name_label = tk.Label(root, text="Capital City Name", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
city_name_label.place(x=10, y=10)

# Create the entry field for the capital city name
city_entry = tk.Entry(root, font=("Arial", 12), width=20)
city_entry.place(x=10, y=40)

# Create the Country label
country_label = tk.Label(root, text="Country:", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
country_label.place(x=10, y=80)

# Create the Region label
region_label = tk.Label(root, text="Region:", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
region_label.place(x=10, y=110)

# Create the Language label
language_label = tk.Label(root, text="Language:", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
language_label.place(x=10, y=140)

# Create the Population label
population_label = tk.Label(root, text="Population:", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
population_label.place(x=10, y=170)

# Create the Area label
area_label = tk.Label(root, text="Area:", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333")
area_label.place(x=10, y=200)

def city_details():
    # Send the request to the API
    city_name = city_entry.get()
    api_url = "https://restcountries.com/v2/capital/" + city_name
    api_request = requests.get(api_url)
    api_output_json = json.loads(api_request.content)

    # Display the country details
    country = api_output_json[0]["name"]
    region = api_output_json[0]["region"]
    language = api_output_json[0]["languages"][0]["name"]
    population = api_output_json[0]["population"]
    area = api_output_json[0]["area"]

    country_label.config(text="Country: " + country)
    region_label.config(text="Region: " + region)
    language_label.config(text="Language: " + language)
    population_label.config(text="Population: " + str(population))
    area_label.config(text="Area: " + str(area) + " sq km")

# Create the Get Details button
details_button = tk.Button(root, text="Get Details", font=("Arial", 12), bg="#333", fg="#fff", command=city_details)
details_button.place(x=10, y=240)

root.mainloop()
