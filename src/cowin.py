import requests
from fake_useragent import UserAgent
from telegram import to_telegram

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}


def find_vaccine(district_id, date):
    api_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date
    print(api_url)
    response = requests.get(api_url, headers=browser_header)
    if response.ok:
        resp_json = response.json()
        centers = []

        if resp_json.get('centers'):
            to_send = None
            for center in resp_json.get('centers'):
                for session in center["sessions"]:
                    if int(session["available_capacity_dose1"]) > 4 and session["min_age_limit"] == 18:
                        centers.append("name: " + center["name"])
                        centers.append("address: " + center["address"])
                        centers.append("pincode: " + str(center["pincode"]))
                        centers.append("date: " + session["date"])
                        centers.append("min_age_limit: " + str(session["min_age_limit"]))
                        centers.append("vaccine: " + str(session["vaccine"]))
                        centers.append("available_capacity_dose1: " + str(session["available_capacity_dose1"]))
                        centers.append("available_capacity_dose2: " + str(session["available_capacity_dose2"]))
                        centers.append("")
                        centers.append("")
                        to_send = '\n'.join(centers)

            if to_send is not None:
                to_telegram(to_send)
    else:
        to_telegram("We are having issues while executing command")
