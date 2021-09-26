import requests
import geocoder

bearer_token = '<bearer_token>'



def create_url(woeid):
    url = "https://api.twitter.com/1.1/trends/place.json?id={}".format(woeid)
    return url


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    print("find out what is trending on Twitter near your city")
    while True:
        while True:
            option = input("1: IP location\n2: Input your own location\n")
            if option == "1":
                url = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(geocoder.ip('me').latlng[0], geocoder.ip('me').latlng[1])
                woeid = connect_to_endpoint(url)[0]["woeid"]
                break
            elif option == "2":
                location = input("Your city:")
                url = "https://www.metaweather.com/api/location/search/?query=" + location
                woeid = connect_to_endpoint(url)
                if woeid != []:
                    woeid = woeid[0]["woeid"]
                    break
                else:
                    print("Location not found")
            else:
                print("not valid option")
        try:
            url = create_url(woeid)
            json_response = connect_to_endpoint(url)[0]["trends"]
            for element in json_response:
                print(element['name'])
            break
        except Exception as e:
            print("Location not found, please input a new one")

if __name__ == "__main__":
    main()

