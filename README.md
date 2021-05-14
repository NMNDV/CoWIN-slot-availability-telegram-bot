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



# Issues
1) The telegram bot shows the timeout error
- This issue is related to your API's connection with the telegram server (Check your internet)
- What also works: "From one user in telegram, start the conversation with the bot, that will resolve the error"

2) Does not respond to more than one user
- The responsers to the bot are queued up so only one user at a time is responeded as one session lasts around 40 miniuts.
- We get the concurrency by decreasing the session time.
