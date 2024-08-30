"""
شروع پروژه در تاریخ جمعه 1402/10/27 است
   آخرین باری که روی پروژه کار کردم 1403/02/30
کار های سینا :
ارسال ایمیل #1✳✅✳
نوشتن متن #2✳✅✳
باز کردن نقشه طبق مکان گفته شده من #3✳✅✳
عکس گرفتن #4✳✅✳
فیلم گرفتن #5✳✅✳
ضبط کننده صدا #6✳✅✳
آینه #7✳✅✳
پخش آهنگ #8✳✅✳
چک اتصال به اینترنت #9✳✅✳
متصل شدن به اینترنت #10✳✅✳
ساعت گویا #11✳✅✳
نام امروز #12✳✅✳
عدد خوان #13✳✅✳
تاریخ خوان شمسی #14✳✅✳
تاریخ خوان میلادی #15✳✅✳
تاریخ خوان قمری #16✳✅✳
زمان خوان کامل #17✳✅✳
اجرا کننده نرم افزار #18✳✅✳
سکه انداختن شیر یا خط #19✳✅✳
تاس انداختن #20✳✅✳
خواموش کردن سیستم #21✳✅✳
سرچ در ویکی پدیا #22✳✅✳
سرچ در گوگل #23✳✅✳
جواب درست در برابر افطراء #24✳✅✳
محاسبه ریاضی ساده دم دستی #25✳✅✳
محاسبه ابجد اسامی #26✳✅✳
مترجم #27✳⬜✳
پخش فیلم ها . . .  (به زودی) #28✳⬜✳
مشاوره و قیمت رمز ارز ها (به زودی (کد های تستی در فایل komako))#29✳⬜✳
لطیفه گویی (به زودی) 30#✳⬜✳
فال توپ جادویی (شبیح توپ بیلیارد) (به زودی) 31#✳⬜✳
فال حافظ . . .  (به زودی) 32#✳⬜✳
فال شیخ بهایی . . .  (به زودی) 33#✳⬜✳

"""
################################################
################################################
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyttsx3
import shutil   
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pygame
from pygame import mixer
import webbrowser
import cv2
import wave
from moviepy.editor import VideoFileClip, AudioFileClip
import keyboard
import json
from persian_tools import digits
import pywifi
from pywifi import const
import datetime
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from hijri_converter import Hijri, Gregorian
import random
import wikipedia
import mysql.connector as msc
import math
from playsound import playsound
import time
import pyaudio
import os
import requests
from farsi_tools import standardize_persian_text
from TTS.model import *
import speech_recognition as sr
from translate import *
from translate import Translator



################################################
################ گوش و زبان سینا ###############

def API_tts(Text) :
    model_name = "vits male1 (best)"
    text = str(Text)

    response = requests.post("https://kamtera-persian-tts-coquitts.hf.space/run/predict", json={"data": [text, model_name]}).json()
    data = response["data"]
    url_token = data[0]['name']
    return url_token

def download_file(t):
    url_token = API_tts(t)
    url = f"https://kamtera-persian-tts-coquitts.hf.space/file={url_token}"
    download_path = r'C:\Users\computer\Downloads'

    response = requests.get(url)

    if response.status_code == 200:
        # دریافت نام فایل از URL
        filename = os.path.basename(url)
        # ایجاد مسیر کامل برای ذخیره فایل
        file_path = os.path.join(download_path, filename)
        # ذخیره فایل
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"فایل با نام {filename} با موفقیت دانلود شد.")
    else:
        print("خطا در دریافت فایل.")

def change_name_and_run_sond():
    directory = r'C:\Users\computer\Downloads'
    wav_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            if filename.endswith('.wav'):
                wav_files.append(filename)

    output_path = ""
    wav_file = wav_files[0]
    print(wav_file)
    os.rename(f'C:\\Users\\computer\\Downloads\\{wav_file}', 'C:\\Users\\computer\\Downloads\\sp.wav')
    output_path = "C:\\Users\\computer\\Downloads\\sp.wav"
    playsound(output_path)
    time.sleep(3)

    shutil.move("C:\\Users\\computer\\Downloads\\sp.wav", "C:\\Users\\computer\\Desktop\\sp.wav")

def zaban(matn):
    download_file(matn)
    change_name_and_run_sond()

def goosh(kogaeem) :
    """
    چک میکنه که آیا به اینترنت متصل هست با نه اگر بود با STT گوگل و اگر نبود با STT آفلاین Vosk کار میکنه
    """
    # test_kar = check_internet_connection()
    # if test_kar == True :
    #     try:
    #         r = sr.Recognizer()
    #         mic = sr.Microphone()
    #         with mic as sours:
    #             play_audio("E . or. D:\\you model dataset sonds directory\\بیپ2.mp3")
    #             time.sleep(0.5)
    #             audio = r.listen(sours)
    #             command = r.recognize_google(audio, language='fa-IR')
    #             print(command)
    #             return f"{command}"
    #             if f"{test}" == None:
    #                 return "   "
    #     except Exception :
    #         if kogaeem == "0":
    #             pass
    #         else:
    #             play_audio("E . or. D:\\you model dataset sonds directory\\error.mp3")
    #             time.sleep(1)
    # else:
    try:
        model = Model(r"C:\Program Files\Python310\Lib\site-packages\vosk-model-fa-0.5")
        recognizer = KaldiRecognizer(model, 16000)
        cap = pyaudio.PyAudio()
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        if str(kogaeem) == "1" :
            play_audio("E . or. D:\\you model dataset sonds directory\\بیپ2.mp3")
        elif str(kogaeem) == "0" :
            pass
        time.sleep(0.5)
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result["text"]
                print(text)
                if f"{text}" == None :
                    return "   "
                else:
                    return f"{text}"

    except Exception:
        if kogaeem == "0":
            pass
        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\error.mp3")
            time.sleep(1)

# def goosh_online(kogaeem) :
#     """
#     چک میکنه که آیا به اینترنت متصل هست با نه اگر بود با STT گوگل و اگر نبود با STT آفلاین Vosk کار میکنه
#     """
#     test_kar = check_internet_connection()
#     if test_kar == True :
#         try:
#             r = sr.Recognizer()
#             mic = sr.Microphone()
#             with mic as sours:
#                 play_audio("E . or. D:\\you model dataset sonds directory\\بیپ2.mp3")
#                 time.sleep(0.5)
#                 audio = r.listen(sours)
#                 command = r.recognize_google(audio, language='fa-IR')
#                 print(command)
#                 return f"{command}"
#                 if f"{test}" == None:
#                     return "   "
#         except Exception :
#             if kogaeem == "0":
#                 pass
#             else:
#                 play_audio("E . or. D:\\you model dataset sonds directory\\error.mp3")
#                 time.sleep(1)

def play_audio(file_path):
    print(file_path)
    pygame.init()
    File = f"{file_path}"
    for ad in range(3):
        mixer.init()
        mixer.music.load(File)
        mixer.music.play()

################################################
############# سلام برای بیدار شدن سینا ##########
def get_up_sina():
    play_audio("E . or. D:\\you model dataset sonds directory\\salam.mp3")
    time.sleep(2.5)

################################################
########## توابع کار های سینا با اینترنت #######

def internet() :
    play_audio("E . or. D:\\you model dataset sonds directory\\درحال_اتصال.mp3")
    time.sleep(1)
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    profile = pywifi.Profile()
    profile.ssid = "Baba"
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = "12345qwert"
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(3)
    if iface.status() == const.IFACE_CONNECTED:
        play_audio("E . or. D:\\you model dataset sonds directory\\متصل.mp3")
        time.sleep(2)
        return True
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\عدم_اتصال.mp3")
        time.sleep(5)
        return False

def check_internet_connection():
    try:
        # ارسال درخواست به یک وب‌سایت معتبر
        response = requests.get("https://www.google.com")
        # اگر پاسخ 200 باشد یعنی اینترنت متصل است
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        # در صورت بروز خطا، یعنی اینترنت متصل نیست
        return False

def check_internet_connect() :
    test_check = check_internet_connection()
    if test_check == True :
        play_audio("E . or. D:\\you model dataset sonds directory\\اینترنت شما متصل است.mp3")
        time.sleep(0.8)
    else:
        while True:
            play_audio("E . or. D:\\you model dataset sonds directory\\اینترنت شما متصل نیست آیا وصل کنم.mp3")
            time.sleep(3)
            Q = goosh("0")
            if "بله" in Q:
                internet()
                break
            elif "خیر" in Q:
                play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
                time.sleep(0.9)
                play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
                time.sleep(0.2)
                pas("")
            else:
                play_audio("E . or. D:\\you model dataset sonds directory\\بله یا خیر.mp3")
                time.sleep(2)

        play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
        time.sleep(0.2)
        pas("")

