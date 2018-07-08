# -*- coding: utf-8 -*-
import telebot
import urllib.request
import urllib.parse
import requests
import json
import validators
import re
import sqlite3
from bs4 import BeautifulSoup
import time
import threading
import emoji


creator_id={522560313}
sudo_users={522560313}


token="553744104:AAHBfr3UOIaT-tLGaok6tJ62rs5TapZI1IE"
bot=telebot.TeleBot(token)



a="\n \033 Bot Firstname:{} ".format(bot.get_me().first_name)
b="\n \033 Bot ID:{} ".format(bot.get_me().id)
c="\n \033 Bot Is Online Now!"
print(a+b+c)
#--------------------------------------------------------------------------------------------------------------------
                                                        #creating database
#--------------------------------------------------------------------------------------------------------------------
db=sqlite3.connect("c:/users/ali427/desktop/py/mydb.sqlite",check_same_thread=False)
cursor=db.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS group_info(group_id INTEGER,group_charge INTEGER,creator_id INTEGER,lock_link INTEGER,lock_sticker INTEGER,lock_video INTEGER,lock_video_note INTEGER,lock_music INTEGER,lock_voice INTEGER,lock_contact INTEGER,lock_location INTEGER,lock_emoji INTEGER,lock_username INTEGER,lock_photo INTEGER,group_welcome STRING,lock_chat INTEGER,lock_forward INTEGER,group_count INTEGER PRIMARY KEY)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS group_members_info(group_id INTEGER , num_messages INTEGER , num_alert INTEGER , member_count INTEGER PRIMARY KEY)''')
db.commit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                        #set groups
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message:message.text=="ست")
def input_groupid_db(message):
    i = None
    if message.from_user.id in sudo_users:
        for row in cursor.execute('''SELECT group_id FROM group_info'''):
            if message.chat.id in row:
                i = 0
                break
            else:
                i = 1
        try:
            if i == 0:
                bot.reply_to(message,'⛓ گروه از قبل در ليست گروه هاي مديريتي ربات قرار داشت !')
            if i == 1:
                bot.reply_to(message,'☑️ گروه با موفقيت در ليست گروه هاي مديريتي قرار گرفت و به مدت 1 روز شارژ شد لطفا براي شارژ مجدد هرچه زودتر اقدام نماييد .')
                cursor.execute('INSERT INTO group_info(group_id,group_charge,lock_link,lock_sticker,lock_video,lock_username,lock_photo,lock_chat,lock_forward,lock_video_note,lock_music,lock_voice,lock_contact,lock_location,lock_emoji,group_welcome) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(message.chat.id,1,0,0,0,0,0,0,0,0,0,0,0,0,0,str(0),))
                db.commit()
        except Exception as e:
            print(e)
#--------------------------------------------------------------------------------------------------------------------------------------------------
                                                     #charge groups
#--------------------------------------------------------------------------------------------------------------------------------------------------            
@bot.message_handler(regexp = "^charge")
def charge(message):
    i = None
    if message.from_user.id in sudo_users:
        for row in cursor.execute('''SELECT group_id FROM group_info'''):
            if message.chat.id in row:
                i = 1
            else:
                i = 0
        try:
            if i==1:
                cursor.execute('''UPDATE group_info SET group_charge=? WHERE group_id=?''',(message.text.split()[1],message.chat.id))
                db.commit()
                bot.reply_to(message,"ϟ گروه به مدت {} شارژ شد .".format(message.text.split()[1]))
                Timer(message.text.split()[1],bot.leave_chat(message.chat.id))
            if i==0:
                bot.reply_to(message,"✖ لطفا ابتدا دستور ست را ارسال نماييد .")
        except Exception as e:
            print(e)

        

            

    

#-----------------------------------------------------------------------------------------------------------------------------------------------------
                                              #leave , add sudo , new chat member
#-----------------------------------------------------------------------------------------------------------------------------------------------------        
@bot.message_handler(commands=['start'])
def reply_start(message):
    bot.reply_to(message,"Hi I Am Created By @mlcft")


@bot.message_handler(commands=['help'])
def reply_help(message):
    bot.reply_to(message,"No Help")


@bot.message_handler(func=lambda message:message.text=="leave")
def leave(message):
    if message.from_user.id in sudo_users:
        ID=message.chat.id
        #cursor.execute('''DELETE FROM info WHERE group_id=?''',(ID,))
        #db.commit()
        bot.leave_chat(message.chat.id)
    else:
        bot.reply_to(message,"شما سودو نيستيد")
		
		
@bot.message_handler(func=lambda message:message.text=="درباره ربات" or message.text=="first bot" or message.text=="فرست بات")
def about(message):
    bot.reply_to(message,"\n ربات ضد اسپم و مدیریت گروه فوق پیشرفته فرست \n صاحب امتیاز ربات : معین دلاوری   \n شناسه سازنده : @mlcft\n • سودوی ربات : رها تهرانی ℡ @End_021 \n برنامه نویسی شده توسط : تیم برنامه نویسی فرست \n  گروه پشتیبانی : t.me/joinchat/blablabla \n برای خریداری و مشورت با سودوهای ربات به گروه پشتیبانی مراجعه فرمایید \n  ─┅━━━━━━━┅─ \n FIRST™")
    img = open("c:/users/ali427/desktop/picture/bot.gif" , "rb")
    bot.send_document(message.chat.id,img)

@bot.message_handler(content_types=["new_chat_members"])
def welcome(m):
        j = cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,))
   # try:
        if m.new_chat_member.id==bot.get_me().id:
            if m.from_user.id in sudo_users:
                bot.send_message(m.chat.id,"® با سلام از خريداري و اعتماد شما متشکريم از امکانات فوق العاده ربات پيشرفته مديريت گروه فرست لذت ببريد , لطفا قبل از هر اقدامی ابتدا ربات را ادمین کنید.\n• صاحب امتیاز ربات : معین دلاوری ℡ @mlcft \n • سودوی ربات : رها تهرانی ℡ @End_021 \n─┅━━━━━━━┅─\n  FIRST™   ")
                img = open("c:/users/ali427/desktop/picture/bot.gif" , "rb")
                bot.send_document(m.chat.id,img)

				
			   # for row in cursor.execute('SELECT group_charge FROM group_info WHERE group_id = ?',(m.chat.id,)):
				#    for r in row:
				  #          Timer(r,lambda time:bot.leave_chat(m.chat.id),args=(time,))


            else:
                bot.send_message(m.chat.id,"✗ لطفا از سودوهاي ربات بخواهيد ربات را به گروه شما بياورند \n• سودوی ربات : رها تهرانی ℡ @End_021 \n ─┅━━━━━━━┅─ \n FIRST™  ")
                bot.leave_chat(m.chat.id)
        else:
            if m.new_chat_member.is_bot==True and bot.get_chat_member(m.chat.id,bot.get_me().id).status=="administrator" and (bot.get_chat_member(m.chat.id,m.from_user.id).status != "administrator" and bot.get_chat_member(m.chat.id,m.from_user.id).status != "creator"):
                bot.kick_chat_member(m.chat.id,m.new_chat_member.id)
                bot.reply_to(m,"■ کاربر ["+m.from_user.first_name+"  -  "+str(m.from_user.id)+"] قفل ربات در اين گروه فعال است و افزودن ربات ممنوع ميباشد !"+"\n \n ›› ربات ["+m.new_chat_member.first_name+"- @"+m.new_chat_member.username+"] اخراج شد.")
            else:
                if j != [(0,)]:
                    if 'FIRSTNAME' in cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0]:
                        if m.new_chat_member.first_name:
                            bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('FIRSTNAME',m.new_chat_member.first_name))
                        else:
                            bot.repply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('FIRSTNAME',' '))
                    if 'LASTNAME' in cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0]:
                        if m.new_chat_member.last_name:
                            bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('LASTNAME',m.new_chat_member.last_name))
                        else:
                            bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('LASTNAME',None))
                    if 'ID' in cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0]:
                        bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('ID',str(m.new_chat_member.id)))
                    if 'GROUP' in cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0]:
                        if m.chat.title:
                            bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('GROUP',m.chat.title))
                        else:
                            bot.reply_to(m,cursor.execute('SELECT group_welcome FROM group_info WHERE group_id=?',(m.chat.id,)).fetchall()[0][0].replace('GROUP',' '))
    # except Exception as e:
     #   print(e)
        


	    
@bot.message_handler(func=lambda message:message.text=="sudo")#bug
def add_sudo(message):
    if message.from_user.id in creator_id:
        sudo_users.add(message.reply_to_message.from_user.id)
        bot.reply_to(message,"™ کاربر مورد نظر با موفقيت به تيم سودوهاي ربات افزوده شد")
    else:
         pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                  #info
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         

@bot.message_handler(func=lambda message:message.text=="info")
def info(message):
    try:
        if message.reply_to_message:
            bot.reply_to(message,"ID : {}".format(message.reply_to_message.sticker.file_id))
        else:
            pass
    except:
        bot.reply_to(message,"فقط براي استيکر ها استفاده کنيد!")








#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                             #ban and restrickt
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#unsokot ro nanveshtam			
			
@bot.message_handler(func=lambda message:message.text=="اخراج" or message.text=="بن")
def kick(message):
    if message.reply_to_message:
        status=bot.get_chat_member(message.chat.id,message.from_user.id).status
        if bot.get_chat_member(message.chat.id,bot.get_me().id).status=="administrator" :
            if status=="creator" or status=="administrator":
                if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status=="member" or bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status=="restricted":
                    bot.kick_chat_member(message.chat.id,message.reply_to_message.from_user.id)
                    bot.reply_to(message,"⛔️ کاربر با موفقیت اخراج شد ")
                else:
                    bot.reply_to(message,"!! دسترسي محدود کردن مديران و سازندگان را ندارم")    
            else:
                bot.reply_to(message,">> شما دسترسی ندارید !!")
        else:
            bot.reply_to(message,"» ادمين نيستم")
    else:
        pass
#unban ro nanveshtam
#-----------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    #promote
#-------------------------------------------------------------------------------------------------------------------------------------------------------    
@bot.message_handler(func=lambda message:message.text=="ترفیع" or message.text=="ارتقاع")
def promote(message):
    if message.reply_to_message:
        status=bot.get_chat_member(message.chat.id,message.from_user.id).status
        if bot.get_chat_member(message.chat.id,message.from_user.id).can_promote_members==True or status=="creator":
            if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status == "member" or bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status == "restricted":
                if bot.get_chat_member(message.chat.id,bot.get_me().id).can_promote_members == True:
                    bot.promote_chat_member(message.chat.id,message.reply_to_message.from_user.id,can_change_info=True,can_delete_messages=True,can_invite_users=True,can_restrict_members=True,can_pin_messages=True,can_promote_members=False)
                    bot.reply_to(message,"◄ کاربر مورد نظر به مقام مديريت گروه ارتقاع يافت")
                else:
                    bot.reply_to(message,"ºº لطفا ابتدا دسترسي افزودن ادمين جديد را به بات بدهيد")
            else:
                bot.reply_to(message,"↕ کاربر مورد نظر از قبل ادمين بود  ")
        else:
            bot.reply_to(message,"₪ شما دسترسي ارتقاع کاربران را نداريد")
    else:
        pass


@bot.message_handler(func=lambda message:message.text=="عزل")
def promote(message):
    if message.reply_to_message:
        status=bot.get_chat_member(message.chat.id,message.from_user.id).status
        if bot.get_chat_member(message.chat.id,message.from_user.id).can_promote_members==True or status=="creator":
            if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status == "administrator" or bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status=="creator":
                if bot.get_chat_member(message.chat.id,bot.get_me().id).can_promote_members == True:
                    if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status != "creator":
                        bot.promote_chat_member(message.chat.id,message.reply_to_message.from_user.id)
                        bot.reply_to(message,"◄ کاربر مورد نظر با موفقيت از مقام مديريت گروه عزل شد.")
                    else:
                        bot.reply_to(message,"» شما دسترسي عزل اين کاربر را نداريد.")
                else:
                    bot.reply_to(message,"ºº لطفا ابتدا دسترسي افزودن ادمين جديد را به بات بدهيد.")
            else:
                bot.reply_to(message,"↕ کاربر مورد نظر از ابتدا مقامي نداشت.  ")
        else:
            bot.reply_to(message,"₪ شما دسترسي عزل کاربران را نداريد.")
    else:
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        #paksazi
#----------------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message:message.text=="پاکسازی")
def delet_message(message):
    status=bot.get_chat_member(message.chat.id,message.from_user.id).status
    ID=message.message_id
    if bot.get_chat_member(message.chat.id,bot.get_me().id).status=="administrator":
        if status=="creator" or status=="administrator":
            try:
                while ID>=0:
                    bot.delete_message(message.chat.id,ID)
                    ID-=1
            except:
                pass
            bot.send_message(message.chat.id,"✓ پاکسازی با موفقیت انجام شد")
    else:
        bot.reply_to(message,"» ادمين نيستم")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                      #pin
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message:message.text=="پین" or message.text=="pin")
def pin(message):
    status=bot.get_chat_member(message.chat.id,message.from_user.id).status
    if message.reply_to_message:
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_pin_messages==True:
            if bot.get_chat_member(message.chat.id,message.from_user.id).can_pin_messages==True or status=='creator':
                if message.reply_to_message!=message.pinned_message:
                    bot.pin_chat_message(message.chat.id,message.reply_to_message.message_id)
                    bot.reply_to(message,"» با موفقيت پين شد.")
            else:
                bot.reply_to(message,"» شما دسترسي نداريد!")
        else:
            bot.reply_to(message,"» دسترسي کافي را ندارم")


#--------------------------------------------------------------------------------------------------------------------------------------------------
                                                                   #group_info
#--------------------------------------------------------------------------------------------------------------------------------------------------    
@bot.message_handler(func=lambda message:message.text=='اطلاعات')
def gap_info(message):
    s = bot.get_chat_member(message.chat.id,message.from_user.id)
    if s.status == 'creator' or s.status == 'administrator':
        for row in cursor.execute('SELECT group_id,lock_link,lock_sticker,lock_video,lock_video_note,lock_photo,lock_username,lock_forward,lock_location,lock_contact,lock_chat,lock_music,lock_voice FROM group_info WHERE group_id=?',(message.chat.id,)):
            A = {1:emoji.emojize("فعال :lock:",use_aliases=True),0:emoji.emojize("غير فعال :closed_lock_with_key:",use_aliases=True)}
            a1 = '» آيدي گروه : {} \n» قفل لينک : {} \n» قفل استيکر : {}\n» قفل فيلم : {}\n» قفل فيلم سلفي : {}\n» قفل عکس : {}\n» قفل يوزرنيم : {}\n» قفل فروارد : {}\n» قفل مکان : {}\n» قفل مخاطب : {}\n» قفل چت : {} \n» قفل موزيک : {} \n» قفل صدا : {} \n'.format(row[0],A[row[1]],A[row[2]],A[row[3]],A[row[4]],A[row[5]],A[row[6]],A[row[7]],A[row[8]],A[row[9]],A[row[10]],A[row[11]],A[row[12]])
            bot.reply_to(message,a1)
            return a1
#-------------------------------------------------------------------------------------------------------------------------------------------------
                                                                  #ghofl ha #hanoz kamel nis
#-------------------------------------------------------------------------------------------------------------------------------------------------        
@bot.message_handler(content_types=['text'])
def all_text(message):
    s = bot.get_chat_member(message.chat.id,message.from_user.id)
    i = None
    r_v = None
    r_vn = None
    r_s = None
    r_p = None
    r_vo = None
    r_m = None
    r_l = None
    r_u = None
    r_f = None
    r_lo = None
    r_c = None
    r_ch = None
    r_e = None
#------------------------------------------------------------------------------------------------------------
    if message.text=='قفل فیلم':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):        
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_video FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_v in row:
                      if r_v == 0:
                          cursor.execute('UPDATE group_info SET lock_video=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فيلم با موفقيت فعال شد .')
                      if r_v == 1:
                          bot.reply_to(message,'⛓ قفل فيلم فعال بود .')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن فیلم':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_video FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_v in row:
                      if r_v == 1:
                          cursor.execute('UPDATE group_info SET lock_video=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فيلم غير فعال شد .')
                      if r_v == 0:
                          bot.reply_to(message,'⛓ قفل فيلم غيرفعال بود .')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#--------------------------------------------------------------------------------------------------------------------    
    if message.text=='قفل استیکر':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_sticker FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_s in row:
                      if r_s == 0:
                          cursor.execute('UPDATE group_info SET lock_sticker=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل استيکر با موفقيت فعال شد .')
                      if r_v == 1:
                          bot.reply_to(message,'⛓ قفل استيکر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن استیکر':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_sticker FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_s in row:
                      if r_s == 1:
                          cursor.execute('UPDATE group_info SET lock_sticker=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل استيکر غير فعال شد .')
                      if r_s == 0:
                          bot.reply_to(message,'⛓ قفل استيکر غير فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#-------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل عکس':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_photo FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_p in row:
                      if r_p == 0:
                          cursor.execute('UPDATE group_info SET lock_photo=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل عکس با موفقيت فعال شد .')
                      if r_p == 1:
                          bot.reply_to(message,'⛓ قفل عکس فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن عکس':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_photo FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_p in row:
                      if r_p == 1:
                          cursor.execute('UPDATE group_info SET lock_photo=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل عکس غير فعال شد .')
                      if r_p == 0:
                          bot.reply_to(message,'⛓ قفل عکس غير فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#----------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل لینک':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_link FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_l in row:
                      if r_l == 0:
                          cursor.execute('UPDATE group_info SET lock_link=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل لينک با موفقيت فعال شد .')
                      if r_l == 1:
                          bot.reply_to(message,'⛓ قفل لينک فعال بود .')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن لینک':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_link FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_l in row:
                      if r_l == 1:
                          cursor.execute('UPDATE group_info SET lock_link=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل لينک غير فعال شد .')
                      if r_l == 0:
                          bot.reply_to(message,'⛓ قفل لينک غير فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#--------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل یوزرنیم':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_username FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_u in row:
                      if r_u == 0:
                          cursor.execute('UPDATE group_info SET lock_username=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل يوزرنيم با موفقيت فعال شد .')
                      if r_u == 1:
                          bot.reply_to(message,'⛓ قفل يوزرنيم فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن یوزرنیم':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_username FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_u in row:
                      if r_u == 1:
                          cursor.execute('UPDATE group_info SET lock_username=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل يوزرنيم غير فعال شد .')
                      if r_u == 0:
                          bot.reply_to(message,'⛓ قفل يوزرنيم غيرفعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل فروارد':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_forward FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_f in row:
                      if r_f == 0:
                          cursor.execute('UPDATE group_info SET lock_forward=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فروارد با موفقيت فعال شد .')
                      if r_f == 1:
                          bot.reply_to(message,'⛓ قفل فروارد فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن فروارد':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_forward FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_f in row:
                      if r_f == 1:
                          cursor.execute('UPDATE group_info SET lock_forward=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فروارد غير فعال شد .')
                      if r_f == 0:
                          bot.reply_to(message,'⛓ قفل فروارد غير فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#--------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل ویس':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_voice FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_vo in row:
                      if r_vo == 0:
                          cursor.execute('UPDATE group_info SET lock_voice=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل ویس با موفقیت فعال شد . ')
                      if r_vo == 1:
                          bot.reply_to(message,'⛓ قفل ویس فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن ویس':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_voice FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_vo in row:
                      if r_vo == 1:
                          cursor.execute('UPDATE group_info SET lock_voice=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل ویس غیر فعال شد .')
                      if r_vo == 0:
                          bot.reply_to(message,'⛓ قفل ویس غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#-----------------------------------------------------------------------------------------------------------------
    if message.text=='قفل موزیک':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_music FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_m in row:
                      if r_m == 0:
                          cursor.execute('UPDATE group_info SET lock_music=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل موزیک با موفقیت فعال شد .')
                      if r_m == 1:
                          bot.reply_to(message,'⛓ قفل موزیک فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن موزیک':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_music FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_m in row:
                      if r_m == 1:
                          cursor.execute('UPDATE group_info SET lock_music=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل موزیک غیر فعال شد .')
                      if r_m == 0:
                          bot.reply_to(message,'⛓ قفل موزیک غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#---------------------------------------------------------------------------------------------------------------
    if message.text=='قفل فیلم سلفی':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_video_note FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_vn in row:
                      if r_vn == 0:
                          cursor.execute('UPDATE group_info SET lock_video_note=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فیلم سلفی فعال شد .')
                      if r_vn == 1:
                          bot.reply_to(message,'⛓ قفل فیلم سلفی فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن فیلم سلفی':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_video_note FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_vn in row:
                      if r_vn == 1:
                          cursor.execute('UPDATE group_info SET lock_video_note=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل فیلم سلفی غیر فعال شد .')
                      if r_vn == 0:
                          bot.reply_to(message,'⛓ قفل فیلم سلفی غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#-------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل مکان':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_location FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_lo in row:
                      if r_lo == 0:
                          cursor.execute('UPDATE group_info SET lock_location=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل مکان فعال شد .')
                      if r_lo == 1:
                          bot.reply_to(message,'⛓ قفل مکان فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن مکان':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_location FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_lo in row:
                      if r_lo == 1:
                          cursor.execute('UPDATE group_info SET lock_location=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل مکان غیر فعال شد .')
                      if r_lo == 0:
                          bot.reply_to(message,'⛓ قفل مکان غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#--------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل مخاطب':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_contact FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_c in row:
                      if r_c == 0:
                          cursor.execute('UPDATE group_info SET lock_contact=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل مخاطب فعال شد .')
                      if r_c == 1:
                          bot.reply_to(message,'⛓ قفل مخاطب فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن مخاطب':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_contact FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_c in row:
                      if r_c == 1:
                          cursor.execute('UPDATE group_info SET lock_contact=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل مخاطب غیر فعال شد .')
                      if r_c == 0:
                          bot.reply_to(message,'⛓ قفل مخاطب غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#------------------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل چت':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_chat FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_ch in row:
                      if r_ch == 0:
                          cursor.execute('UPDATE group_info SET lock_chat=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ فل چت فعال شد .')
                      if r_ch == 1:
                          bot.reply_to(message,'⛓ قفل چت فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن چت':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_chat FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_ch in row:
                      if r_ch == 1:
                          cursor.execute('UPDATE group_info SET lock_chat=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل چت غیر فعال شد .')
                      if r_ch == 0:
                          bot.reply_to(message,'⛓ قفل چت غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#------------------------------------------------------------------------------------------------------------------------------------
    if message.text=='قفل اموجی':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_emoji FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_e in row:
                      if r_e == 0:
                          cursor.execute('UPDATE group_info SET lock_emoji=? WHERE group_id=?',(1,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل اموجی فعال شد .')
                      if r_e == 1:
                          bot.reply_to(message,'⛓ قفل اموجی فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)

        
                

    if message.text=='باز کردن اموجی':
        if bot.get_chat_member(message.chat.id,bot.get_me().id).can_delete_messages==True:
            if (s.can_delete_messages==True) or (s.status=='creator'):
                for row in cursor.execute('SELECT group_id FROM group_info'''):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
            else:
                bot.reply_to(message,'» شما دسترسي نداريد .')
        else:
            bot.reply_to(message,'» لطفا ابتدا ربات را ادمين کنيد !')


        try:
            if i==1:
              for row in cursor.execute('SELECT lock_emoji FROM group_info WHERE group_id=?',(message.chat.id,)):
                  for r_e in row:
                      if r_e == 1:
                          cursor.execute('UPDATE group_info SET lock_emoji=? WHERE group_id=?',(0,message.chat.id))
                          db.commit()
                          bot.reply_to(message,'☑️ قفل اموجی غیر فعال شد .')
                      if r_ch == 0:
                          bot.reply_to(message,'⛓ قفل اموجی غیر فعال بود !')
            if i==0:
                bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
        except Exception as e:
            print(e)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                         #restrict and ban
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if re.search(r'^سکوت(\s\d+)$',message.text):
        def sth():
            bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_add_web_page_previews=True)
        i = re.search(r'\d{1,}',message.text).group(0)
        try:
            if message.reply_to_message:
                if bot.get_chat_member(message.chat.id,bot.get_me().id).can_restrict_members == True:
                    if (s.can_restrict_members==True) or s.status=='creator':
                        if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status not in ['creator' , 'administrator']:    
                            bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id)
                            bot.reply_to(message,"⛔️ کاربر در گروه #سکوت شد و توانایی چت کردن به مدت «{}» دقیقه را نخواهد داشت .".format(re.search(r'\d{1,}',message.text).group(0)))
                            threading.Timer(int(i)*60,sth).start()
                        else:
                            bot.reply_to(message,"» شما نمیتوانید (مدیران , سازندگان) را محدود کنید !")
                    else:
                        bot.reply_to(message,"شما دسترسی ندارید !")
                else:
                   bot.reply_to(message,"» ادمين نيستم")
            else:
                pass
        except Exception as e:
            print(e)



    if re.search(r'^سکوت$',message.text):
        try:
            if message.reply_to_message:
                 if bot.get_chat_member(message.chat.id,bot.get_me().id).can_restrict_members == True:
                    if (s.can_restrict_members==True) or s.status=='creator':
                        if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status not in ['creator' , 'administrator']:    
                            bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id)
                            bot.reply_to(message,'⛔️ کاربر در گروه #سکوت شد و توانایی چت کردن را نخواهد داشت .')
                        else:
                            bot.reply_to(message,'» شما نمیتوانید (مدیران , سازندگان) را محدود کنید !')
                    else:
                        bot.reply_to(message,'شما دسترسی ندارید !')
                 else:
                    bot.reply_to(message,'» ادمين نيستم.')
            else:
                pass
        except Exception as e:
            print(e)


    if re.search(r'لغو\sسکوت$',message.text):
        try:
            if message.reply_to_message:
                if bot.get_chat_member(message.chat.id,bot.get_me().id).can_restrict_members == True:
                    if (s.can_restrict_members==True) or s.status=='creator':
                        if bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status == 'restricted':
                            bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_add_web_page_previews=True)
                            bot.reply_to(message,emoji.emojize(':relaxed: کاربر با موفقيت لغو سکوت شد .',use_aliases=True))
                        else:
                            bot.reply_to(message,'» کاربر از ابتدا سکوت نبود !')
                    else:
                        bot.reply_to(message,'شما دسترسی ندارید !')
                else:
                    bot.reply_to(message,'» ادمين نيستم.')
            else:
                pass
        except Exception as e:
            print(e)
