import requests
from bs4 import BeautifulSoup
import telegram, time
import logging, sys
from variables import token, chat_id

# debug true/false
logging.basicConfig(stream=sys.stdout, level=logging.ERROR,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("noegig")
logger.setLevel(logging.INFO)

baseurl = "https://www.noegig.at/bestellung/"

# telegram
def send_to_telegram(message):
    bot = telegram.Bot(token)
    text = "found new Gemeinden for noegig: {}, here is the link to the new page: {}".format(message,baseurl)
    bot.sendMessage(chat_id=chat_id, text=text, disable_web_page_preview=True)


def get_new_list():
    list_gemeinden = []
    s = requests.Session()
    site = s.get(url=baseurl)
    soup = BeautifulSoup(site.text, features="html.parser")
    for y in soup.find_all('p', class_='toggler'):
        list_gemeinden.append(y.text)
    return list_gemeinden


def main():
    old_list_gemeinden = get_new_list()

    logger.info("Bot started!")

    while True:
        neue_gemeinden = []
        new_list_gemeinden = get_new_list()
        if len(new_list_gemeinden) == 0:
            logger.info("new_list_gemeinden is empty, maybe Networkerror, waiting a bit and continue to next loop")
            time.sleep(10)
            continue
        for element in new_list_gemeinden:
            if element not in old_list_gemeinden:
                neue_gemeinden.append(element)

        # check if list has entries (list not empty)
        if neue_gemeinden:
            send_to_telegram(neue_gemeinden)
            logger.info("Found new Gemeinden, and sent it to Telegram Notification Channel")

        old_list_gemeinden = new_list_gemeinden

        time.sleep(300)
        logger.info("Neuer Durchgang")


if __name__ == '__main__':
    main()