def send_email():
    test_net = check_internet_connection()
    if test_net :
        matn = ""
        adres = ""
        title = ""
        play_audio("E . or. D:\\you model dataset sonds directory\\matn_email.mp3")
        # time.sleep(3)
        while True :
            command = goosh("1")
            if command != "" or command != " ":
                matn = command
                break
            else:
                play_audio("E . or. D:\\you model dataset sonds directory\\matn_khali.mp3")
                # time.sleep(3)
        play_audio("E . or. D:\\you model dataset sonds directory\\adres_email2.mp3")
        # time.sleep(3)
        adreses = {"me": "baraye.meta@gmail.com", "fother": "applytc@gmail.com"}
        while True :
            command2 = goosh("1")
            for i in adreses.keys():
                if i in command2:
                    adres = f"{adreses[i]}"
                    break
                else:
                    play_audio("E . or. D:\\you model dataset sonds directory\\not_email.mp3")
                    time.sleep(2)
                    break
                    adres = ""
            if adres in adreses.values() and adres != "":
                break
        if matn != "" and adres != "" :
            message = MIMEMultipart()
            message["from"] = "name_shakhs"
            message["to"] = f"{adres}"
            message["subject"] = f"هاتف گفت : {title}"
            message.attach(MIMEText(f"{matn}"))
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("your gmail", "your gmail api key")
                smtp.send_message(message)
            play_audio("E . or. D:\\you model dataset sonds directory\\send_mail.mp3")
            time.sleep(3)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
        pas("")
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\تذکر_اینترنت.mp3")
        time.sleep(5)
        comm = goosh("1")
        if "بله" in comm or "آره" in comm or "اره" in comm:
            internet()
            send_email()
        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")

def map():
    test_net = check_internet_connection()
    if test_net:
        play_audio("E . or. D:\\you model dataset sonds directory\\map.mp3")
        time.sleep(4)
        command = goosh("1")
        base_url = "https://www.google.com/maps/search/"
        address_query = "+".join(command.split())
        full_url = base_url + address_query
        webbrowser.open(full_url)
        play_audio("E . or. D:\\you model dataset sonds directory\\نقشه شما.mp3")
        time.sleep(3)
        play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
        time.sleep(2)
        pas("")
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\تذکر_اینترنت.mp3")
        time.sleep(5)
        comm = goosh("1")
        if "بله" in comm or "آره" in comm or "اره" in comm:
            internet()
            map()

        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")

def maghalle_khan(text) :
    zaban(text)

def wiki_pedia():
    test_net = check_internet_connection()
    if test_net:
        try:
            play_audio("E . or. D:\\you model dataset sonds directory\\سرچ ویکی.mp3")
            time.sleep(2)
            # تغییر زبان به فارسی
            wikipedia.set_lang("fa")
            # دریافت عنوان مقاله مرتبط با کلمه کلیدی از کاربر
            search_term = goosh("0")
            # جستجو در ویکی پدیا
            play_audio(
                "E . or. D:\\you model dataset sonds directory\\درحال ویکی.mp3")
            time.sleep(2)
            page = wikipedia.page(search_term)
            # چاپ عنوان مقاله
            title = page.title
            print(f"عنوان مقاله: {title} \n")
            # چاپ محتوای مقاله
            matn = page.content
            print(f"{matn}\n")
            os.chdir("C:\\Users\\computer\\Desktop")
            with open(f"{title}.txt", "w", encoding="utf-8") as file:
                file.write(f"عنوان : {title}\n\n    {matn}")
            play_audio("E . or. D:\\you model dataset sonds directory\\ذخیره مقاله.mp3")
            time.sleep(3)

            play_audio("E . or. D:\\you model dataset sonds directory\\متن مقاله.mp3")
            time.sleep(2)
            comm = goosh("1")

            if "بله" in comm or "آره" in comm :
                play_audio("E . or. D:\\you model dataset sonds directory\\بسیار خب منتظر باشید.mp3")
                time.sleep(3)
                maghalle_khan(f"{title} ,,؛؛ {matn}")

            else:
                play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
                time.sleep(1)
                play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
                time.sleep(2)




            pas("")
        except:
            play_audio("E . or. D:\\you model dataset sonds directory\\عدم ویکی.mp3")
            time.sleep(2)
            pas("")
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\تذکر_اینترنت.mp3")
        time.sleep(5)
        comm = goosh("1")
        if "بله" in comm or "آره" in comm or "اره" in comm:
            internet()
            wiki_pedia()

        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")

def google():
    test_net = check_internet_connection()
    if test_net:
        try:
            play_audio("E . or. D:\\you model dataset sonds directory\\سرچ.mp3")
            time.sleep(2.5)
            comm = goosh("0")
            goda = comm.split(" ")
            serch_command = ""
            for i in goda :
                serch_command += i + "+"
            serch_command = serch_command[:-1]
            print(serch_command)
            os.system(f"start https://www.google.com/search?q={serch_command}")
            play_audio("E . or. D:\\you model dataset sonds directory\\نتیجه سرچ.mp3")
            time.sleep(2.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2.5)
            pas("")

        except:
            play_audio("E . or. D:\\you model dataset sonds directory\\عدم سرچ.mp3")
            time.sleep(2)
            pas("")
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\تذکر_اینترنت.mp3")
        time.sleep(5)
        comm = goosh("1")
        if "بله" in comm or "آره" in comm or "اره" in comm:
            internet()
            google()

        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")

def Voice_translator():
    pass


def STT2(Lang) :
    fa = ["فارسی",
          "پارسی",
          "پرشین",
          "persian",
          "farsi"]

    en = ["انگلیسی",
          "انگلیش",
          "english",
          "englis",]

    LN = ""
    if Lang in fa :
        play_audio("E . or. D:\\you model dataset sonds directory\\صحبت کنید.mp3")
        LN = 'fa-IR'
    elif Lang in en :
        pyttsx3.speak("so pleas speak")
        LN = "en-US"

    time.sleep(1)

    # try:
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as sours:
        play_audio("E . or. D:\\you model dataset sonds directory\\بیپ2.mp3")
        time.sleep(0.5)
        audio = r.listen(sours)
        command = r.recognize_google(audio, language=f"{LN}")
        print(command + "\n")
        return command

    # except Exception as er:
    #     print(f"{er}\nخطا در اینترنت !!!")
    #     pas("")

def API_TTS2(Text):
    try:
        # model_name = "vits male1 (best)" #"صدای آقا"
        model_name = "vits female (best)" #"صدای خانم"
        # text = str(Text)
        response = requests.post("https://kamtera-persian-tts-coquitts.hf.space/run/predict",json={"data": [str(Text), model_name]}).json()
        data = response["data"]
        url_token = data[0]['name']
        return url_token
    except Exception :
        print("\n" + "مشکل در اتصال یا سرعت کند اینترنت")
def TTS2(lang, Text):
    fa = ["فارسی",
          "پارسی",
          "پرشین",
          "persian",
          "farsi"]
    en = ["انگلیسی",
          "انگلیش",
          "english",
          "englis",]

    Lang = ""
    if lang in en :
        Lang = "en"
    elif lang in fa :
        Lang = "fa"


    if Lang == "fa" :
        download_file(Text)
        change_name_and_run_sond()

    elif Lang == "en" :
        text = Text
        engine = pyttsx3.init()
        # تنظیم جنس صدا
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # صدای زنانه
        engine.setProperty('rate', 180)  # تنظیم سرعت گفتار (اختیاری)
        engine.say(text)
        engine.runAndWait()
def Translatetor(Text, From) :
    print(f">>> From >>> {From}")
    print(f">>> Text >>> {Text}")

    langs = {"فارسی" : "fa", "عربی" : "ar", "english" : "en", "هندی (hindi)" : "in"}
    fa = ["فارسی",
          "پارسی",
          "پرشین",
          "persian",
          "farsi"]

    en = ["انگلیسی",
        "انگلیش",
        "english",
        "englis",]

    from_lang = ""
    to_lang = ""
    if From in fa :
        from_lang = 'fa-IR'
        to_lang = 'en-US'
    elif From in en :
        from_lang = 'en-US'
        to_lang = 'fa-IR'

    print(f">>> from_lang >>> {from_lang}")
    print(f">>> to_lang >>> {to_lang}")

    # تبدیل متن به یک خط با حذف خطوط خالی
    one_line_text = ' '.join(str(Text).splitlines())
    outpute = Translator(f"{to_lang}", f"{from_lang}").translate(f"{one_line_text}")
    print("\n\n" + f"{outpute}")
    return f"\n\n{outpute}"


    if len(str(outpute)) > 500 :
        print("طول متن بیش از 500 کاراکتر است و نمیتوان به زبان مقابل ترجمه کرد")

    else:
        print("\n\n" + f"{outpute}")
        return f"\n\n{outpute}"

