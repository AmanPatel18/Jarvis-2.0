# required modules
from tkinter import *
from Tkinter.custom_module import window_at_centre
from PIL import ImageTk
import PIL.Image
import threading
from tkinter import ttk
from datetime import datetime
import pyttsx3
import time
import weather
from speech_recognition import *
import webbrowser
import sys
import os
import playsound
from random import randint
import pygame

# To track number of times play music command has given
global track, entry_field, win, stop_button, mic_btn, isplaying
track = 0
entry_field = None
win=None
stop_button=None
mic_btn=None
isplaying=0

class Jarvis:

    def __init__(self):
        # initialise the engine of pyttsx3 
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[3].id)
        self.engine.setProperty('rate',185)
        

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        hour = int(time.strftime('%H'))
        if hour >= 0 and hour < 12:
            message='Good Morning!'
            entry_field.insert(END,message)
            self.speak(message)
        elif hour >= 12 and hour < 16:
            message='Good Afternoon!'
            entry_field.insert(END,message)
            self.speak(message)
        else:
            message='Good Evening!'
            entry_field.insert(END,message)
            self.speak(message)
        message="मैं जार्विस हूं सर, कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूँ?"
        entry_field.delete(0,END)
        entry_field.insert(END, message)
        self.speak(message)

    def current_time(self):
        hour = int(time.strftime('%I'))
        minute = time.strftime('%M')
        meridian = time.strftime('%p')
        time_dictionary={1:'एक',2:'दो',3:'तीन',4:'चार',5:'पाँच',6:'छः',7:'सात',8:'आठ',9:'नौ',10:'दस',11:'ग्यारह',12:'बारह'}
        hour_str=time_dictionary[hour]
        message = '\nसमय हुआ है - '+str(hour)+':'+minute+' '+meridian
        speak = '\nसमय हुआ है - '+hour_str+' बजकर '+minute+' मिनट '+meridian
        entry_field.delete(0,END)
        entry_field.insert(END,message)
        self.speak(speak)

    def file_explorer(self):
        os.startfile("C:\\Windows\\explorer.exe")
        message = 'मैं फ़ाइल एक्सप्लोरर खोल रहा हूँ...'
        entry_field.delete(0,END)
        entry_field.insert(END,message)
        self.speak(message)

    def notepad(self):
        message='मैं नोटपैड खोल रहा हूँ...'
        entry_field.delete(0,END)
        entry_field.insert(END,message)
        self.speak(message)
        os.startfile("C:\\Windows\\notepad.exe")

    def bye(self):
        global mic_btn
        img3 = ImageTk.PhotoImage(PIL.Image.open('C:/users/patel/pictures/PNG/mic3.png'))
        option = ['\nअलविदा सर!', '\nगुड बाय और टेक केयर सर!',
                  '\nअलविदा फिर मिलेंगें!']
        choice = randint(0, len(option)-1)
        entry_field.delete(0,END)
        entry_field.insert(END,option[choice])
        self.speak(option[choice])
        mic_btn.config(image=img3)
        playsound.playsound("C:\\Users\\patel\\Music\\Audio\\robot_blip2.wav",True)
        time.sleep(1)
        sys.exit(win.destroy())

    def youtube(self):
            webbrowser.open_new_tab('https://www.youtube.com')
            message='यूट्यूब खोला जा रहा है...'
            entry_field.delete(0,END)
            entry_field.insert(END,message)
            self.speak(message)

    def say_name(self):
      message = '\nमेरा नाम जार्विस है।'
      entry_field.delete(0,END)
      entry_field.insert(END,message)
      self.speak(message)

    def play_music(self):
        global track, isplaying
        pygame.mixer.init()
        if track==0 and isplaying==0:
            option = ['\nसंगीत बजाया जा रहा है...', '\nये रहा आपका गाना...']
            choose = randint(0, len(option)-1)
            entry_field.delete(0,END)
            entry_field.insert(END,option[choose])
            self.speak(option[choose])
            track=1

        os.chdir('C:/users/patel/music/music library/')
        music_list = os.listdir()
        choice = randint(0, len(music_list)-1)
        song='C:/users/patel/music/music library/'+music_list[choice]
        print(song)

        try:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            isplaying=1
            track=0
        except:
            self.play_music()
        
    def stop_music(self):
        global isplaying
        isplaying=0
        pygame.mixer.music.pause()
    
    def change_music(self):
        global isplaying
        if isplaying==1:
            os.chdir('C:/users/patel/music/music library/')
            music_list = os.listdir()
            choice = randint(0, len(music_list)-1)
            song='C:/users/patel/music/music library/'+music_list[choice]

            try:
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
            except:
                self.change_music()
        else:
            message = 'फिलहाल कोई गाना नहीं बज रहा है।'
            entry_field.delete(0,END)
            entry_field.insert(END,message)
            self.speak(message)

    def things_i_do(self):
        option = [
            'मैं आपको समय बता सकता हूँ।',
            'मैं आपके लिए फाइल एक्स्प्लोरर खोल सकता हूँ।',
            'मैं आपके लिए नोटपैड खोल सकता हूँ।',
            'मैं आपके बाय बाय  कहने पर इस एप्प को बंद कर सकता हूँ।',
            'मैं आपके लिए यूट्यूब खोल सकता हूँ।',
            'मैं आपके लिए गाने बजा सकता हूँ।',
            'मैं आपको अपना नाम बता सकता हूँ।',
            'मैं आपको आपके शहर के तापमान क बारे में जानकारी दे सकता हूँ।'
            ]
        message='मैं ये कुछ चीजे कर सकता हूँ -'
        entry_field.delete(0,END)
        entry_field.insert(END, message)
        self.speak(message)

        for task in option:
                entry_field.delete(0, END)
                entry_field.insert(END, task)
                self.speak(task)

    def weather(self):
        question = '\nसर, क्या आप कृपया मुझे शहर का नाम बता सकते हैं?'
        entry_field.delete(0,END)
        entry_field.insert(END,question)
        self.speak(question)

        recognize = Recognizer()
        with Microphone() as source:
            entry_field.delete(0,END)
            entry_field.insert(END,'सुन रहा हूँ...')
            recognize.energy_threshold = 4000
            recognize.pause_threshold = 2
            audio = recognize.listen(source)
            entry_field.delete(0, END)
            entry_field.insert(END, 'समझ रहा हूँ...')
            city = recognize.recognize_google(audio, language='en-in')

            weather.init(city)
            temperature = weather.temp()
            message = f'बर्तमान में {city} का तापमान है- '
            entry_field.delete(0,END)
            entry_field.insert(END,message+str(temperature)+u"\N{DEGREE SIGN}C")
            self.speak(message+' '+str(temperature)+' डिग्री सेल्सियस')

    def takeCommand(self):
        recognize = Recognizer()
        with Microphone() as source:
            entry_field.delete(0, END)
            entry_field.insert(END,'सुन रहा हूँ...')
            recognize.energy_threshold = 4000
            recognize.pause_threshold = 1
            audio = recognize.listen(source)
            try:
                entry_field.delete(0, END)
                entry_field.insert(END, 'समझ रहा हूँ...')
                text = recognize.recognize_google(audio, language='hi-in')
                text = text.lower()
                return text

            except Exception as e:
                print(e)
                #message = 'माफ करना सर!, कृपया फिर से कहें!'
                #entry_field.delete(0, END)
                #entry_field.insert(END,message)
                #self.speak(message)

    def main(self):
        playsound.playsound('C:/users/patel/music/audio/robot_blip.wav',True)
        self.wishMe()
        while(True):
            query = self.takeCommand()
            if query == None:
                continue

            if 'फाइल एक्स्प्लोरर' in query or 'फाइल' in query:
                self.file_explorer()

            elif 'बाय' in query or 'गुड बाय' in query or 'रेस्ट' in query:
                self.bye()

            elif 'नोटपैड खोलो' in query:
                self.notepad()

            elif 'समय' in query or 'टाइम' in query:
                self.current_time()

            elif 'नाम' in query or 'तुम कोन हो' in query:
                self.say_name()

            elif 'यूट्यूब' in query:
                self.youtube()

            elif 'गाना' in query or 'म्यूजिक' in query:
                self.play_music()
            
            elif 'बदलो' in query or 'चेंज' in query:
                self.change_music()
            
            elif 'बंद करो' in query or 'म्यूजिक बंद करो' in query:
                self.stop_music()

            elif 'चीजे' in query or 'कर सकते हो' in query:
                self.things_i_do()

            elif 'मौसम' in query or 'तापमान' in query:
                self.weather()

            else:
                r = Recognizer()
                with Microphone() as source:
                    r.energy_threshold = 4000
                    r.pause_threshold = 2
                    entry_field.delete(0,END)
                    entry_field.insert(END,'आपने कहा - '+'"'+query+'"'+'।')
                    self.speak('आपने कहा - '+query)
                    time.sleep(1)
                    entry_field.delete(0,END)
                    entry_field.insert(END, 'क्या मैं सही हूं, सर?')
                    self.speak('क्या मैं सही हूं, सर?')
                    entry_field.delete(0, END)
                    entry_field.insert(END, 'सुन रहा हूँ...')
                    audio = r.listen(source)
                    entry_field.delete(0, END)
                    entry_field.insert(END, 'समझ रहा हूँ...')
                    query = r.recognize_google(audio, language='hi-in')

                    if 'सही हो' in query or 'हाँ' in query or 'यू आर राइट' in query or 'यस' in query :
                        message = 'शुक्रिया जनाब मैं खुद को और बेहतर बनाने की कोसिस करता रहूँगा।'
                        entry_field.delete(0,END)
                        entry_field.insert(END,message)
                        self.speak(message)

                    else:
                        message='मुझे माफ करना सर!, मैं अभी भी सीख रहा हूं ...'
                        entry_field.delete(0,END)
                        entry_field.insert(END,message)
                        self.speak(message)

