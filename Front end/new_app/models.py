from django.db import models

# Create your models here.
import numpy as np
import pickle



import joblib
import numpy as np
import pandas as pd
#from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import load_model

# Load the model
#lstm1 = load_model(r'C:\Users\ST-0010\Music\ITML12-SMS\CODING\Front end\sms_lstm.h5',"rb")



# Testing phase
# log = pickle.load(open("email_log_bow.pkl", 'rb'))
svm = pickle.load(open("sms_svm_tfidf.pkl", 'rb'))
rf = pickle.load(open("sms_RF_tfidf.pkl", 'rb'))
lstm = pickle.load(open("sms_RF_tfidf.pkl", 'rb'))

countvect = pickle.load(open("tfidf.pkl", 'rb'))


def predict(text,algo): 
	#text = [text]
	filter_text = countvect.transform(text)
	print(filter_text.shape)
	if algo=='#':
		y_pred=lstm.predict(filter_text)
		return y_pred[0]
	elif algo== 'SGD':
		y_pred = svm.predict(filter_text)
		return y_pred[0]
	else:
		y_pred=rf.predict(filter_text)
		return y_pred[0]