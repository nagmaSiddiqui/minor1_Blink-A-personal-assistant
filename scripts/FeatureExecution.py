import VoiceInput as vr
import datetime
import wikipedia
import webbrowser
import time
import random
import subprocess
import requests
import wolframalpha
import os
import winshell
import speech_recognition as sr
import pywhatkit
import keyboard
from AppOpener import run
from pygame import mixer
# from inputmode import mode_select
from standardfunctions import *
from dialogue import *
from api_keys import *
import pygame
from pathlib import Path
import asyncio
import winsdk.windows.media.control as wmc

BlinkInputMode=0 #Globally declare input as text default

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

pygame.mixer.pre_init(44100, -16, 2, 64)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(relative_to_assets("assistant_voice_started.mp3"))

def takeCommand():
    print("Listening....")
    pygame.mixer.music.play()
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 4000
    r.pause_threshold = 1
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
    try:
        print("Recognizing....")
        said = r.recognize_google(audio, language='en')
        print(f"You Said : {said}\n")
    except sr.UnknownValueError:
        print("could not understand audio \n~Trying Again~")
        return takeCommand()
    except sr.RequestError as e:
        print(
            "Could not request results, check your internet connection; {0}".format(e))
        return "None"
    return said.lower()


def takecommand_text():
    query = input(">> ")
    return query.lower()


def take_input(variable):
    if variable == 0:
        return takecommand_text()
    elif variable == 1:
        return takeCommand()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        # playsound._#playsoundWin(os.path.join('soundeffects\sfx',"gm.mp3"))
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        # playsound._#playsoundWin(os.path.join('soundeffects\sfx',"ga.mp3"))
        print("Hello,Good Afternoon")
    else:
        # playsound._#playsoundWin(os.path.join('soundeffects\sfx',"ge.mp3"))
        print("Hello,Good Evening")
    time.sleep(2)


async def getMediaSession():
    sessions = await wmc.GlobalSystemMediaTransportControlsSessionManager.request_async()
    session = sessions.get_current_session()
    return session

def mediaIs(state):
    session = asyncio.run(getMediaSession())
    if session == None:
        return False
    return int(wmc.GlobalSystemMediaTransportControlsSessionPlaybackStatus[state]) == session.get_playback_info().playback_status #get media state enum and compare to current main media session state

def note(text):
    '''date = datetime.datetime.now()'''
    r = random.randint(1, 20000000)
    note_name = ("Blink-note" + str(r))
    with open(note_name, "w") as f:
        f.write(text)
    print("Note saved as : ", note_name)
    subprocess.Popen(["notepad.exe", note_name])

# here is the exceution functions i made it, so that the main code looks a bit clean XD

