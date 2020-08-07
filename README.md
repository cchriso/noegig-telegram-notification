# noegig-telegram-notification

This script monitors the noegig website for new places (Gemeinden) where fibre optics will be rolled out in Lower-Austria.
When new places were found, it will notify me via Telegram.

You have to create a file called **variables.py** in the same directory as the script.py and fill in your chat_id from telegram, as well as the token from your Telegram Bot (can easily be created: https://core.telegram.org/bots#6-botfather)

It should look like this:

```python
chat_id = 1234567
token = "7654321:8d67f7fvs8r6fsd78fgsdr7_sdf4"
```

How to get my chat_id?
1. open this url in your browser. Use your Bot Token (it's the long token) https://api.telegram.org/bot\<yourtoken\>/getUpdates
2. send a message to your bot
3. Refresh the site and look at the result. You should see your chat id


if you want to run this script in a docker container, this is what you'll have to do:

```bash
docker build -t "noegig-telegram-notification:v1" .
docker run --restart=always noegig-telegram-notification:v1
```

If you want to learn more about the noegig project visit their site: https://www.noegig.at/
