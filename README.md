# CoWIN-Slotbooking-telegram-bot
The ultimate telegram bot that notifies you the available slots for the given locations and districts, with given frequency

First install requirements:
```python
pip install -r requirements.txt
```

Then copy and paste the bot token obtained from [@Botfather](https://t.me/botfather), and paste it on the line below in the py file

```python
TOKEN = "TOKEN from @BotFather"
NAME = "Write down your bot's NAME"
USR_NAME = "Write down your bot's USERNAME"
```

If you want to change the district enter the district ID in the below line of the py file
```python
district_ID = 770  # Ahmedabad
```

The default search date is of tomorrow's date, you can also change it (Make sure the date is the datetime object)
```python
tomorrow_DTO = datetime.date.today() + datetime.timedelta(days=1)
```

# The Bot session:

The approximate total time is stored in the variable total_time
```python
total_time = 40 * 60  # seconds
```
here the total time is 40 miniuts.

The refresh time is stored in the variable refresh_time
```python
refresh_time = 2.0 - delay  # seconds
```
here the delay is the natural delay caused by obtaining the data and sending them to the user on telegram
i.e. the RTT of data server + RTT of telegram server

The time we wait after getting atleast one available slot can be changed as below
```python
time_slot_wait = 6.0 - delay  # seconds
```

When there is no session, we do not remp the message filled with no sessions yet, you can set the no session message time as below
```python
no_sess_msg_time = 2 * 60  # seconds
```

You may change the User-Agent header field if required however the default User-Agent works on every platform
```python
headers = {
        "User-Agent": "Your User-Agent"
    }
```

Then run the file using the below command 
```python
python cowin_bot_main.py
```

Now your bot is online.

# How to use the CoWIN slot booking bot
- Open telegram and search the bot name or the username associated with the given token (A good practice is to store the name and the username in the NAME and the USER_NAME variable in the py file).
- While the py file is running, start the conversation by pressing the start button prompted.
- If you have already started the conversation and want to restart, type /start or /help to start again
- ### Now when the bot send you the slot message, you will get the list of pincode, name, and the age limit. So keep your Aarogya Setu app open and enter the pincode and the name and select the slot and you're done with the slot booking.


# Issues
1) The telegram bot shows the timeout error
- This issue is related to your API's connection with the telegram server (Check your internet)
- What also works: "From one user in telegram, start the conversation with the bot, that will resolve the error"

2) Does not respond to more than one user
- The responsers to the bot are queued up so only one user at a time is responeded as one session lasts around 40 miniuts.
- We get the concurrency by decreasing the session time.
