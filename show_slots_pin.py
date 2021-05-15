"""
Developer     : Naman Dave @NMNDV
Recent Update : 14-05-2021 17:30:12
Developer Site: nmndv.github.io
"""


import time
import requests
import datetime


pincode = 380004

tomorrow_DTO = datetime.date.today() + datetime.timedelta(days=1)
dd = str(tomorrow_DTO.day)
mm = str(tomorrow_DTO.month)
yyyy = str(tomorrow_DTO.year)

# The natural delay for the signal
# The delay to obtain the data and send the user on telegram
# RTT of data server + RTT of telegram server
# This you will have to observe and note.
delay = 0.5  # second

# Telegram bot total session time
total_time = 40 * 60  # seconds

# Refresh time
refresh_time = 1.5 - delay  # seconds

# Time to wait after the slots are found
# Otherwise you will get message after each refresh_time
time_slot_wait = 2.0 - delay  # seconds

# Time to respond the 'No sessions' message
# So that you know the bot is working 😂
no_sess_msg_time = 20  # seconds


if refresh_time < 0.0:
    refresh_time = 0.0

total_ticks = int(total_time / refresh_time)
no_sess_tick = int(no_sess_msg_time / refresh_time)

pin_g = str(pincode)
date_g = dd + "-" + mm + "-" + yyyy



print(
    "Welcome to the CoWIN slot-availibility bot. "
    "Developed by NMNDV (git)"
)
url = (
    "https://cdn-api.co-vin.in/api/v2/appointment/"
    "sessions/public/"
    "findByPin?pincode=" + pin_g + "&date=" + date_g
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    " AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/90.0.4430.212 Safari/537.36"
}

priority_dict = {
    'pincode': "Pincode",
    'available_capacity': "Available Capacity",
    'min_age_limit': 'Minimum age limit',
    'name': 'Name',
    'address': 'Address'
}
take_other_priority = False

time_stemp = 0
t_start = time.time()
while (time.time() - t_start) < total_time:
    lr = requests.get(url, headers=headers)
    try:
        finite = lr.json()
        if finite["sessions"] != []:
            print("Hey!!! I found some sessions 🤗")
            tr1 = ""
            for center in finite["sessions"]:
                for pri_val in priority_dict:
                    try:
                        tr1 += str(priority_dict[pri_val]) + ": " + str(center[pri_val]) + "\n"
                    except:
                        pass
                if take_other_priority:
                    for entry in center:
                        if entry not in priority_dict:
                            print(entry, center[entry], sep=": ")
                            tr1 += str(entry) + ": " + str(center[entry]) + "\n"
            print(tr1)
            time.sleep(time_slot_wait)
        else:
            if ((time_stemp + 1) % no_sess_tick) == 0:
                print("No sessions yet 😐 " + datetime.datetime.now().strftime(
                    "%H:%M:%S"
                    ))
    except:
        if ((time_stemp + 1) % no_sess_tick) == 0:
            print(
                "Server's response failure,"
                " reasons: high traffic, try changing your bot's"
                " User-Agent header, "
                "maybe the server is crashed 🤔 " + datetime.datetime.now(
                ).strftime(
                    "%H:%M:%S"
                    )
            )
        time.sleep(refresh_time)
    time.sleep(refresh_time)
    time_stemp += 1

print(
    "ASBot session completed, please type: run this file again"
    " to start a new session"
)


