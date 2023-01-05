import tkinter as tk #import to make app
from PIL import Image,ImageTk # use to set background
import requests # use to call api for the weather data 

#Key:3d6a72f243fbffab92cc9dd0d6b3ad44    my api key dont use  it create your own api  
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} api calling linkg

root =tk.Tk() #creating the window

root.title("Weather app")# define the title name of app
root.geometry("600x500")# define the size window size of app

def format_response(weather): # function for get data display on app window
    try:
           city=weather['name']
           condition=weather['weather'][0]['description']
           temp=weather['main']['temp']
           final_str ='City:%s\nCondition:%s\ntemprature:%s'%(city,condition,temp)
    except:
         final_str='there was probleam in retrieving data'
    return final_str       


def get_weather(city):# function for calling api and get data in the app
    weather_key = '3d6a72f243fbffab92cc9dd0d6b3ad44'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID':weather_key,'q':city,'units':'imperial'}
    response =requests.get(url,params)
    #print(response.json())
    weather = response.json()
   
   
   # print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])


    result['text']= format_response(weather)#to get the result formt


    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)


    def open_image(icon_name):# function for icon display in data
        size=int(frame_two.winfo_height()*0.25)
        img=ImageTk.PhotoImage(Image.open('./img/'+icon_name+'.png').resize((size,size)))
        weather_icon.delete('all')
        weather_icon.create_image(0,0,anchor='nw',image=img)
        weather_icon.image=img


img=Image.open('./bg.png.jpg')#getting image file to background of app
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)
bg_lbl=tk.Label(root,image=img_photo)

bg_lbl.place(x=0,y=0)


frame_one=tk.Frame(bg_lbl,bg="#00ffff",bd=5)#creating frame to input city name
frame_one.place(x=80,y=60,width=450,height=50)

heading_title= tk.Label(bg_lbl,text='Earth including over 200,000 cities !',fg='#0000FF',bg='#F0F0F8',font=('times new roman',18,'bold'))


#creating the button for get the weather report
txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='W')
btn =tk.Button(frame_one,text='get weather',fg='green',font=('times new roman',16,'bold'),command =lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)


#this frame is create to display the weather data the city when we call api
frame_two=tk.Frame(bg='#7F7FFF',bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='#FCFCFC',justify ='left',anchor='nw')
result.place(relwidth=1,relheight=1)

#creating canvas for the img icon
weather_icon=tk.Canvas(result,bg='#DEDEDE',bd=0,highlightthickness=0)
weather_icon.place( x=0.75,y=0,relwidth=1,relheight=0.5)


root.mainloop()