#-------------------------------------------------------------------------------------------------------------------------------------------------
                                               #hobbie
#--------------------------------------------------------------------------------------------------------------------------------------------------
    if message.text=='آیدی' or message.text=='ایدی' or message.text.lower()=='id':
        if (not message.reply_to_message)and(not message.forward_from)and(not message.forward_from_chat):
            try:
                ID = str(message.from_user.id)
                URL = 'https://api.telegram.org/bot'+token+'/getUserProfilePhotos?user_id='+ID
                a=urllib.request.urlopen(URL).read()
                b=json.loads(a)
                cmembers=bot.get_chat_members_count(message.chat.id)
                if b["result"]["photos"] == []:
                    bot.send_photo(message.chat.id,"AgADBAAD_qcxG69p0h4hBXvoQL0SJ47dihoABAPrtkkqM_WPVbcBAAEC","\n• آیدی شما : "+str(message.from_user.id)+"\n• نام شما : "+str(message.from_user.first_name)+"\n• شناسه شما :  @"+str(message.from_user.username)+"\n• نام گروه : "+str(message.chat.title)+"\n• آیدی گروه  :"+str(message.chat.id)+"\n • تعداد پیام های گروه :"+str(message.message_id)+"\n • تعداد افراد گروه :"+str(cmembers) ,reply_to_message_id=message.message_id)
                else:
                    c=b["result"]["photos"][0][0]["file_id"]
                    bot.send_photo(message.chat.id,c,"چه پروفايل خوشگلي♥"+ "\n• آیدی شما :" +str(message.from_user.id)+"\n• نام شما : "+str(message.from_user.first_name)+"\n• شناسه شما :  @"+str(message.from_user.username)+"\n• نام گروه : "+str(message.chat.title)+"\n• آیدی گروه  :"+str(message.chat.id)+"\n • تعداد پیام های گروه :"+str(message.message_id)+"\n • تعداد افراد گروه :"+str(cmembers),reply_to_message_id=message.message_id)
            except Exception as e:
                print(e)

                
        if message.reply_to_message:
            try:
                ID = str(message.reply_to_message.from_user.id)
                URL = 'https://api.telegram.org/bot'+token+'/getUserProfilePhotos?user_id='+ID
                a=urllib.request.urlopen(URL).read()
                b=json.loads(a)
                cmembers=bot.get_chat_members_count(message.chat.id)
                if b["result"]["photos"] == []:
                    bot.send_photo(message.chat.id,"AgADBAAD_qcxG69p0h4hBXvoQL0SJ47dihoABAPrtkkqM_WPVbcBAAEC","\n• آيدي فرد : "+str(message.from_user.id)+"\n• نام فرد : "+str(message.from_user.first_name)+"\n• شناسه فرد :  @"+str(message.from_user.username)+"\n• نام گروه : "+str(message.chat.title)+"\n• آیدی گروه  :"+str(message.chat.id)+"\n • تعداد پیام های گروه :"+str(message.message_id)+"\n • تعداد افراد گروه :"+str(cmembers) ,reply_to_message_id=message.message_id)
                else:
                    c=b["result"]["photos"][0][0]["file_id"]
                    bot.send_photo(message.chat.id,c, "\n• آيدي فرد :" +str(message.reply_to_message.from_user.id)+"\n• نام فرد : "+str(message.reply_to_message.from_user.first_name)+"\n• شناسه فرد :  @"+str(message.reply_to_message.from_user.username)+"\n• نام گروه : "+str(message.chat.title)+"\n• آیدی گروه  :"+str(message.chat.id)+"\n • تعداد پیام های گروه :"+str(message.message_id)+"\n • تعداد افراد گروه :"+str(cmembers),reply_to_message_id=message.message_id)
            except Exception as e:
                    print(e)



    if message.text == 'ربات':
        try:
            if s.status == 'creator' or s.status == 'administrator':
                bot.reply_to(message,'آنلاینم عزیزم ❤️')
        except Exception as e:
            print(e)


    if message.text == 'من کیم':
        try:
            if not message.reply_to_message and not message.forward_from:
                status=bot.get_chat_member(message.chat.id,message.from_user.id).status
                if message.from_user.id in creator_id:
                    bot.reply_to(message,"» شما سازنده ربات هستيد!")
                    bot.send_sticker(message.chat.id,"CAADBAADCQADR7ZSHdFBzdM4zOAYAg",reply_to_message_id=message.message_id)
                else:
                    if message.from_user.id in sudo_users:
                        bot.reply_to(message,"شما ادمين ربات هستيد")
                        bot.send_sticker(message.chat.id,"CAADBAADCAADR7ZSHW9aOLcKBsnvAg",reply_to_message_id=message.message_id)
                    else:
                        if status == "creator":
                            bot.reply_to(message,"»شما سازنده گروه هستيد!")
                            bot.send_sticker(message.chat.id,"CAADBAADBgADR7ZSHTj77H1C75ZJAg",reply_to_message_id=message.message_id)
                        if status == "administrator":
                            bot.reply_to(message,"» شما ادمين گروه هستيد!")
                            bot.send_sticker(message.chat.id,"CAADBAADBQADR7ZSHZTv9hnUG55gAg",reply_to_message_id=message.message_id)
                        if status == "member":
                            bot.reply_to(message,"متاسفم ☹ \n \n »شما هيچ مقامي نداريد !")
                            bot.send_sticker(message.chat.id,"CAADBAADBwADR7ZSHbwep-vQq6k2Ag",reply_to_message_id=message.message_id)
                        if status == "restricted":
                            bot.reply_to(message,"متاسفم ☹ \n \n »شما هيچ مقامي نداريد !")
                            bot.send_sticker(message.chat.id,"CAADBAADBwADR7ZSHbwep-vQq6k2Ag",reply_to_message_id=message.message_id)
        except Exception as e:
            print(e)


    if message.text == 'زمان':
        try:
            URL="http://api.novateam.ml/time.php"
            a=urllib.request.urlopen(URL).read()
            b=json.loads(a)

            url = 'http://www.time.ir/'
            headers = {}
            headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
            req = urllib.request.Request(url , headers=headers)
            resp = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(resp , 'html.parser')
            shamsi = soup.find_all(class_='dateTypeBody')[0]
            letter_shamsi = shamsi.find(class_='show date').text
            num_shamsi = shamsi.find(class_='show numeral').text
            miladi = soup.find_all(class_='dateTypeBody')[2]
            letter_miladi = miladi.find(class_='show date').text
            num_miladi = miladi.find(class_='show numeral').text
            ghamari = soup.find_all(class_='dateTypeBody')[1]
            letter_ghamari = ghamari.find(class_='show date').text
            num_ghamari = ghamari.find(class_='show numeral').text
            falaki = soup.find_all(class_='dateTypeBody')[3]
            falaki_letter = falaki.find(class_='show sign').text
            bot.reply_to(message,"♯ تاريخ امروز : "+b['date']+"\n ♯ روز هفته : "+b['today']+"\n ♯ ساعت : "+b['time']+'\n ♯ تاريخ شمسي : '+str(letter_shamsi)+'\n ♯ تاريخ عددي : '+num_shamsi+'\n ♯ تاريخ ميلادي : '+letter_miladi+'\n ♯ تاريخ عددي : '+num_miladi+'\n ♯ تاريخ قمري : '+letter_ghamari+'\n ♯ تاريخ عددي : '+num_ghamari+'\n ♯ برج فلکي : '+falaki_letter)
        except Ecxeption as e:
            print(e)


    if message.text == 'جک':
        try:
            headers={}
            headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            url = "http://www.akairan.com/fun/funny-story/201322785610.html"
            req = urllib.request.Request(url , headers=headers)
            resp = urllib.request.urlopen(req).read()
            soup = BeautifulSoup(resp , 'html.parser')
            text = soup.find(id="innertop")
            text = text.findAll("p")[15].get_text()
            bot.reply_to(message,str(text))
        except Exception as e:
            print(e)




    if re.search(r'^آب\sو\sهوا\s(.+)',message.text):  #bug
        place = str(re.match(r'^آب\sو\sهوا\s(.+)',message.text).group(1))
        base_url = 'https://query.yahooapis.com/v1/public/yql?'
        yql_query = 'select wind from weather.forecast where woeid in (select woeid from geo.places(1) where text='+'"'+place+'")'
        yql_url = base_url + urllib.parse.urlencode({'q':yql_query}) + '&format=json'
        resp = urllib.request.urlopen(yql_url).read()
        print(resp)
