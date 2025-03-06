import requests
import sys
import tabulate

def main():
    loc = input("Enter your location: ").lower()
    print(weather(loc))

def weather(loc):
    names = ["City", "Region", "Country", "Temperature", "Wind", "Humidity"]
    try:
        w = requests.get(f"https://api.weatherapi.com/v1/current.json?key=5d84f1e16a5141ab880183953250603&q={loc}")
        w = w.json()
        
        city = w["location"]["name"]
        region = w["location"]["region"]
        country = w["location"]["country"]

        temp = f'{w["current"]["temp_c"]} °C'
        wind = f'{w["current"]["wind_kph"]} kph'
        humidity = f'{w["current"]["humidity"]} %'

        table_data = [[city, region, country, temp, wind, humidity]]

        table = tabulate.tabulate(tabular_data=table_data, headers=names, tablefmt="grid")

        return table

    except requests.RequestException:
        sys.exit("Something went wrong!")
    except KeyError:
        sys.exit("Invalid City")

if __name__ == "__main__":
    main()
