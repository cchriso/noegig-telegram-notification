# noegig-telegram-notification

This script monitors the noegig website for new places (Gemeinden) where fibre optics will be rolled out in Austria.
When new places were found, it will notify me via Telegram.

To use it, you have to fill in your chat_id from telegram, and a token from your Telegram Bot (can easily be created: https://core.telegram.org/bots#6-botfather)

'''bash
docker build -t "noegig-telegram-notification:v1" .
docker run --restart=always noegig-telegram-notification:v1
'''


If you want to learn more about the noegig project visit their site: https://www.noegig.at/