#----------------------------------------------------------------------------------------------------------------------------------
                                                    #welcome message
#----------------------------------------------------------------------------------------------------------------------------------           
    if re.search(r'^تنظیم\sپیام\sورودی(.+)',message.text):
            try:
                if s.status == 'creator':
                    x = str(re.match(r'^تنظیم\sپیام\sورودی(.+)',message.text).group(1))
                    cursor.execute('UPDATE group_info SET group_welcome=? WHERE group_id=?',(x,message.chat.id))
                    db.commit()
                    bot.reply_to(message,emoji.emojize(':heavy_check_mark: پیام خوشامد با موفقیت تغییر یافت .',use_aliases=True))
                else:
                    bot.reply_to(message,emoji.emojize(':sunglasses: » فقط سازنده گروه به این قسمت دسترسی دارد .',use_aqliases=True))
            except Exception as e:
                print(e)
    if re.search(r'حذف\sپیام\sورودی',message.text):
        try:
            if s.status == 'creator':
                cursor.execute('UPDATE group_info SET group_welcome=? WHERE group_id=?',(0,message.chat.id))
                db.commit()
                bot.reply_to(message,emoji.emojize(':exclamation: پیام ورودی با موفقیت حذف شد .',use_aliases=True))
        except Exception as e:
            print(e)
