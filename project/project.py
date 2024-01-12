import requests

def main():
    location = get_user_location()
    if location:
        suggest_places(location)

def get_user_location():
    key = "poRCTPjPwMPoNKjUOVrAYYjN4LQkLwfm"
    base_url = "https://www.mapquestapi.com/geocoding/v1/address?key="

    while True:
        valid_location = input("Enter a valid location to explore!: ")
        if validate_location(valid_location):
            main_url = f"{base_url}{key}&location={valid_location}"
            r = requests.get(main_url)
            if r.status_code == 200:
                data = r.json()["results"][0]["locations"][0]
                city = data["adminArea4"]
                state = data["adminArea3"]
                country = data["adminArea1"]
                zipcode = data["postalCode"]
                lat = data["latLng"]["lat"]
                lon = data["latLng"]["lng"]
        
                print("Your location is: ")
                print("City: ",city)
                print("State: ", state)
                print("Country: ", country)
                print("Zip: ", zipcode)
                print("Latitude: ", lat)
                print("Longitude: ", lon)
                return {
                    "city": city,
                    "state": state,
                    "country": country,
                    "zipcode": zipcode,
                    "latitude": lat,
                    "longitude": lon
                }
            else:
                print("Invalid location, please try again")
        else:
            print("Invalid location, please try again")

def validate_location(valid_location):
    return bool(valid_location)


def suggest_places(location):
    key = "poRCTPjPwMPoNKjUOVrAYYjN4LQkLwfm"
    base_url = "https://www.mapquestapi.com/search/v2/radius?"

    location_str = f"{location['latitude']},{location['longitude']}"

    options = {
        "units": "dk",
        "ambiguities": "ignore",
        "outFormat": "json"
    }


    params = {
        "key": key,
        "origin": location_str,
        "ambiguities": options["ambiguities"],
        "units": options["units"],
        "outFormat": options["outFormat"],
    }

    try:
        r = requests.get(base_url, params=params)
        r.raise_for_status()
        response = r.json()
        places = response.get("searchResults", [])
        if places:
            print(f"Here are some places you might like in real driving kms 🚗:")
            for place in places:
                distance = round(place['distance'], 2)
                print(f"{place['name']} - {distance} kms")
        else:
            print(f"No places near you were found!")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching places: {e}")


if __name__ == "__main__":
    main()