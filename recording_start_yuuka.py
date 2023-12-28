from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import streaming_check_yuuka
import schedule
import time 



def recording():

    def yuuka_recording():
        #録画
        ydl_opts = {
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.showroom-live.com/r/JOY_YUUKA_MURAYAMA'])

        #録画中確認の変数
        global yuuka_rec_check
        yuuka_rec_check = True

    if yuuka_rec_check == False and streaming_check_yuuka.YUUKA_is_live_value == True:
        yuuka_recording()
    elif streaming_check_yuuka.YUUKA_is_live_value == False :
        yuuka_rec_check = False
    else:
        pass

    print("関数実行完了")


recording()

#繰り返し
#schedule.every(10).minutes.do(recording)

#while True:
#    schedule.run_pending()
#    time.sleep(1)