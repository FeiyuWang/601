import requests
from datetime import date
from datetime import datetime as dt
from os.path import exists

bearer_token = 'YourToken'


def create_url(name = "twitterdev"):
    url = "https://api.twitter.com/1.1/users/show.json?screen_name={name}".format(name = name)
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

def write_to_file(text):
    with open('out.txt', 'w') as f:
        currenttime = dt.today()
        print(str(text) + "\n" + currenttime.strftime("%m/%d/%Y %H:%M:%S"), file=f)

def read_from_file(text):
    if exists("out.txt"):
        with open("out.txt", "r+") as f:
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]
            last = dt.strptime(lines[-1], "%m/%d/%Y %H:%M:%S")
            lastfan = lines[-2]
            currenttime = dt.strptime(dt.today().strftime("%m/%d/%Y %H:%M:%S"), "%m/%d/%Y %H:%M:%S")
            print(str(text) + "\n" + currenttime.strftime("%m/%d/%Y %H:%M:%S"), file=f)
            print("your follower has increased by {}({}%) over {}".format(text - int(lastfan), round(100 * ((text - int(lastfan)) / int(lastfan)), 2), currenttime - last))
        return 0
    else:
        with open("out.txt", "a+") as f:
            currenttime = dt.strptime(dt.today().strftime("%m/%d/%Y %H:%M:%S"), "%m/%d/%Y %H:%M:%S")
            print(str(text) + "\n" + currenttime.strftime("%m/%d/%Y %H:%M:%S"), file=f)
            print("your current follower amount is {}, run this program again to see how many new follower have followed you since last run".format(text))
        return 1


def main():
    url = create_url()
    fan_count = connect_to_endpoint(url)['followers_count']
    read_from_file(fan_count)


if __name__ == "__main__":
    main()