def Translator():
    test_net = check_internet_connection()
    if test_net:
        while True :
            play_audio("E . or. D:\\you model dataset sonds directory\\از چه زبانی.mp3")
            time.sleep(1)
            zab = goosh("1")
            langs__ = ["فارسی",
                  "پارسی",
                  "پرشین",
                  "persian",
                  "farsi",
                  "انگلیسی",
                  "انگلیش",
                  "english",
                  "englis",]
            for i in langs__ :
                if i in zab :
                    command = STT2(i)
                    Tr = Translatetor(command, i)
                    TTS2(i, Tr)
                    break
                else:
                    pass
    else:
        play_audio("E . or. D:\\you model dataset sonds directory\\تذکر_اینترنت.mp3")
        time.sleep(5)
        comm = goosh("1")
        if "بله" in comm or "آره" in comm or "اره" in comm:
            internet()
            google()

        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")
################################################
############## توابع کار های سینا آفلاین ########
def connect_to_data_base():
    # con = msc.connect(host="127.0.0.1", user="root", password="12345qwert", database="sina", port=3306)
    con = msc.connect(host="127.0.0.1", user="root", password="12345qwert", database="sina", port=3306)
    return con

def reset_fosh() :
    fosh_ha = connect_to_data_base()
    cur = fosh_ha.cursor()
    cur.execute(f"UPDATE fahashi SET tedade_movaghat = 0 WHERE id = 1")
    fosh_ha.commit()

def nevis():
    text = ""

    play_audio("E . or. D:\\you model dataset sonds directory\\nevisande.mp3")
    time.sleep(2)

    while True :
        command1 = goosh("1")
        if "سینا تمام" not in command1 :
            text += f"{command1}\n"
        elif "سینا تمام" in f"{command1}":
            break


    os.chdir("C:\\Users\\computer\\Desktop")

    play_audio("E . or. D:\\you model dataset sonds directory\\esme_matn.mp3")
    time.sleep(2)
    command2 = goosh("1")

    comm = command2.split(" ")
    command2 = ""
    for i in comm :
        command2 += i + "_"



    os.chdir("C:\\Users\\computer\\Desktop")
    with open(f"{command2}.txt", "w", encoding="utf-8") as file:
        file.write(f"شما گفتید :\n{text}")

    os.system(f"start {command2}.txt")


    play_audio("E . or. D:\\you model dataset sonds directory\\matn_zakhire_shod.mp3")
    time.sleep(4)
    play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
    time.sleep(2)
    pas("")

def photo():
    play_audio("E . or. D:\\you model dataset sonds directory\\amade.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\1.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\2.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\3.mp3")
    # شروع نمایش دوربین
    cap = cv2.VideoCapture(0)
    # خواندن یک فریم از دوربین
    ret, frame = cap.read()
    # بستن دوربین
    cap.release()
    # ذخیره عکس در دسکتاپ
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    photo_path = os.path.join(desktop_path, "captured_photo.jpg")
    cv2.imwrite(photo_path, frame)
    os.chdir("C:\\Users\\computer\\Desktop")
    os.system("start captured_photo.jpg")
    play_audio("E . or. D:\\you model dataset sonds directory\\aks.mp3")
    time.sleep(0.5)
    play_audio("E . or. D:\\you model dataset sonds directory\\aks_gerefte_shod.mp3")
    time.sleep(5)
    play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
    time.sleep(2)
    pas("")

