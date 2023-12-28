import requests
import schedule
import time 




def check():

    yuuka_url = "https://www.showroom-live.com/api/room/status?room_url_key=JOY_YUUKA_MURAYAMA"
    yuuka_response = requests.get(yuuka_url)
    yuuka_data = yuuka_response.json()

    global YUUKA_is_live_value
    YUUKA_is_live_value = yuuka_data.get("is_live", None)

    print("関数実行完了")

check()

#繰り返し
#schedule.every(10).minutes.do(check)

#while True:
#    schedule.run_pending()
#    time.sleep(1)