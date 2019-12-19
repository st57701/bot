import json
from time import sleep

import requests
import _json

token = "867833069:AAHY6tiiT0OVaaG94O_hzY7SNnakUCqEJWE"

URL = "https://api.telegram.org/bot" + token + "/"

answers_dic={"HI": "Hi, I am bot", "HOW ARE YOU?":"I am good","NAME":"Your name is"} #Dictonary of answers


def get_updates():
    url = URL + "getupdates"
    #print(url)
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id_from_api=data['result'][-1]['message']['chat']['id']
    message_text_from_api =data['result'][-1]['message']['text']
    message_id_from_api = data['result'][-1]['message']['message_id']
    username_from_api= data['result'][-1]['message']['chat']['username']




    message={'chat_id': chat_id_from_api, 'text':message_text_from_api,'message_id':message_id_from_api,
             "username":username_from_api}
    return message


def send_message(chat_id,text):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id,text)
    requests.get(url)




def main():

   msg_id_to_compare=0
   while True:
        answers=get_message()
        if(answers!=None):
            chat_id=answers['chat_id']
            text = answers['text']
            message_id = answers['message_id']
            username = answers['username']
            text_upper=str(text).upper()




            if(text_upper in answers_dic and message_id!=msg_id_to_compare):

               send_message(chat_id,answers_dic[text_upper])
               msg_id_to_compare=message_id

        else:
            continue
        sleep(2)



if __name__ == "__main__":
    main()