def film():
    play_audio("E . or. D:\\you model dataset sonds directory\\amade.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\1.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\2.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\3.mp3")
    time.sleep(0.5)
    play_audio("E . or. D:\\you model dataset sonds directory\\بیپ2.mp3")
    os.chdir("C:\\Users\\computer\\Desktop")
    def record_video_with_audio():
        # ایجاد یک شیء VideoCapture برای دوربین
        cap = cv2.VideoCapture(0)

        # اندازه فریم‌هایی که گرفته می‌شود را تنظیم کنید
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # تنظیم فرمت ذخیره‌سازی فیلم
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        # ایجاد یک شیء VideoWriter برای ذخیره فیلم
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        out = cv2.VideoWriter(os.path.join(desktop_path, "captured_video.avi"), fourcc, 20.0, (640, 480))

        # تنظیمات ضبط صدا
        audio_format = pyaudio.paInt16
        audio_channels = 2
        audio_rate = 44100
        audio_chunk = 3024

        audio = pyaudio.PyAudio()
        # stream = audio.open(format=audio_format, channels=audio_channels, rate=audio_rate, input=True, frames_per_buffer=audio_chunk)
        stream = audio.open(format=audio_format, channels=audio_channels, rate=44100, input=True,
                            frames_per_buffer=audio_chunk)

        # ذخیره کردن صدا در فایل
        wf = wave.open(os.path.join(desktop_path, "captured_audio.wav"), 'wb')
        wf.setnchannels(audio_channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(audio_rate)

        while True:
            # خواندن یک فریم از دوربین
            ret, frame = cap.read()

            # نوشتن فریم در فیلم
            out.write(frame)

            # ضبط صدا
            audio_data = stream.read(audio_chunk)
            wf.writeframes(audio_data)

            # نمایش تصویر در پنجره
            cv2.imshow('Recording Video', frame)

            # بررسی ورودی کاربر برای قطع فیلم
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # تمیز کردن و انجام تمامی عملیات
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # بستن جریان صدا
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wf.close()
    record_video_with_audio()

    def merge_video_audio(video_file, audio_file, output_file):
        # بارگذاری فایل‌های ویدئو و صوت
        video_clip = VideoFileClip(video_file)
        audio_clip = AudioFileClip(audio_file)

        # ترکیب فیلم و صدا
        video_clip = video_clip.set_audio(audio_clip)

        # ذخیره فیلم جدید
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')


    play_audio("E . or. D:\\you model dataset sonds directory\\درحال_ذخیره.mp3")
    time.sleep(3)

    video_file = "C:\\Users\\computer\\Desktop\\captured_video.avi"
    audio_file = "C:\\Users\\computer\\Desktop\\captured_audio.wav"
    output_file = 'output_video_with_audio.mp4'  # مسیر فایل خروجی

    merge_video_audio(video_file, audio_file, output_file)
    # حذف فایل ویدئویی
    if os.path.exists(video_file):
        os.remove(video_file)
        print(f"{video_file} deleted successfully")
    else:
        print(f"{video_file} does not exist")

    # حذف فایل صوتی
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print(f"{audio_file} deleted successfully")
    else:
        print(f"{audio_file} does not exist")
    play_audio("E . or. D:\\you model dataset sonds directory\\فیلم_ذخیره_شد.mp3")
    time.sleep(4)
    play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
    time.sleep(2)
    os.chdir("C:\\Users\\computer\\Desktop")
    os.system(f"start output_video_with_audio.mp4")
    pas("")

def voic_recorder():
    os.chdir(r"C:\Users\computer\Desktop")
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('ctrl'):
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            break


    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    os.chdir("C:\\Users\\computer\\Desktop")
    os.system(f"start output.wav")



    pas("")

def ayne():
    play_audio("E . or. D:\\you model dataset sonds directory\\بفرما_آینه.mp3")
    # ایجاد یک شیء VideoCapture برای دوربین
    cap = cv2.VideoCapture(0)
    # چک کردن اینکه آیا دوربین با موفقیت باز شده یا نه
    if not cap.isOpened():
        print("دوربین باز نشد. مطمئن شوید که دوربین متصل است.")
    while True:
        # خواندن یک فریم از دوربین
        ret, frame = cap.read()
        # چک کردن اینکه آیا فریم با موفقیت خوانده شده یا نه
        if not ret:
            print("خواندن فریم با مشکل مواجه شد.")
            break
        # نمایش تصویر در پنجره
        cv2.imshow('Camera', frame)
        # انتظار برای فشردن دکمه ESC برای خروج


        if cv2.waitKey(1) & 0xFF == 27:

            break
    # تمیز کردن و انجام تمامی عملیات
    cap.release()
    cv2.destroyAllWindows()
    play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
    time.sleep(2)
    pas("")

def ahang():
    play_audio("E . or. D:\\you model dataset sonds directory\\پخش_آهنگ.mp3")
    time.sleep(1.5)
    command = goosh("1")
    alboms = {"ایرانی" : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\ایرانی",
              "خارجی"  : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\خارجی",
              "بی‌کلام"  : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\بیکلام",
              "بی کلام"  : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\بیکلام",
              "بیکلام"  : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\بیکلام",
              "ترکیبی" : "E:\\موارد دیگر\\فایل های کاری\\پروژه های شخصی\\دستیار سینا\\data\\ahang_haye_sefareshi\فاز\\ترکیبی"
              }

    mod = ["ایرانی", "خارجی", "بی کلام", "بی‌کلام", "بیکلام", "ترکیبی"]
    aa = False
    for i in mod:
        if i in command:
            aa = True
            play_audio("E . or. D:\\you model dataset sonds directory\\قطع_آهنگ.mp3")
            time.sleep(2.5)
            # مسیر دایرکتوری حاوی آهنگ‌ها
            songs_dir = f"{alboms[i]}"
            print(songs_dir)

            # گرفتن لیست فایل‌های موسیقی در دایرکتوری
            songs_list = os.listdir(songs_dir)

            # مرتب کردن لیست آهنگ‌ها بر اساس نام
            songs_list.sort()

            # شروع پخش آهنگ‌ها
            pygame.init()
            pygame.mixer.init()

            for song in songs_list:
                song_path = os.path.join(songs_dir, song)
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()

                # حلقه بازی Pygame برای کنترل پخش آهنگ
                running = True

                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE : # or a_test == False:
                                pygame.mixer.music.stop()
                                running = False


                    baadi = goosh("2")
                    if keyboard.is_pressed('right') or baadi == "بعدی" or baadi == "آهنگ بعدی":
                        running = False
                        time.sleep(0.5)

                    if keyboard.is_pressed('tab') or baadi == "برو بیرون" or baadi == "ولش کن" or baadi == "ولشکن":
                        pygame.mixer.music.stop()
                        play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
                        time.sleep(2)
                        pas("")
                        break
        elif "هیچی" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            break
    if aa == False :
        play_audio("E . or. D:\\you model dataset sonds directory\\نان_آلبوم.mp3")
        time.sleep(3)
        ahang()
    pas("")

def number_to_speech(text_number):
    try:
        adad = int(digits.convert_from_word(f"{text_number}"))
        print(adad)
        return adad
    except Exception :
        return False

def adad_bekhan(adad):
    try:
        def adad_khan(adad) :
            matn_adad = f"{digits.convert_to_word(adad)}"
            print(matn_adad)
            return matn_adad
        def replace_space(text):
            return text.replace(" و ", "و ")
        dict_adad = {"منفی" : "منفیه",
                     "صفر": "0" ,
                     "یک": "1",
                     "دو": "2",
                     "سه": "3",
                     "چهار": "4",
                     "پنج": "5",
                     "شش": "6",
                     "هفت": "7",
                     "هشت": "8",
                     "نه": "9",
                     "ده": "10",
                     "یازده": "11",
                     "دوازده": "12",
                     "سیزده": "13",
                     "چهارده": "14",
                     "پانزده": "15",
                     "شانزده": "16",
                     "هفده": "17",
                     "هجده": "18",
                     "نوزده": "19",
                     "بیست": "20",
                     "بیستو": "20و",
                     "سی": "30",
                     "سیو": "30و",
                     "چهل": "40",
                     "چهلو": "40و",
                     "پنجاه": "50",
                     "پنجاهو": "50و",
                     "شصت": "60",
                     "شصتو": "60و",
                     "هفتاد": "70",
                     "هفتادو": "70و",
                     "هشتاد": "80",
                     "هشتادو": "80و",
                     "نود": "90",
                     "نودو": "90و",
                     "صد": "100",
                     "صدو": "100و",
                     "دویست": "200",
                     "دویستو": "200و",
                     "سیصد": "300",
                     "سیصدو": "300و",
                     "چهارصد": "400",
                     "چهارصدو": "400و",
                     "پانصد": "500",
                     "پانصدو": "500و",
                     "ششصد": "600",
                     "ششصدو": "600و",
                     "هفتصد": "700",
                     "هفتصدو": "700و",
                     "هشتصد": "800",
                     "هشتصدو": "800و",
                     "نهصد": "900",
                     "نهصدو": "900و",
                     "هزار": "1000",
                     "هزارو": "1000و",
                     "میلیون": "1000000",
                     "میلیونو": "1000000و",
                     "میلیارد": "1000000000",
                     "میلیاردو": "1000000000و",
                     "بیلیون" : "1000000000000",
                     "بیلیونو" : "1000000000000و",
                     "بیلیارد": "1000000000000000",
                     "بیلیاردو": "1000000000000000و"
                     }
        output_text = replace_space(adad_khan(adad))
        print(output_text)
        goda = f"{output_text}".split(" ")
        for i in goda :
            print(i)
            play_audio(f"E . or. D:\\you model dataset sonds directory\\{dict_adad[i]}.mp3")
            if i == "میلیاردو" or i == "هزارو" or i == "میلیونو" or i == "صدو" or i == "تیلیونو" or i == "تیلیاردو" or i == "بیلیونو" or i == "بیلیاردو":
                #
                time.sleep(0.89)
            else:
                #
                time.sleep(0.69)
    except Exception :
        play_audio(f"E . or. D:\\you model dataset sonds directory\\ارور عدد.mp3")
        time.sleep(7)
        pas("")

def saat_gooya():
    saat = int(datetime.datetime.now().time().hour)
    daghighe = int(datetime.datetime.now().time().minute)
    saniye = int(datetime.datetime.now().time().second)
    if saat > 12 :
        saat -= 12
    play_audio("E . or. D:\\you model dataset sonds directory\\ساعت.mp3")
    time.sleep(0.8)
    adad_bekhan(saat)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\و.mp3")
    time.sleep(0.5)
    adad_bekhan(daghighe)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\دقیقه.mp3")
    time.sleep(0.6)
    play_audio("E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.6)
    pas("")

def emrooz() :
    rooz_haye_hafte_shamsi = {"0": "2شنبه", "1": "3شنبه", "2": "4شنبه", "3": "5شنبه", "4": "جمعه",
                              "5": "شنبه", "6": "1شنبه"}
    soti = rooz_haye_hafte_shamsi[f'{datetime.datetime.today().weekday()}']
    play_audio("E . or. D:\\you model dataset sonds directory\\امروز.mp3")
    time.sleep(0.7)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{soti}.mp3")
    time.sleep(0.8)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.4)
    pas("")

def tarikh():
    shamsi = {1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر",
              5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان", 9: "آذر",
              10: "دی", 11: "بهمن", 12: "اسفند"
              }

    shamsi_emrooz = JalaliDateTime.now()
    print(f"{shamsi_emrooz.day} اُم_{shamsi[int(shamsi_emrooz.month)]}_{shamsi_emrooz.year}")

    play_audio("E . or. D:\\you model dataset sonds directory\\امروز.mp3")
    time.sleep(0.6)
    adad_bekhan(shamsi_emrooz.day)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\امه.mp3")
    time.sleep(0.5)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{shamsi[shamsi_emrooz.month]}.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ماهه.mp3")
    time.sleep(0.9)
    adad_bekhan(shamsi_emrooz.year)
    time.sleep(0.4)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.6)
    pas("")


    # print(f"{shamsi_emrooz.day} اُم_{shamsi[int(shamsi_emrooz.month)]} ماه_{shamsi_emrooz.year}")
    # print(f"{milada_emrooz.day} اُم_{miladi[int(milada_emrooz.month)]}_{milada_emrooz.year}")
    # print(f"{ghamari_emrooz.day} اُم_{ghamari[int(ghamari_emrooz.month)]}_{ghamari_emrooz.year}")
    # adad_hafte = int(datetime.datetime.today().weekday())
    # print(f" امروز {rooz_haye_hafte_shamsi[f'{datetime.datetime.today().weekday()}']}  {shamsi_emrooz.year}/{int(shamsi_emrooz.month)}/{shamsi_emrooz.day}")

def tarikh_kamel():
    shamsi = {1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر",
              5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان", 9: "آذر",
              10: "دی", 11: "بهمن", 12: "اسفند"
              }
    rooz_haye_hafte_shamsi = {"0": "2شنبه", "1": "3شنبه", "2": "4شنبه", "3": "5شنبه", "4": "جمعه",
                              "5": "شنبه", "6": "1شنبه"}
    shamsi_emrooz = JalaliDateTime.now()
    soti = rooz_haye_hafte_shamsi[f'{datetime.datetime.today().weekday()}']
    play_audio("E . or. D:\\you model dataset sonds directory\\امروز.mp3")
    time.sleep(0.7)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{soti}.mp3")
    time.sleep(0.8)
    adad_bekhan(shamsi_emrooz.day)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\امه.mp3")
    time.sleep(0.5)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{shamsi[shamsi_emrooz.month]}.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ماهه.mp3")
    time.sleep(0.9)
    adad_bekhan(shamsi_emrooz.year)
    time.sleep(0.4)
    saat = int(datetime.datetime.now().time().hour)
    daghighe = int(datetime.datetime.now().time().minute)
    if saat > 12 :
        saat -= 12
    play_audio("E . or. D:\\you model dataset sonds directory\\ساعت.mp3")
    time.sleep(0.8)
    adad_bekhan(saat)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\و.mp3")
    time.sleep(0.5)
    adad_bekhan(daghighe)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\دقیقه.mp3")
    time.sleep(0.6)
    play_audio("E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.6)

    pas("")


    # print(f"{shamsi_emrooz.day} اُم_{shamsi[int(shamsi_emrooz.month)]} ماه_{shamsi_emrooz.year}")
    # print(f"{milada_emrooz.day} اُم_{miladi[int(milada_emrooz.month)]}_{milada_emrooz.year}")
    # print(f"{ghamari_emrooz.day} اُم_{ghamari[int(ghamari_emrooz.month)]}_{ghamari_emrooz.year}")
    # adad_hafte = int(datetime.datetime.today().weekday())
    # print(f" امروز {rooz_haye_hafte_shamsi[f'{datetime.datetime.today().weekday()}']}  {shamsi_emrooz.year}/{int(shamsi_emrooz.month)}/{shamsi_emrooz.day}")

def tarikh_gh():
    ghamari = {1: "محرم (1)", 2: "صفر (2)", 3: "ربیع الاول (3)", 4: "ربیع الثانی (4)",
               5: "جمادی الاول (5)", 6: "جمادی الآخر (6)", 7: "رجب (7)", 8: "شعبان (8)", 9: "رمضان (9)",
               10: "شوال (10)", 11: "ذی القعده (11)", 12: "ذی الحجه (12)"}
    ghamari_emrooz = Hijri.today()
    print(f"{ghamari_emrooz.day} اُم_{ghamari[int(ghamari_emrooz.month)]}_{ghamari_emrooz.year}")

    play_audio("E . or. D:\\you model dataset sonds directory\\امروز.mp3")
    time.sleep(0.6)
    adad_bekhan(ghamari_emrooz.day)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\امه.mp3")
    time.sleep(0.5)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ماهه.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{ghamari[ghamari_emrooz.month]}.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ساله.mp3")
    time.sleep(0.9)
    adad_bekhan(ghamari_emrooz.year)
    time.sleep(0.4)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.6)
    pas("")

