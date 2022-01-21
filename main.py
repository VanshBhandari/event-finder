import requests
import json
                  
url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey=yEBm3UuudAzpdQLfC7dR8bB46wlsv7Zh'

city = input("enter the city: ")

start_event_date_input = input("enter start date in YYYY-MM-DD: ")
start_event_date = f'{start_event_date_input}T00:00:00Z'

end_event_date_input = input("enter end date in YYYY-MM-DD: ")
end_event_date = f'{end_event_date_input}T00:00:00Z'

parameters = {
    'city': city,
    'startDateTime': start_event_date,
    'endDateTime': end_event_date
}
response = requests.get(url, parameters)
js = response.json()

try:
    events = js["_embedded"]["events"]
    for i in events:
        name = i["name"]
        local_date = i["dates"]["start"]["localDate"]
        local_time = i["dates"]["start"]["localTime"]
        print(name)
        print(local_date)
        print(local_time)
except KeyError:
    print("enter valid inputs")
