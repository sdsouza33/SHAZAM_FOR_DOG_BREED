import cv2
import pandas as pd
import numpy as np
import scipy
import h5py
import keras
import time
import tensorflow as tf
from keras.applications.imagenet_utils import preprocess_input
from PIL import Image
from sklearn.metrics import accuracy_score
from keras.applications.resnet50 import ResNet50
from keras.layers import Input
from keras.models import Model

import os
from tqdm import tqdm
import keras
from PIL import Image
import os
import matplotlib.pyplot as plt
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print("Starting to Load model .h5 file")
new_model = load_model('K:/Resnet50/transfer-learning/exam1.h5')

print("Model Loaded")
global graph
graph = tf.get_default_graph()

df = pd.read_csv('K:/Resnet50/labels.csv')



breed=['pomeranian', 'scottish_deerhound', 'shetland_sheepdog', 'clumber', 'curly-coated_retriever', 'german_short-haired_pointer', 'rhodesian_ridgeback', 'briard', 'doberman', 'scotch_terrier', 'kerry_blue_terrier', 'french_bulldog', 'kuvasz', 'samoyed', 'maltese_dog', 'boxer', 'cairn', 'malamute', 'standard_schnauzer', 'bouvier_des_flandres', 'dingo', 'toy_poodle', 'miniature_schnauzer', 'yorkshire_terrier', 'bluetick', 'bloodhound', 'entlebucher', 'welsh_springer_spaniel', 'miniature_pinscher', 'norfolk_terrier', 'black-and-tan_coonhound', 'whippet', 'bedlington_terrier', 'beagle', 'collie', 'redbone', 'kelpie', 'german_shepherd', 'gordon_setter', 'keeshond', 'giant_schnauzer', 'saluki', 'border_collie', 'cardigan', 'standard_poodle', 'dandie_dinmont', 'old_english_sheepdog', 'english_setter', 'groenendael', 'shih-tzu', 'weimaraner', 'basset', 'pug', 'irish_water_spaniel', 'bull_mastiff', 'walker_hound', 'soft-coated_wheaten_terrier', 'siberian_husky', 'newfoundland', 'airedale', 'australian_terrier', 'golden_retriever', 'affenpinscher', 'great_pyrenees', 'dhole', 'mexican_hairless', 'vizsla', 'otterhound', 'irish_setter', 'malinois', 'west_highland_white_terrier', 'rottweiler', 'norwich_terrier', 'papillon', 'pembroke', 'chow', 'irish_wolfhound', 'pekinese', 'greater_swiss_mountain_dog', 'borzoi', 'tibetan_mastiff', 'brabancon_griffon', 'sealyham_terrier', 'toy_terrier', 'great_dane', 'lhasa', 'bernese_mountain_dog', 'border_terrier', 'labrador_retriever', 'silky_terrier', 'norwegian_elkhound', 'english_springer', 'sussex_spaniel', 'ibizan_hound', 'cocker_spaniel', 'leonberg', 'brittany_spaniel', 'saint_bernard', 'chihuahua', 'miniature_poodle', 'afghan_hound', 'chesapeake_bay_retriever', 'lakeland_terrier', 'komondor', 'tibetan_terrier', 'appenzeller', 'basenji', 'wire-haired_fox_terrier', 'schipperke', 'american_staffordshire_terrier', 'eskimo_dog', 'irish_terrier', 'japanese_spaniel', 'flat-coated_retriever', 'boston_bull', 'african_hunting_dog', 'staffordshire_bullterrier', 'blenheim_spaniel', 'english_foxhound', 'italian_greyhound']
#val=sorted(set(df['breed']))

#print("BREED ++???",val[61]) 
#print(*zip(val,range(len(val))))  
#print("BREED ++???",df['breed'][61])
print("labels loaded")

n = len(df)
#breed = set(df['breed'])
n_class = len(breed)
class_to_num = dict(zip(breed, range(n_class)))
num_to_class = dict(zip(range(n_class), breed))
breed=list(breed)
width = 256



def detect(img1):
    if img1=='default.jpg':
        return 'Please give a proper image'
    else:    
        print("IMAGE++++++++>>>>>",img1)
        pred=[]
        I_p='K:/Resnet50/test_train'
        PATH=os.path.join(I_p,str(img1))
        print(PATH)
        img=np.expand_dims(cv2.resize(cv2.imread(PATH),(width,width)),axis=0)

        with graph.as_default():
            Y_pred = new_model.predict(img, verbose=2)
            y_pred = np.argmax(Y_pred, axis=1)
            print(y_pred,np.max(Y_pred))

        if np.max(Y_pred)*100<55:
            for i in y_pred:
                print("BREED NAME +++++>>>",breed[i])
            return 'Please upload an appropriate image'                        
        else:    
            for i in y_pred:
                print("BREED NAME +++++>>>",i)
                pred.append(breed[i])
            return '{0} Accuracy : {1}%'.format(' '.join(pred),str(round(np.max(Y_pred)*100,2)))


def give_image(img1):
    I_p='K:/Resnet50/train/'
    PATH=os.path.join(I_p,str(img1))
    print(str(img1))
    return PATH