def showmagic(statement):
    
        ##playsound.#playsound(os.path.join('soundeffects\sfx',"howcanihelpyounow.mp3"))
        #print("\nTell Me How Can I Help you Now ?")

    if statement==None:
        print("No Input Detected!\n")
        
    else:
        if 'pause' in statement:
            session=asyncio.run(getMediaSession())
            session.try_pause_async()

        elif "resume" in statement:
            session = asyncio.run(getMediaSession())
            session.try_play_async()

        elif "open" in statement:
            query=statement.split('open')
            run(query[1])

        elif "hibernate" in statement or "sleep" in statement: #note this feature only works if there is a mic connected. 
            vr.Speak("Hibernating.")
            print("please use the wakeword to wake me up, till then i'll be going undercover.")
            print("Available Wake Words :\n1.Assistant activate\n2.wake up assistant")
            time.sleep(2)
            subprocess.call('start scripts/Hotword/hotword_detection.pyw', shell=True)
            time.sleep(0.5)
            quit()

        # elif "no thanks"==statement:
        #     vr.Speak("ok, i will sleep for some time then.")
        #     print("ok, i will sleep for some time then.")
        #     print("\nuse the wakeword to awake me, till then i'll be going undercover.")
        #     time.sleep(2)
        #     subprocess.call('start scripts/Hotword/hotword_detection.pyw', shell=True)
        #     quit()

        elif "hi"==statement or "hello" in statement :
            hello_greating=any_random(hello)
            print(hello_greating,"\n(NOTE:if you wanna have chat with me. just use the 'Lets Chat' command)")
            vr.Speak(hello_greating)
            time.sleep(1)

        elif " youtube" and "play" in statement:
            statement=statement.replace("play ","")
            statement=statement.replace(" on youtube","")
            query=statement.split('youtube')
            srch=query
            print("Searching for : ",srch," on youtube")
            print("opening youtube...")
            sss=(f"https://www.youtube.com/results?search_query="+
                    "+".join(srch))
            pywhatkit.playonyt(sss)
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3")) 
            time.sleep(1)

        elif "search" and "youtube" in statement:
            query=statement.split('youtube and search for')
            srch=query
            print("Searching for : ",srch," on youtube")
            print("opening youtube...")
            sss=(f"https://www.youtube.com/results?search_query="+
                    "+".join(srch))
            webbrowser.open_new_tab(sss)
            time.sleep(1)

        elif 'open youtube' in statement:
                vr.Speak('Opening Youtube...')
                webbrowser.open_new_tab("https://www.youtube.com")
                time.sleep(1)
                print("youtube is open now.")
                #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
                time.sleep(2)

        elif 'open google photo' in statement:
            vr.Speak('Opening Google Photos')
            webbrowser.open_new_tab("https://photos.google.com/login")
            time.sleep(3)

        elif 'open github' in statement:
            print('Opening GitHub...')
            webbrowser.open_new_tab("https://github.com/")
            print('GitHub is now Open.')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            print("Google chrome is open now.")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif "snipping tool" in statement:
            print("Opening Snipping Tool")
            os.system("start snippingtool")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif "screenshot" in statement:
            import random
            time.sleep(1.5)
            import pyscreenshot
            image = pyscreenshot.grab()
            r = random.randint(1,20000000)
            file_name=("Blinkscreenshot"+ str(r) +".png")
            image.save(file_name)
            print("Screenshot saved as : ",file_name)
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"done.wav"))
            time.sleep(2)

        elif "edge" in statement:
            print("Opening Microsoft Edge")
            os.system("start msedge")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3")) 
            time.sleep(2)

        elif 'open whatsapp' in statement or 'whatsapp' in statement:
            webbrowser.open_new_tab('https://web.whatsapp.com/')
            print('opening WhatsApp Web')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(6)

        elif 'open instagram' in statement or 'instagram' in statement:
            webbrowser.open_new_tab('https://www.instagram.com/')
            print('opening Instagram')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(6)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            print("Google Mail is open now.")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif 'open discord' in statement or 'discord' in statement:
            webbrowser.open_new_tab("https://discord.com/channels/@me")
            print("discord is open now.")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif 'open facebook' in statement:
            print('opening facebook...')
            webbrowser.open_new_tab("https://www.facebook.com/")
            print('facebook is open now.')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(2)

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            print("Here is stackoverflow")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(1)

        elif 'clear cache' in statement or 'clear system cache' in statement or 'boost system' in statement:
            vr.Speak("Clearing system Cache....")
            vr.Speak("please do not touch anything for a while, the automated process is starting.")
            keyboard.press_and_release('win+R')
            time.sleep(1)
            keyboard.write("%temp%",delay=0.1)
            time.sleep(0.7)
            keyboard.press_and_release("enter")
            print("clearing cache in process....")
            time.sleep(2.6)
            keyboard.press_and_release("ctrl+a")
            time.sleep(0.5)
            keyboard.press_and_release("del+shift")
            time.sleep(0.7)
            keyboard.press_and_release("enter")
            print ('Starting the removal of the file !\n')
            print("If you see any Error, just Delete the Temp Folder manually.")
            time.sleep(1)

        elif "open my inbox" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(1)

        elif "open my sent mails" in statement or "open my sent mail" in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(1)

        elif 'open terminal' in statement or 'cmd' in statement:
            os.startfile ("cmd")
            print("Command Prompt is Open Now")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"taskcompleted.mp3"))
            time.sleep(1)

        elif 'log off' in statement or 'sign out' in statement:
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            subprocess.call(["shutdown", "/l"])

        elif "shutdown" in statement or "shut down" in statement:
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            time.sleep(1)
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"shutdown.mp3"))
            time.sleep(1)
            os.system('shutdown/s')

        elif "restart my pc" in statement:
            vr.Speak("okay, restarting your pc")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"logoff.mp3"))
            os.system('shutdown/r')
        
        elif 'date today' in statement or 'today date' in statement:
            from datetoday import today_date
            print(today_date())
            vr.Speak(today_date())
            time.sleep(1)
        
        elif "empty recycle bin" in statement:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                vr.Speak("you should press enter if any dialog box appears.")
                time.sleep(1.3)
                vr.Speak("Recycle Bin Emptied")

        elif "note" in statement or "remember this" in  statement:
                print("What would you like me to write down?")
                vr.Speak("What would you like me to write down?")
                note_text = take_input(Blink_input_mode)
                note(note_text)
                print("I have made a note of that.\n")
                #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"done.wav"))

        elif "weather" in statement:
            #API KEY REQUIRED HERE
            if weather_api_key=="fcde3268d682df74d42316d89caa74c1":   #{this part can be comment out later,and indexing below shall be fixed
                print("You need to get an API key first!\n")
                vr.Speak("You need to get an API key first!")
            else: 
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"cityname.mp3"))
                print("\nwhats the city?")
                city_name= take_input(Blink_input_mode)
                complete_url=base_url+"appid="+weather_api_key+"&q="+city_name     #weather_api_key is the api key here
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]

                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\nhumidity (in percentage) = " +
                        str(current_humidiy) +
                        "\ndescription = " +
                        str(weather_description))
                    vr.Speak("Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\nhumidity in percentage is " +
                        str(current_humidiy) +
                        "\ndescription  " +
                        str(weather_description))

                else:
                    vr.Speak(" City Not Found. ")
                    print(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            vr.Speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx',"news.mp3"))
            time.sleep(6)

        elif "search on google" in statement:
                statement = statement.split("search on google")
                search = statement
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                vr.Speak("Searching " + str(search) + " on google")
                #playsound._#playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
                time.sleep(1)

        elif 'ask' in statement:
            if wolfram_api_key=="YOUR API KEY HERE":
                print("You need to get an API key first!")
            else:
                vr.Speak("I can answer to computational and geographical questions and what question do you want to ask now")
                query=take_input(Blink_input_mode)
                client = wolframalpha.Client(wolfram_api_key) #API KEY REQUIRED HERE
                res = client.query(query)
                answer = next(res.results).text
                print(answer)

        elif 'wikipedia' in statement:
            vr.Speak("Searching Wikipedia about it...")
            statement =statement.replace("search on wikipedia about", "")
            try:
                results = wikipedia.summary(statement, sentences=3)
                vr.Speak("According to Wikipedia")
                print(results)
                vr.Speak(results)
            except:
                vr.Speak("Unknown Error Occured, say your question again.")
                
        
        elif 'who is' in statement:
            try:
                vr.Speak("getting information from Wikipedia..")
                statement =statement.replace("who is ","")
                results = wikipedia.summary(statement, sentences=3)
                vr.Speak("According to Wikipedia")
                print(results)
                vr.Speak(results)
            except:
                vr.Speak("Enable to Fetch Data,try again.")
                

        elif "where is" in  statement:
                ind = statement.split().index("is")
                location = statement[ind + 8:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                vr.Speak("This is where i found, " + str(location))
                webbrowser.open(url)    
                #playsound._#playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
                time.sleep(1)

        elif 'yt studio' in statement or 'open yt studio' in statement:
            webbrowser.open_new_tab("https://studio.youtube.com/")
            vr.Speak("opening youtube creator studio")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
            time.sleep(2)

        elif 'live studio' in statement or 'livestream dashboard' in statement or 'live control room' in statement:
            webbrowser.open_new_tab('https://studio.youtube.com/channel/UCWe1CSEpVq_u6WDk3F7E2Mg/livestreaming/manage')
            vr.Speak("opening youtube livestream dashboard")
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','taskcompleted.mp3'))
            time.sleep(2)

        elif 'how were you born' in statement  or 'why were you born' in statement:
            print('''
            I was born with a team of university students in 2022.''')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','born.mp3'))
            time.sleep(1)

        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am Blink your Persoanl AI assistant. I am programmed for managing normal tasks in your Life')
            vr.Speak("I am Blink your Persoanl AI assistant. I am programmed for managing normal tasks in your Life")
            time.sleep(1)

        elif 'who are you' in statement or 'what is your name' in statement :
            vr.Speak("my name is Blink, how could you forget me :-(")
            print('my name is Blink your A.I assistant')
            print(" (ㆆ_ㆆ) "*3)
            time.sleep(1)

        elif 'tell commands' in statement or 'your commands' in statement  or 'command' in statement:
            vr.Speak("Telling you the list of my commands :")
            vr.Speak("below is the list of all commands respectively.")
            print('\n\nbelow is the list of all commands respectively')
            from console import command_list
            print(command_list)
            time.sleep(1)

        # elif 'chat' in statement: 
        #     #print('\nChat Feature is Still in under development version,\nso please have patience while using it.')
        #     chat(Blink_input_mode)
        #     from console import bug
        #     print(bug)
        #     time.sleep(1)


        elif 'i want to dictate' in statement:
            vr.Speak("okay opening dictation option.")
            time.sleep(0.5)
            keyboard.press_and_release('win+H')
            time.sleep(0.5)
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','done.wav'))
            

        elif 'say' in statement or 'pronounce' in statement:
            vr.Speak("okay, type the text.")
            what_to_say=input('What you Want Me To Say : ')
            print('user entered :',what_to_say)
            vr.Speak(what_to_say)
            time.sleep(2)


        elif "thanks" in statement:
            reply_to_thanks=any_random(np)
            print(reply_to_thanks)
            vr.Speak(reply_to_thanks)

        else:
            print('Unable to Read Your Command\nError: Unknown Command')
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','systemdown.mp3'))
            #playsound._#playsoundWin(os.path.join('soundeffects\sfx','responses.wav'))
            time.sleep(2)
        return 0