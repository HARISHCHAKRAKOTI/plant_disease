# working
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model

# Load the trained model to classify plant leaf diseases
model = load_model("D:\docking\Project\plant_96.h5")

# Dictionary to label all plant leaf disease classes
class_labels = {
    0:'Apple___Apple_scab',
 1:'Apple___Black_rot',
 2:'Apple___Cedar_apple_rust',
 3:'Apple___healthy',
 4:'Blueberry___healthy',
 5:'Cherry_(including_sour)___Powdery_mildew',
 6:'Cherry_(including_sour)___healthy',
 7:'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 8:'Corn_(maize)___Common_rust_',
 9:'Corn_(maize)___Northern_Leaf_Blight',
 10:'Corn_(maize)___healthy',
 11:'Grape___Black_rot',
 12:'Grape___Esca_(Black_Measles)',
 13:'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 14:'Grape___healthy',
 15:'Orange___Haunglongbing_(Citrus_greening)',
 16:'Peach___Bacterial_spot',
 17:'Peach___healthy',
 18:'Pepper,_bell___Bacterial_spot',
 19:'Pepper,_bell___healthy',
 20:'Potato___Early_blight',
 21:'Potato___Late_blight',
 22:'Potato___healthy',
 23:'Raspberry___healthy',
 24:'Soybean___healthy',
 25:'Squash___Powdery_mildew',
 26:'Strawberry___Leaf_scorch',
 27:'Strawberry___healthy',
 28:'Tomato___Bacterial_spot',
 29:'Tomato___Early_blight',
 30:'Tomato___Late_blight',
 31:'Tomato___Leaf_Mold',
 32:'Tomato___Septoria_leaf_spot',
 33:'Tomato___Spider_mites Two-spotted_spider_mite',
 34:'Tomato___Target_Spot',
 35:'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 36:'Tomato___Tomato_mosaic_virus',
 37:'Tomato___healthy'
}

# Initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Plant Leaf Disease Classification')
top.configure(background='peach puff')

label = Label(top, background='aqua', font=('Times New Roman', 15, 'bold'))
leaf_image = Label(top)

def classify(file_path):
    try:
        global label
        image = Image.open(file_path)
        image = image.resize((256, 256))  # Assuming the model requires 96x96 images
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)
        pred = np.argmax(model.predict(image))
        disease_class = class_labels[pred]
        label.configure(foreground='#011638', text=f'Predicted Disease: {disease_class}({pred})')
    except Exception as e:
        print("Error occurred:", e)

def show_classify_button(file_path):
    classify_button = Button(top, text="Classify Image", command=lambda: classify(file_path),
                             padx=10, pady=5)
    classify_button.configure(background='#364156', foreground='white', font=('Times New Roman', 15, 'bold'))
    classify_button.place(x=490, y=550)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        leaf_image.configure(image=im)
        leaf_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except Exception as e:
        print("Error occurred:", e)

upload_button = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
upload_button.configure(background='#364156', foreground='white', font=('Times New Roman', 10, 'bold'))

upload_button.pack(side=BOTTOM, pady=50)
leaf_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

heading = Label(top, text="Plant Leaf Disease Detection", pady=20, font=('Times New Roman', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