#---------------------------------------------------------------------------------------#

# splash screen window
splash=Tk()
splash.resizable(0,0)
splash.overrideredirect(True)
splash.wm_attributes('-topmost',True)

window_at_centre(splash, 600, 267)

# photoimage for background of splash screen
jarvis=PhotoImage(file="C:\\Users\\patel\\Pictures\\PNG\\jarvis2.png")

bgLabel=Label(splash,image=jarvis)
bgLabel.pack()

# loading label for splash screen
loadingLabel=Label(splash,font=('Times 20 bold'),fg='aqua',bg='black')
loadingLabel.place(x=280,y=190)

# change style 
s=ttk.Style()
s.theme_use('clam')
s.configure("bar.Horizontal.TProgressbar", troughcolor='black',
            bordercolor='aqua', background='aqua', lightcolor='aqua', darkcolor='aqua')

# Progress bar (loading bar)
bar=ttk.Progressbar(splash,style="bar.Horizontal.TProgressbar",orient=HORIZONTAL,length=180,mode='determinate')
bar.place(x=280, y=230)

#---------------------------------------------------------------------------------------#

# main application window     
def main_win():
    global entry_field, win, stop_button ,mic_btn
    win = Toplevel()
    win.title('Coding Drift')
    win.config(bg='black')
    win.wm_attributes('-topmost',True)
    win.overrideredirect('True')
    window_at_centre(win, 620, 300)
    win.wm_attributes('-alpha', 0.8)
    splash.withdraw()

    # initialise the instance of Jarvis
    model = Jarvis()

    # function to change the color of mic on hover
    def effect_change(e):
        mic_btn.config(image=img2)

    # function to revert the color of mic on hover leave
    def effect_revert(e):
        mic_btn.config(image=img1)
        
    # main header Jarvis Voice Assistant
    header = Label(win, text="Jarvis Voice Assistance",
                   font=('Times 32 bold'), bg='black', fg='gold')
    header.pack(pady=10)

    # diaplay date
    
    date=datetime.now()
    date=date.strftime('%A\n%d-%b-%Y')
    date_label=Label(win,text=date,font=('Times 16 bold'),bg='black',fg='orange')
    date_label.place(x=460,y=80)

    # image of mic
    img1 = ImageTk.PhotoImage(PIL.Image.open('C:/users/patel/pictures/PNG/mic1.png'))
    img2 = ImageTk.PhotoImage(PIL.Image.open('C:/users/patel/pictures/PNG/mic2.png'))

    # button to speak to Jarvis
    mic_btn = Button(win, image=img1, bg='black', relief='flat',activebackground='black',borderwidth=0,command=threading.Thread(target=model.main).start)
    mic_btn.pack(pady=10)

    # entry field
    entry_field = Entry(win, font=('Georgia 15 bold'),
                        bg='black', fg='light green', relief='flat', justify=CENTER)
    entry_field.pack(pady=20,ipadx=200)

    # event-binding
    mic_btn.bind('<Enter>', effect_change)
    mic_btn.bind('<Leave>', effect_revert)

i=0
# function for screen loading status
def load():
    global i
    if i<=10:
        txt='Loading... '+str(i*10)+'%'
        loadingLabel['text']=txt
        bar['value']=10*i
        i += 1
        loadingLabel.after(500,load)
    else:
        main_win()

# function to load the loading bar
load()
mainloop()
