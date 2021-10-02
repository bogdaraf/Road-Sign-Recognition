import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from keras.models import load_model

#Load the trained model
model = load_model('model.h5')

#Label all traffic signs classes.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

def classify(file_path, label):
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
    label.place(relx=0.5, rely=0.3, anchor=CENTER)

def show_classify_button(file_path, label):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path, label),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.5,rely=0.8, anchor=CENTER)

def upload_image(label):
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded = uploaded.resize((150,150))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        sign_image.place(relx=0.5, rely=0.5, anchor=CENTER)
        label.configure(text='')
        show_classify_button(file_path, label)
    except:
        pass

#Initialise GUI
top=tk.Tk()
top.geometry('400x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

#Heading, text shown at the top
heading = Label(top, text="Road Sign Recognition",pady=50, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()

#Label, after successful classification shows the class of the sign
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))

#Upload image button
upload=Button(top,text="Upload an image",command=lambda: upload_image(label),padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.place(relx=0.5, rely=0.7, anchor=CENTER)

#Road sign image
sign_image = Label(top)

top.mainloop()