#----------------------------------------------------------------------------------------------------------------------------------
                                              #bottum
#----------------------------------------------------------------------------------------------------------------------------------
    p = bot.get_chat_member(message.chat.id,bot.get_me().id)
    markup = telebot.types.InlineKeyboardMarkup()
    key1 = telebot.types.InlineKeyboardButton(emoji.emojize('اطلاعات گروه :notebook_with_decorative_cover:',use_aliases=True),callback_data='cb')
    key2 = telebot.types.InlineKeyboardButton('تنظیمات ⚙️',callback_data='cb2')
    key3 = telebot.types.InlineKeyboardButton(emoji.emojize('راهنما :mag_right:',use_aliases=True),callback_data='cb3')
    key4 = telebot.types.InlineKeyboardButton(emoji.emojize('خروج :heavy_multiplication_x:',use_aliases=True),callback_data='cb4')
    markup.add(key1)
    markup.add(key2,key3)
    markup.add(key4)
    if message.text == 'پنل':
        if s.status == 'creator':
            for row in cursor.execute('SELECT group_id FROM group_info'):
                    if message.chat.id in row:
                        i = 1
                        break
                    else:
                        i = 0
                
        if i==1:
            if p.can_delete_messages and p.can_invite_users and p.can_restrict_members and p.can_pin_messages and p.can_promote_members == True:                                                          
                bot.reply_to(message,emoji.emojize('به پنل ربات خوش آمدید  :open_file_folder:'),reply_markup=markup)
            else:
                bot.reply_to(message,'» لطفا ابتدا ربات را ادمین کنید و همه دسترسی ها را به ربات بدهید !')
        if i==0:
            bot.reply_to(message,'» لطفا ابتدا از سودوهاي ربات بخواهيد گروه ها ست کنند')
