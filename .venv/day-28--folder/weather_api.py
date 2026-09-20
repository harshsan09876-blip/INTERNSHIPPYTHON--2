import requests

def get_weather(city):
    
    API_KEY = "MY_API_KEY"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    
    try:
        response = requests.get(URL)
        data = response.json()
        if response.status_code == 200:
            print(f"weather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Weather: {data['weather'][0]['description']}")
        else:
            print(f'City{city} not found. PLease check the name and try again.')
            
    except Exception as e:
        print(f"Something went wrong: {e}")
        
if __name__ == "__main__":
    city = input("Enter the  city name: ")
    get_weather(city)
        