def tarikh_ml():
    miladi = {1: "january(ژانویه)", 2: "february(فوریه)", 3: "March(مارس)", 4: "April(آوریل)", 5: "May(می)",
              6: "June(ژوئن)", 7: "July(ژولای)", 8: "August(آگوست)", 9: "September(سپتامبر)", 10: "October(اکتبر)",
              11: "November(نوامبر)", 12: "December(دسامبر)"}
    milada_emrooz = datetime.datetime.today()
    print(f"{milada_emrooz.day} اُم_{miladi[int(milada_emrooz.month)]}_{milada_emrooz.year}")

    play_audio("E . or. D:\\you model dataset sonds directory\\امروز.mp3")
    time.sleep(0.6)
    adad_bekhan(milada_emrooz.day)
    time.sleep(0.1)
    play_audio("E . or. D:\\you model dataset sonds directory\\امه.mp3")
    time.sleep(0.5)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ماهه.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\{miladi[milada_emrooz.month]}.mp3")
    time.sleep(0.9)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\ساله.mp3")
    time.sleep(0.9)
    adad_bekhan(milada_emrooz.year)
    time.sleep(0.4)
    play_audio(f"E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(0.6)
    pas("")

def App_runer():
    play_audio("E . or. D:\\you model dataset sonds directory\\کدام_نرم_افزار.mp3")
    time.sleep(1)
    App_Dict = {
                "ویرایش فیلم": "Adobe_After_Effe_ts_2020.lnk",
                "فتوشاپ": "Adobe_Photoshop2020.lnk",
                "رباتیک": "Arduino_IDE.lnk",
                "ماشین حساب": "Calculator.lnk",
                "ساخت فیلم": "Camtasia_2019.lnk",
                "ترمینال": "CMD.lnk",
                "دانلود منیجر": "Download_Manager.lnk",
                "مرورگر": "Firefox.lnk",
                "میکث صدا": "FL_Studio_20.lnk",
                "ایزوتوپ هشت": "iZotope_RX8_Audio_Editor.lnk",
                "متا": "mmaaiinn.lnk",
                "ترمینال دو": "MSYS2.lnk",
                "دیتا بیس": "MySQL_Workbench_8.0_CE.lnk",
                "ویرچوال": "Oracle_VM_VirtualBox.lnk",
                "نقشی": "Paint.lnk",
                "فایل": "PC.lnk",
                "طراحی مدار": "Proteus_8_Professional.lnk",
                "فیلتر شکن": "psiphon3.exe",
                "اسکایپ": "Skype.lnk",
                "محل کار": "Visual_Studio_Code.lnk",
                "طراحی ویندوز": "designer_for_windows.ui",
                "مرورگر دو": "Google_Chrome.lnk",
                "محل کارم": "PyCharm_2023.2.1.lnk",}

    coom = goosh("1")
    os.chdir(r"C:\Users\computer\Desktop\App_List")
    a = False
    for i in App_Dict.keys():
        if i in coom :
            play_audio("E . or. D:\\you model dataset sonds directory\\درحال_اجرای_نرم_افزار.mp3")
            time.sleep(3)
            os.system(f'start {App_Dict[i]}')
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            a = True
            pas("")
        elif "هیچی" in coom :
            play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
            time.sleep(0.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2)
            pas("")
    if a == False :
        play_audio("E . or. D:\\you model dataset sonds directory\\نرم_افزار_نیست.mp3")
        time.sleep(4)
        App_runer()

def tas():
    play_audio("E . or. D:\\you model dataset sonds directory\\تاس شما عدد.mp3")
    time.sleep(1.5)
    adad_bekhan(random.randrange(1, 7))
    play_audio("E . or. D:\\you model dataset sonds directory\\آورد.mp3")
    time.sleep(0.8)
    pas("")

def seke():
    play_audio("E . or. D:\\you model dataset sonds directory\\سکه_ی_شما.mp3")
    time.sleep(1.5)
    roo = random.randrange(0, 2)
    if roo == 0 :
        play_audio("E . or. D:\\you model dataset sonds directory\\خط.mp3")
        time.sleep(0.5)
    elif roo == 1:
        play_audio("E . or. D:\\you model dataset sonds directory\\شیر.mp3")
        time.sleep(0.5)
    play_audio("E . or. D:\\you model dataset sonds directory\\آمد.mp3")
    time.sleep(0.5)

    pas("")

def shut_down():
    while True :
        play_audio("E . or. D:\\you model dataset sonds directory\\چند_ثانیه_دیگه_سیستم_خواموش.mp3")
        time.sleep(2.5)
        comm = goosh("0")
        matn = number_to_speech(comm)
        if matn != False :
            while True:
                play_audio("E . or. D:\\you model dataset sonds directory\\سیستم شما تا.mp3")
                time.sleep(1)
                adad_bekhan(matn)
                play_audio("E . or. D:\\you model dataset sonds directory\\ثانیه دیگر_خواموش میشود.mp3")
                time.sleep(2.5)
                Q = goosh("0")
                if "بله" in Q :
                    play_audio("E . or. D:\\you model dataset sonds directory\\سیستم درحال خواموشی.mp3")
                    time.sleep(2.5)
                    for i in range(1, int(matn) + 1) :
                        adad_bekhan(i)
                        time.sleep(1)
                    os.system(f"shutdown /s /t {matn}")
                    break
                elif "خیر" in Q :
                    play_audio("E . or. D:\\you model dataset sonds directory\\یاشه.mp3")
                    time.sleep(0.9)
                    pas("")
                else:
                    play_audio("E . or. D:\\you model dataset sonds directory\\بله یا خیر.mp3")
                    time.sleep(2)
        else:
            play_audio("E . or. D:\\you model dataset sonds directory\\عدد نامفهوم.mp3")
            time.sleep(2)

def sleep():
    matn = 10
    os.system(f"timeout /t {matn} && rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    # while True :
    #     print("چند ثانیه دیگر خواموش بشه؟ :: ")
    #     comm = goosh("0")
    #     matn = number_to_speech(comm)
    #     if matn != False :
    #         while True:
    #             print(f"سیستم تا {matn} ثانیه دیگر خواموش میشود . . . ")
    #             print("آیا مطمئن هستید؟ ::: بله/خیر ::: ")
    #             Q = goosh("0")
    #
    #             if "بله" in Q :
    #                 os.system(f"timeout /t {matn} && rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    #                 break
    #             elif "خیر" in Q :
    #                 pas("")
    #             else:
    #                 print("فقط بله یا خیر")
    #
    #     else:
    #         print("عدد نامفهوم!!!!")
    #
    #     break

def mohasebe() :
    play_audio("E . or. D:\\you model dataset sonds directory\\معادله را بگویید.mp3")
    time.sleep(2.5)
    command = goosh(0)
    try:
        # دیکشنری ها
        amal = {"علاوه": "+", "اضافه": "+", "پلاس": "+", "منهای": "-", "تفریق": "-", "ضرب": "*", "تقسیم": "/", "توان": "**","جزر": "0.0"}
        horoofe_ezafe = ["بر", "به", "در"]
        alaem = ["+", "-", "*", "/", "**"]
        alaemhh = ["علاوه", "اضافه", "پلاس", "منهای", "تفریق", "ضرب", "تقسیم", "توان", "جزر"]

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # ورودی
        voroodi0 = str(command)

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # جدا کردن کلمات در لیت جدا
        goda2 = voroodi0.split(" ")

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # حذف حروف اضافه در معادله متنی
        for i in goda2:
            if i in horoofe_ezafe:
                goda2.pop(goda2.index(i))

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # تفکیک اعداد از علائم ریاضی
        goda = []
        matn = ""
        for i in goda2:
            if i in alaemhh:
                goda.append(matn[0:-1])
                goda.append(i)
                matn = ""
            else:
                matn += i + " "
        goda.append(matn[0:-1])
        for i in goda:
            if "" == i or " " == i:
                goda.pop(goda.index(i))

        print(f"              goda           {goda}")

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        for i in goda:
            if i == "هزار":
                goda[goda.index(i)] = "یک هزار"

        # ////////////////////////////////////////
        # ////////////////////////////////////////


        for i in goda:
            if i in amal.keys():
                goda[goda.index(i)] = amal[i]

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # حرف به عدد
        ad = []
        # index = 0
        for i in goda:
            if "0.0" == i or 0.0 == i:
                ad.append(i)

            if i not in alaem:
                adad = digits.convert_from_word(i)
                ad.append(adad)

            elif i in alaem:
                #
                ad.append(i)

        print(f"              ad        {ad}")

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        for i in ad:
            if i == "0.0" or i == 0.0:
                ad.pop(ad.index(i) + 1)
                index = ad.index(i)
                gazr = math.sqrt(int(ad[index + 1]))
                print(gazr)
                ad[index + 1] = gazr
                ad.pop(index)

        print(f"              ad        {ad}")

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # جفت کردن المان های یک لیست در یک رشته
        tabdil_yafte = ""
        for i in ad:
            #
            tabdil_yafte += str(i)

        print(tabdil_yafte)

        # ////////////////////////////////////////
        # ////////////////////////////////////////

        # محاسبه معادله
        mohasebe_moadele = int(eval(tabdil_yafte))

        play_audio("E . or. D:\\you model dataset sonds directory\\جواب معادله.mp3")
        time.sleep(2)

        adad_bekhan(mohasebe_moadele)
        time.sleep(5)
        print(mohasebe_moadele)

        play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
        time.sleep(2)
        pas("")




    except :
        play_audio("E . or. D:\\you model dataset sonds directory\\مشکل در حل معادله.mp3")
        time.sleep(6)
        mohasebe()

def abgad() :
    abgads = ["کبیر", "صغیر", "تعدیل", "وسط", "معکوس", "وسیط", "ابجدی", "وضعی", "مغربی"]
    ezafi = ["ابجد" , "اسم" , "اسامی" , "های" , "ها" , "حساب" , "کبیر" , "صغیر" , "چنده" , "محاسبه", "حساب", "کن", "بگو", "چقدر", "این", "نام","رو","را","ابجدش", "و", "کن", "بکن", "چقدره" ,"چقدر" , "چه", "قدر", "قدره", "چقدره؟" ,"چقدر؟", "قدر؟", "قدره؟","ابجد","اسم","بذار", "حساب", "یا", "با", "به", "استفاده", "از", "توسط", "این", "اسامی", "اسم", "ها", "رو", "را", "میتونی", "لطفا", "ابجد", " و ", "و" ,"کن", "بکن", "بنما", "درست"]
    play_audio("E . or. D:\\you model dataset sonds directory\\اسامی ابجد.mp3")
    abgad = {}


    time.sleep(4)
    asami = goosh("0")
    tak_esm = asami.split(" ")
    noe_abgad = ""
    for i in abgads :
        if i in tak_esm :
            noe_abgad = i
            break

    if noe_abgad == "" :
        while True :
            play_audio("E . or. D:\\you model dataset sonds directory\\چه نوع ابجد.mp3")
            time.sleep(1.5)
            comm = goosh("0")
            for i in abgads :
                if i in comm:
                    noe_abgad = i
                    break

            if "هیچی" in comm or "ولش کن" in comm :
                play_audio("E . or. D:\\you model dataset sonds directory\\باشه.mp3")
                time.sleep(0.5)
                play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
                time.sleep(2)
                pas("")



            if  noe_abgad != "" :
                #
                break

            elif noe_abgad == "" :
                play_audio("E . or. D:\\you model dataset sonds directory\\چنین ابجدی در داده های ما مُجود نیست.mp3")
                time.sleep(4)

    if noe_abgad == "کبیر":
        abgad = {
            "ء": 0, "ئ": 10, "ا": 1, "آ": 1, "ب": 2, "ج": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ی": 10,
            "ک": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70,
            "ف": 80, "ص": 90, "ق": 100, "ر": 200, "ش": 300, "ت": 400,
            "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000, " ": 0,
            "گ": 20, "چ": 3, "پ": 2, "ژ": 7}
    elif noe_abgad == "صغیر":
        abgad = {
            "ا": 1, "آ": 1, "ب": 2, "ج": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ی": 10, "ئ": 10,
            "ک": 8, "ل": 6, "م": 4, "ن": 2, "س": 0, "ع": 10,
            "ف": 8, "ص": 6, "ق": 4, "ر": 8, "ش": 0, "ت": 4,
            "ث": 8, "خ": 0, "ذ": 4, "ض": 8, "ظ": 0, "غ": 4, " ": 0,
            "گ": 8, "چ": 3, "پ": 2, "ژ": 7
        }
    elif noe_abgad == "تعدیل":
        abgad = {
            "ا": 210, "آ": 210, "ب": 420, "ج": 630, "د": 840,
            "ه": 1050, "و": 1260, "ز": 1470, "ح": 1680, "ط": 1890, "ی": 2100, "ئ": 2100,
            "ک": 2310, "ل": 2520, "م": 2730, "ن": 2940, "س": 3150, "ع": 3360,
            "ف": 3570, "ص": 3780, "ق": 3990, "ر": 4200, "ش": 4410, "ت": 4620,
            "ث": 4830, "خ": 5040, "ذ": 5250, "ض": 5460, "ظ": 5670, "غ": 5880, " ": 0,
            "گ": 2310, "چ": 630, "پ": 420, "ژ": 1470}
    elif noe_abgad == "وسط":
        abgad = {
            "ا": 1, "آ": 1, "ب": 2, "پ": 2, "ج": 3, "چ": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ژ": 7, "ح": 8, "ط": 9, "ی": 10, "ئ": 10,
            "ک": 11, "گ": 11, "ل": 12, "م": 13, "ن": 14, "س": 5, "ع": 6,
            "ف": 7, "ص": 8, "ق": 9, "ر": 12, "ش": 2, "ت": 2,
            "ث": 14, "خ": 20, "ذ": 20, "ض": 29, "ظ": 27, "غ": 28, " ": 0
        }
    elif noe_abgad == "معکوس":
        abgad = {
            "ا": 1000, "آ": 1000, "ب": 900, "پ": 900, "ج": 800, "چ": 800, "د": 700,
            "ه": 600, "و": 500, "ز": 400, "ژ": 400, "ح": 300, "ط": 200, "ی": 100, "ئ": 100,
            "ک": 90, "گ": 90, "ل": 80, "م": 70, "ن": 60, "س": 50, "ع": 40,
            "ف": 30, "ص": 20, "ق": 10, "ر": 9, "ش": 8, "ت": 7,
            "ث": 6, "خ": 5, "ذ": 4, "ض": 3, "ظ": 2, "غ": 1, " ": 0}
    elif noe_abgad == "وسیط":
        abgad = {
            "ا": 1, "آ": 1, "ب": 2, "پ": 2, "ج": 3, "چ": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ژ": 7, "ح": 1, "ط": 9, "ی": 10, "ئ": 10,
            "ک": 8, "گ": 8, "ل": 6, "م": 4, "ن": 2, "س": 0, "ع": 10,
            "ف": 8, "ص": 6, "ق": 4, "ر": 8, "ش": 0, "ت": 4,
            "ث": 8, "خ": 0, "ذ": 4, "ض": 8, "ظ": 0, "غ": 4, " ": 0
        }
    elif noe_abgad == "ابجدی":
        abgad = {
            "ا": 8, "آ": 8, "ب": 2, "پ": 2, "ج": 3, "چ": 3, "د": 4,
            "ه": 5, "و": 4, "ز": 7, "ژ": 7, "ح": 2, "ط": 3, "ی": 4, "ئ": 10,
            "ک": 5, "گ": 5, "ل": 4, "م": 7, "ن": 3, "س": 4, "ع": 5,
            "ف": 4, "ص": 7, "ق": 4, "ر": 5, "ش": 4, "ت": 7,
            "ث": 5, "خ": 4, "ذ": 7, "ض": 4, "ظ": 7, "غ": 7, " ": 0
        }
    elif noe_abgad == "وضعی":
        abgad = {
            "ا": 1, "آ": 1, "ب": 2, "پ": 2, "ج": 3, "چ": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ژ": 7, "ح": 8, "ط": 9, "ی": 10, "ئ": 10,
            "ک": 11, "گ": 11, "ل": 12, "م": 13, "ن": 14, "س": 15, "ع": 16,
            "ف": 17, "ص": 18, "ق": 19, "ر": 20, "ش": 21, "ت": 22,
            "ث": 23, "خ": 24, "ذ": 25, "ض": 26, "ظ": 27, "غ": 28, " ": 0
        }
    elif noe_abgad == "مغربی":
        abgad = {
            "ا": 1, "آ": 1, "ب": 2, "پ": 2, "ج": 3, "چ": 3, "د": 4,
            "ه": 5, "و": 6, "ز": 7, "ژ": 7, "ح": 8, "ط": 9, "ی": 10, "ئ": 10,
            "ک": 20, "گ": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70,
            "ف": 80, "ص": 90, "ق": 100, "ر": 200, "ش": 300, "ت": 400,
            "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000, " ": 0
        }

    abgad["گ"] = 0
    abgad["چ"] = 0
    abgad["پ"] = 0
    abgad["ژ"] = 0
    new_words = []

    for i in tak_esm :
        if i in abgads :
            tak_esm.pop(tak_esm.index(i))
    for item in tak_esm:
        #
        new_words.append(item)
    for item2 in new_words:
        if item2 in ezafi:
            new_words.remove(item2)
    for item3 in new_words:
        if item3 in ezafi:
            new_words.remove(item3)
    for item4 in new_words:
        if item4 in ezafi:
            new_words.remove(item4)
    for item5 in new_words:
        if item5 in ezafi:
            new_words.remove(item5)
    print(tak_esm)
    thing = ""
    for item6 in new_words:
        #
        thing = thing + item6 + " "
    print(thing)
    gam = 0
    for harf in str(thing):
        #
        gam += int(abgad.get(harf, 0))
    abgad_nahaee = int(gam)
    print(abgad_nahaee)
    play_audio("E . or. D:\\you model dataset sonds directory\\جمع اسم.mp3")
    time.sleep(5)
    play_audio("E . or. D:\\you model dataset sonds directory\\عدد ابجد.mp3")
    time.sleep(1)
    adad_bekhan(abgad_nahaee)
    play_audio("E . or. D:\\you model dataset sonds directory\\میباشد.mp3")
    time.sleep(1)
    play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
    time.sleep(2)
    pas("")

################################################
######## هوشیاری و فراخوان های توابع سینا ######
def pas(sina):
    ################################################
    while True :
        ################################################
        if sina == "":
            #
            command = goosh("0")
        else:
            #
            command = sina
        ################################################################################################
        ################################################################################################
        ################################################################################################
        hatman_man = ["چشم", "حتما", "باشه", "باش", "خیلی خوب", "خیله خوب", "ببینم چی میشه"]
        ghorboon_sadaghe = ["سینا دمت گرم", "سینا مرسی", "سینا ممنون", "سینا ایول", "سینا دستت درد نکنه", "سینا خیلی ممنونم", "سینا سپاس", "سینا سپاس گزارم"]
        khamoosh = ["می تونی بری", "لطفا برو", "لطفا خاموش", "خداحافظ", "خدا حافظ", "بایبای", "بای بای"]
        salam_aleyk = ["سلام", "دورود", "چطوری", "سینا سلام", "سینا دورود", "سلام سینا", "دورود سینا"]
        fohsh_list = ["کصافت", "اشغال", "آشغال","ازگل","نفهم", "بی شعور", "بی‌شرف", "خر نفهم", "الاغ خر", "بی شرف", "حرومزاده", "حرامزاده", "بیناموس", "بی ناموس", "کس", "کص", "کون", "جو جو", "جوجو", "ممه", "جنده", "کصه", "کسه", "حیف نون", "احمق", "خنگ", "کودن", "به درد نخور", "شل مغز", "شول مغز", "گایید", "گاییدم", "گائید", "گائیدم", "دیوث", "کیر", "دودول"]
        eshgh_list = ["من بهت علاقه مند شدم", "من عاشقت شدم", "با من ازدواج کن", "با من ازدواج میکنی", "من بهت علاقه مند شدم", "شوهرم شو", "زنم شو", "میخوام باهات تا ابد باشم", "میخوام باهات بخوابم", "با من رل میزنی", "باهم رابطه برقرار کن", "در رابطه باشیم", "رابطه ما عالیه"]
        tanafor_list = ["ازت متنفرم", "ازت بیزارم", "نمیخوام ببینمت", "برو گم شو", "برو گمشو", "گورت رو گم کن", "گورتو گم کن", "گورت را گم کن", "برو نبینمت", "خیلی بدی", "تو خیلی بدی", "روت عقده دارم", "باهات حال نمیکنم", "باهات حال نکردم", "باهات حال نکرد", "خیلی مزخرفی", "مزخرفی"]
        ################################################################################################
        ################################################################################################
        ################################################################################################
        mashin_abgadi = ["ابجد و حساب کن", "محاسبه ابجد", "ابجد اسم رو حساب کن", "ابجد اسم", "ماشین حساب ابجدی", "ابجد کبیر", "ابجد صغیر", "ابجد تعدیل"]
        email_list = ["ایمیل بده", "ایمیل بفرست", "جیمیل بده", "جیمیل بفرست", "پیام بده", "پیام بفرست", "ایمیل بده", "جیمیل بده", "پیام بده", "ایمیل ارسال کن", "جیمیل ارسال کن", "پیام ارسال کن"]
        matn_nevis_list = ["برایم بنویس", "برام بنویس", "برایم یاداشت کن",  "برام یاداشت کن", "چیزی که میگم رو بنویس", "یه چیزی میگم بنویس", "یک چیزی میگم بنویس", "میگم بنویس", "بنویس برام"]
        map_lst = ["نقشه رو باز کن", "مپ رو فعال کن", "جی پی اس را باز کن", "نقشه را باز کن", "مپ را فعال کن", "مکان نما فعال"]
        aks_list = ["دوربین آماده", "عکس بگیر", "سلفی بگیر", "تصویر بردار", "ازم عکس بگیر"]
        ayne_list = ["آینه", "آیئنه", "آیینه", "خودمو ببینم", "منو ببین", "آینه رو باز کن"]
        film_list = ["فیلم آماده", "فیلم بگیر", "ویدیو بگیر", "فیلم بردار", "ازم فیلم بگیر"]
        ahang_list = ["پخش آهنگ", "آهنگ پخش کن", "آهنگ بزار", "آهنگ محبوبم", "موزیک بزار", "موزیک پخش کن", "آلبوم های موسیقی", ]
        saat_list = ["ساعت چنده", "ساعت رو بگو", "ساعت را بگو", "زمان الان", "زمان را بگو", "زمان رو بگو", "زمان الان", "تایم الان", "ساعت چند است"]
        emrooz_list = ["امروز چتد شنبه است", "امروز چتد شنبه هست", "امروز چه روزیه", "امروز چه روزی هست", "نام امروز", "چند شنبه است", "چند شنبه هست", "چند شنبست", "امروز چندشنبه است"]
        tarikh_emrooz_list = ["امروز چندامه", "امروز چندمه", "امروز چند امه", "امروز چندم است", "تاریخ امروز", "تقویم امروز", "تاریخ الان", "تقویم الان", "چدمه ماه", "چند امه ماه", "امروز چندم","چندامه ماه"]
        tarikh_emrooz_gh_list = ["امروز چندامه عربی", "امروز چندمه عربی", "امروز چند امه عربی", "امروز چندم عربی است", "تاریخ امروز عربی", "تقویم امروز عربی", "تاریخ الان عربی", "تقویم الان عربی", "چدمه ماه عربی", "چند امه ماه عربی", "امروز چندم عربی","چندامه ماه عربی"]
        tarikh_emrooz_ml_list = ["امروز چندامه میلادی", "امروز چندمه میلادی", "امروز چند امه میلادی", "امروز چندم میلادی است", "تاریخ امروز میلادی", "تقویم امروز میلادی", "تاریخ الان میلادی", "تقویم الان میلادی", "چدمه ماه میلادی", "چند امه ماه میلادی", "امروز چندم میلادی","چندامه ماه میلادی"]
        tarikh_kamel_emrooz_list = ["امروز رو بگو", "تاریخ و زمان امروز", "تاریخ و زمان", "روز و ساعت", "زمان و تاریخ", "تقویم و تایم", "زمان کامل امروز", "زمان دقیق الان", "هفته و تاریخ و زمان", "مشخصات امروز", "امروزو کامل بگو","امروز رو کامل بگو","امروز را کامل بگو"]
        app_runner_list = ["اجرا کن", "باز کن", "فعال کن", "بالا بیار", "نرم افزار رو فعال کن", "نرم افزار رو باز کن", "نرم افزار را باز کن", "نرم افزار را اجرا کن", "نرم افزار رو اجرا کن", "نرم افزار رو ران کن"]
        voice_recorder_list = ["صدا مو ضیط کنه", "صدامو ضیط کنه", "رکورد صدا", "صدای من رو ضبط کن", "صدای من را ضبط کن", "ضبط صدا", "ضبطصدا"]
        adad_gooya_list = ["این عدد رو بخون", "این چه عددی هست", "این چه عددی است", "این عدد را بخوان", "عدد بخوان", "عدد بخون", "این چنده", "عدد خوان", "عدد خون"]
        tas_list = ["تاس بنداز", "تاس پرتاپ کن", "تاس بزن", "پرتاپ تاس", "عدد تاس"]
        seke_list = ["سکه بنداز", "سکه پرتاپ کن", "سکه بزن", "پرتاپ سکه", "روی سکه", "شیر یا خط بنداز", "بازی شیر یا خط", "شیر خط", "شیر یا خط"]
        khamoosh_list = ["سیستم رو خاموش", "سیستم را خاموش", "کامپیوتر رو خاموش", "کامپیوتر را خاموش", "لپ تاپ رو خاموش", "لپ تاپ را خاموش", "رایانه رو خاموش", "رایانه را خاموش", "خاموشی سیستم"]
        sleep_list = ["حالت خواب", "سیستم رو بخوابون", "حالت اسلیپ", "رایانه در حالت خواب", "رایانه در حالت اسلیپ", "سیستم رو بخوابون", "حالت خواب فعال"]
        check_internet_list = ["ببین اینترنت وصله", "ببین اینترنت وصل", "چک کردن اتصال اینترنت", "ببین به اینترنت متصله", "آیا سیستم به اینترنت متصله", "ببین به اینترنت وصلیم", "میشه رفت توی اینترنت", "میشه رفت تو اینترنت"]
        connect_to_internet_list = ["به اینترنت وصل شو", "اتصال به اینترنت", "به اینترنت متصل شو", "به اینترنت وصل بشو", "به اینترنت متصل بشو", "برقراری به اینترنت", "برقرار کردن اتصال به اینترنت", "اینترنت رو وصل کن", "اینترنت را وصل کن"]
        wiki_list = ["سرچ در ویکی‌پدیا", "برای یک مقاله پیدا کن", "جستجوی مقاله", "جستجو در ویکی‌پدیا", "در ویکی‌پدیا بگرد", "در ویکی پدیا بگردید", "در ویکی پدیا بگیرد"]
        google_list = ["سرچ در گوگل", "در گوگل جستجو کن", "در گوگل سرچ کن", "جستجو در گوگل", "در گوگل بگرد", "در گوگل بگردید", "سینا در گوگل بگیرد", "سینا درگوگل بگیرد"]
        hesab_list = ["ماشین حساب", "برام حساب کن", "برای حساب کن", "ماشین حساب کن", "محاسبه کن", "ضرب کن", "جمع کن", "تفریق کن", "تقسیم کن", "حساب و کتاب"]
        Translate = ["ترجمه کن", "ترنسلیت کن", "به انگلیسی", "به فارسی"]
        ################################################################################################
        ################################################################################################
        ################################################################################################


        ################################################
        if any(word in command for word in salam_aleyk) :
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari2.mp3")
            time.sleep(2)
        ################################################
        elif any(word in command for word in Translate) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            Translator()
        ################################################
        elif "سینا خدا حافظ" in command or "سینا خداحافظ" in command or any(word in command for word in khamoosh) and "سینا" in command:
            play_audio("E . or. D:\\you model dataset sonds directory\\خدا_حافظ.mp3")
            time.sleep(4)
            exit()
        ################################################
        elif any(word in command for word in hatman_man) :
            play_audio("E . or. D:\\you model dataset sonds directory\\mamnon.mp3")
            time.sleep(1)
        ################################################
        elif command == "سینا":
            play_audio("E . or. D:\\you model dataset sonds directory\\salam2.mp3")
            time.sleep(1)
            command = goosh("1") + "سینا"
            pas(command)
        ################################################
        elif any(word in command for word in email_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
        ################################################
            time.sleep(2.5)
            send_email()
        ################################################
        elif any(word in command for word in matn_nevis_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            nevis()
        ################################################
        elif any(word in command for word in eshgh_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            nevis()
        ################################################
        elif any(word in command for word in tanafor_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            nevis()
        ################################################
        ################################################
        elif any(word in command for word in mashin_abgadi) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            abgad()
        ################################################
        ################################################
        elif any(word in command for word in map_lst) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            map()
        ################################################
        ################################################
        elif any(word in command for word in aks_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            photo()
        ################################################
        ################################################
        elif any(word in command for word in ayne_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            ayne()
        ################################################
        ################################################
        elif any(word in command for word in film_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            film()
        ################################################
        ################################################
        elif any(word in command for word in ahang_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            ahang()
        ################################################
        ################################################
        elif any(word in command for word in saat_list) and "سینا" in command :
            ######################
            saat_gooya()
        ################################################
        ################################################
        elif any(word in command for word in tarikh_emrooz_gh_list) and "سینا" in command :
            ######################
            tarikh_gh()
        ################################################
        ################################################
        elif any(word in command for word in tarikh_emrooz_ml_list) and "سینا" in command :
            ######################
            tarikh_ml()
        ################################################
        ################################################
        elif any(word in command for word in emrooz_list) and "سینا" in command :
            ######################
            emrooz()
        ################################################
        ################################################
        elif any(word in command for word in tarikh_emrooz_list) and "سینا" in command :
            ######################
            tarikh()
        ################################################
        ################################################
        elif any(word in command for word in tarikh_kamel_emrooz_list) and "سینا" in command :
            ######################
            tarikh_kamel()
        ################################################
        ################################################
        elif any(word in command for word in app_runner_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            App_runer()
        ################################################
        ################################################
        elif any(word in command for word in voice_recorder_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            voic_recorder()
        ################################################
        ################################################
        elif any(word in command for word in adad_gooya_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            play_audio("E . or. D:\\you model dataset sonds directory\\ورود عدد.mp3")
            time.sleep(1)
            adad = int(input("لطفا عدد را وارد کنید : ***-***-***-*** ::: "))
            adad_bekhan(adad)
        ################################################
        ################################################
        elif any(word in command for word in tas_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            tas()
        ################################################
        ################################################
        elif any(word in command for word in seke_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            seke()
        ################################################
        ################################################
        elif any(word in command for word in khamoosh_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            shut_down()
        ################################################
        ################################################
        elif any(word in command for word in sleep_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            sleep()
        ################################################
        ################################################
        elif any(word in command for word in check_internet_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            check_internet_connect()
        ################################################
        ################################################
        elif any(word in command for word in connect_to_internet_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            internet()
            play_audio("E . or. D:\\you model dataset sonds directory\\kari_bari.mp3")
            time.sleep(2.5)
        ################################################
        ################################################
        elif any(word in command for word in wiki_list) and "سینا" in command :
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            wiki_pedia()
        ################################################
        ################################################
        elif any(word in command for word in google_list) and "سینا" in command:
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            google()
        ################################################
        ################################################
        elif any(word in command for word in hesab_list) and "سینا" in command:
            play_audio("E . or. D:\\you model dataset sonds directory\\hatman.mp3")
            time.sleep(2.5)
            mohasebe()
        ################################################
        ################################################
        elif any(word in command for word in fohsh_list) and "سینا" in command :
            fosh_ha = connect_to_data_base()
            cur = fosh_ha.cursor()
            cur.execute(f"SELECT * FROM fahashi")
            kol = cur.fetchall()[0]
            print(kol)
            if int(kol[3]) <= 3 :
                a = int(random.randint(1, 4))
                print(a)
                play_audio(f"E . or. D:\\you model dataset sonds directory\\فحش ({a}).mp3")
                time.sleep(5)
                ab = "  ***  "
                cur.execute(f"UPDATE fahashi SET tedade_kol = '{kol[1] + 1}', fohsh = '{kol[2]} {ab * 5} {command}', tedade_movaghat = '{kol[3] + 1}'")
                fosh_ha.commit()
                pas("")

            elif int(kol[3]) == 4 :
                play_audio(f"E . or. D:\\you model dataset sonds directory\\فحش=خواموشی.mp3")
                time.sleep(5)
                ab = "  ***  "
                cur.execute(f"UPDATE fahashi SET tedade_kol = '{kol[1] + 1}', fohsh = '{kol[2]} {ab * 5} {command}', tedade_movaghat = '{kol[3] + 1}'")
                fosh_ha.commit()
                pas("")

            elif int(kol[3]) == 5 :
                play_audio(f"E . or. D:\\you model dataset sonds directory\\فحش و خواموش.mp3")
                time.sleep(9)
                os.system(f"shutdown /s /t 5")
        ################################################
        ################################################
        elif "هیچی" in command :
            #
            play_audio("E . or. D:\\you model dataset sonds directory\\بیپ.mp3")
        ################################################
        ################################################
        elif any(word in command for word in ghorboon_sadaghe) :
            play_audio("E . or. D:\\you model dataset sonds directory\\خواهش_میکنم.mp3")
            time.sleep(5)
        ################################################
        else:
            #
            pas("")
        ################################################
        ################################################

if __name__ == "__main__":
    get_up_sina()
    reset_fosh()
    pas("")














