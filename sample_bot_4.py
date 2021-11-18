from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.url_message import URLMessage


import time
import logging
import sched
import threading

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
from keyboard import keyboard_menu

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
bot_configuration = BotConfiguration(
	name='TechAssistant',
	avatar='https://static3.depositphotos.com/1003034/155/i/950/depositphotos_1559329-stock-photo-funny-robot-stay-and-show.jpg',
	auth_token='your_viber_token')

viber = Api(bot_configuration)


@app.route('/', methods=['POST'])
def incoming():
    viber_request = viber.parse_request(request.get_data())
    if isinstance(viber_request, ViberMessageRequest) :
        if viber_request.message.text=="1":
            text=str(viber_request.sender.name+", ми працюємо \nПн-Пт з 09.00 до 19.00, \nСб       з 09.00 до 15.00\nНд     Вихідний")
            message=TextMessage(text=text,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
        elif viber_request.message.text=="2":
            text=str(viber_request.sender.name+", наша адреса \nм. ******* , вул.*******, ** \n(****** ПОВЕРХ)")
            message=TextMessage(text=text,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
        elif viber_request.message.text=="3":
            media="https://www.google.com/maps/place/Stryys%CA%B9kyy+Park,+Lebedyne+Ozero/@49.8253333,24.0272835,17z/data=!4m14!1m8!3m7!1s0x0:0x7b4ade7a5b344dc2!2zNDnCsDQ5JzMxLjIiTiAyNMKwMDEnNDYuMSJF!3b1!7e2!8m2!3d49.8253327!4d24.0294693!3m4!1s0x473add6088eef01f:0x23a4d0bd31a73651!8m2!3d49.826554!4d24.030236"
            message=URLMessage(media=media,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
        elif viber_request.message.text=="4":
            text="*******************"
            media="http://*********.***"
            message=URLMessage(media=media,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
            message=TextMessage(text=text,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
        elif viber_request.message.text=="5":
            text="*********************"
            message=TextMessage(text=text,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])
        elif viber_request.message.text=="6":
            text="***********************"
            text1="***********************"

            message=TextMessage(text=text)
            viber.send_messages(viber_request.sender.id, [message])

            message=TextMessage(text=text1,keyboard=keyboard_menu)
            viber.send_messages(viber_request.sender.id, [message])




    return Response(status=200)



if __name__ == "__main__":
    app.run(port=8090)






