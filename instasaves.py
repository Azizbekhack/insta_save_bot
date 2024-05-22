import requests

def get_insta(link):
    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"


    querystring = {"username_or_id_or_url":"mrbeast"}

    headers = {
        "X-RapidAPI-Key": "e09cc2700bmshb93f24e11f7c72fp174b47jsn0eaef815fac4",
        "X-RapidAPI-Host": "instagram-scraper-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()
    return result