@bot.callback_query_handler(func=lambda call:True)
def reply_group_info_button(call):
   s = bot.get_chat_member(call.message.chat.id,call.from_user.id).status
   if s=='creator':
       if call.data == 'cb':
           for row in cursor.execute('SELECT group_id,lock_link,lock_sticker,lock_video,lock_video_note,lock_photo,lock_username,lock_forward,lock_location,lock_contact,lock_chat,lock_music,lock_voice FROM group_info WHERE group_id=?',(call.message.chat.id,)):
               A = {1:emoji.emojize("فعال :lock:",use_aliases=True),0:emoji.emojize("غير فعال :closed_lock_with_key:",use_aliases=True)}
               a1 = '» آيدي گروه : {} \n» قفل لينک : {} \n» قفل استيکر : {}\n» قفل فيلم : {}\n» قفل فيلم سلفي : {}\n» قفل عکس : {}\n» قفل يوزرنيم : {}\n» قفل فروارد : {}\n» قفل مکان : {}\n» قفل مخاطب : {}\n» قفل چت : {} \n» قفل موزيک : {} \n» قفل صدا : {} \n'.format(row[0],A[row[1]],A[row[2]],A[row[3]],A[row[4]],A[row[5]],A[row[6]],A[row[7]],A[row[8]],A[row[9]],A[row[10]],A[row[11]],A[row[12]])
               bot.reply_to(call.message,a1)
       if call.data == 'cb4':
           bot.edit_message_text('» پنل با موفقیت بسته شد .',call.message.chat.id,call.message.message_id)
           bot.answer_callback_query(call.id,emoji.emojize('پنل با موفقیت بسته شد . :anger:',use_aliases=True))
       if call.data ==  'cb2':
           markup = telebot.types.InlineKeyboardMarkup()
           key5 = telebot.types.InlineKeyboardButton('قفل استیکر ',callback_data='n1')
           markup.add(key5)
           bot.edit_message_text('از این بخش میتوانید تنظیمات و قفل های گروه را مدیریت نمایید ⚙️',call.message.chat.id,call.message.message_id,reply_markup=markup)
   else:
       bot.answer_callback_query(call.id,emoji.emojize('فقط سازنده گروه به تنظیمات پنل ربات دستزسی دارد . :no_entry_sign:',use_aliases=True))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def del_video(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.video:
            for row in cursor.execute('SELECT lock_video FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r in row:
                    if r == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)


def del_video_note(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.video_note:
            for row in cursor.execute('SELECT lock_video_note FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_vn in row:
                    if r_vn == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)
							
							         
def del_sticker(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.sticker:
            for row in cursor.execute('SELECT lock_sticker FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_s in row:
                    if r_s == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)
               

def del_photo(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.photo:
            for row in cursor.execute('SELECT lock_photo FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_p in row:
                    if r_p == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)


def del_voice(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.voice:
            for row in cursor.execute('SELECT lock_voice FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_vo in row:
                    if r_vo == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)
							
							
def del_music(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.audio:
            for row in cursor.execute('SELECT lock_music FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_m in row:
                    if r_m == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)							


def del_location(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.location:
            for row in cursor.execute('SELECT lock_location FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_lo in row:
                    if r_lo == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)								
							
							
def del_contact(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        if message.contact:
            for row in cursor.execute('SELECT lock_contact FROM group_info WHERE group_id=?',(message.chat.id,)):
                for r_c in row:
                    if r_c == 1:
                       if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)
							
							
def del_chat(messages):
	for message in messages:
		s = bot.get_chat_member(message.chat.id,message.from_user.id).status
		if message:
			for row in cursor.execute('SELECT lock_chat FROM group_info WHERE group_id=?',(message.chat.id,)):
				for r_ch in row:
					if r_ch==1:
						if s not in ['creator' , 'administrator']:
							bot.delete_message(message.chat.id,message.message_id)

							
def del_link(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        for row in cursor.execute('SELECT lock_link FROM group_info WHERE group_id=?',(message.chat.id,)):
            for r_l in row:
                if r_l == 1:
                    if message.text:
                        if 'http://' in message.text or 'https://' in message.text or 't.me/' in message.text:
                            if s not in ['creator' , 'administrator']: 
                                bot.delete_message(message.chat.id,message.message_id)
                    if message.caption:
                        if 'http://' in message.caption or 'https://' in message.caption or 't.me/' in message.caption:
                            if s not in ['creator' , 'administrator']:
                                bot.delete_message(message.chat.id,message.message_id)

def del_username(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        for row in cursor.execute('SELECT lock_username FROM group_info WHERE group_id=?',(message.chat.id,)):
            for r_u in row:
                if r_u == 1:
                    if message.text:
                        if '@' in message.text:
                            if s not in ['creator' , 'administrator']: 
                                bot.delete_message(message.chat.id,message.message_id)
                    if message.caption:
                        if '@' in message.caption:
                            if s not in ['creator' , 'administrator']:
                                bot.delete_message(message.chat.id,message.message_id)

                            
def del_forward(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        for row in cursor.execute('SELECT lock_forward FROM group_info WHERE group_id=?',(message.chat.id,)):
            for r_f in row:
                if r_f == 1:
                    if message.forward_from or message.forward_from_chat:
                        if s not in ['creator' , 'administrator']: 
                            bot.delete_message(message.chat.id,message.message_id)  

def del_emoji(messages):
    for message in messages:
        s = bot.get_chat_member(message.chat.id,message.from_user.id).status
        for row in cursor.execute('SELECT lock_emoji FROM group_info WHERE group_id=?',(message.chat.id,)):
            for r_e in row:
                if r_e == 1:
                    pass


bot.set_update_listener(del_video)
bot.set_update_listener(del_video_note)
bot.set_update_listener(del_sticker)
bot.set_update_listener(del_photo)
bot.set_update_listener(del_voice)
bot.set_update_listener(del_music)
bot.set_update_listener(del_chat)
bot.set_update_listener(del_link)
bot.set_update_listener(del_location)
bot.set_update_listener(del_contact)
bot.set_update_listener(del_username)
bot.set_update_listener(del_forward)
bot.set_update_listener(del_emoji)
bot.polling()
