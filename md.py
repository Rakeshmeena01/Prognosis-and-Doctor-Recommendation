# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:38:17 2022

@author: RakeshPC
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit import scriptrunner 
import pandas as pd
import numpy as np
import sqlite3

# For Animations
import json

import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
#lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_u1vbg6qk.json")
lottie_heart = load_lottiefile("Heart.json")
lottie_obesity = load_lottiefile("Obesity.json")
lottie_dengue = load_lottiefile("Dengue.json")
lottie_diabetes = load_lottiefile("Diabetes.json")
lottie_pcos = load_lottiefile("Women.json")
lottie_covid = load_lottiefile("Covid19.json")



#st_lottie(lottie_coding,
 #         height=200,
  #        width=200,
   #       key="hello")
#st_lottie(lottie_hello,
 #         height=400,
  #        width=400)
#st_lottie(lottie_heart,
 #         height=400,
  #        width=400)
#st_lottie(lottie_obesity,
 #         height=400,
  #        width=400)
#st_lottie(lottie_dengue,
 #         height=400,
  #        width=400)
#st_lottie(lottie_diabetes,
 #         height=400,
  #        width=400)
#st_lottie(lottie_pcos,
 #         height=400,
  #        width=400)
#st_lottie(lottie_covid,
 #         height=400,
  #        width=400)



# loading the saved models

diabetes_model = pickle.load(open('D:/College/Doctor/diabetes/trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('D:/College/Doctor/heartdisease/heart_disease_model.sav','rb'))

#pcos_model = pickle.load(open(' D:/College/Doctor/PCOS/data without infertility _final.sav','rb'))

obesity_model = pickle.load(open('D:/College/Doctor/Obesity/ObesityDataSet_raw_and_data_sinthetic.sav','rb'))

covid_model = pickle.load(open("D:/College/Doctor/Covid/covid.sav",'rb'))

dengue_model = pickle.load(open("D:\College\Doctor\Multiple Disease Prediction/dengue_savfile.sav",'rb'))



username = ''
# sidebar for navigation
with st.sidebar:
    


    # DB Management
  
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Security
    #passlib,hashlib,bcrypt,scrypt
    import hashlib
    def make_hashes(password):
    	return hashlib.sha256(str.encode(password)).hexdigest()

    def check_hashes(password,hashed_text):
    	if make_hashes(password) == hashed_text:
    		return hashed_text
    	return False
    # DB Management
    import sqlite3 
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    # DB  Functions
    def create_usertable():
    	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


    def add_userdata(username,password):
    	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    	conn.commit()

    def login_user(username,password):
    	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    	data = c.fetchall()
    	return data


    def view_all_users():
    	c.execute('SELECT * FROM userstable')
    	data = c.fetchall()
    	return data



    def main():
    	"""Simple Login App"""

    	st.title("Login")

    	menu = ["Login","SignUp"]
    	choice = st.sidebar.selectbox("Menu",menu)

    	#if choice == "Home":
    	#	st.subheader("Home")

    	if choice == "Login":
    		st.subheader("Login Section")

    		username = st.sidebar.text_input("User Name")
    		password = st.sidebar.text_input("Password",type='password')
    		if st.sidebar.checkbox("Login"):
    			# if password == '12345':
    			create_usertable()
    			hashed_pswd = make_hashes(password)

    			result = login_user(username,check_hashes(password,hashed_pswd))
    			if result:

    				st.success("Logged In as {}".format(username))

    				#task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
    				#if task == "Add Post":
    				#	st.subheader("Add Your Post")

    				#elif task == "Analytics":
    				#	st.subheader("Analytics")
    				#elif task == "Profiles":
    				#	st.subheader("User Profiles")
    				#	user_result = view_all_users()
    				#	clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
    				#	st.dataframe(clean_db)
    			else:
    				st.warning("Incorrect Username/Password")


    	elif choice == "SignUp":
    		st.subheader("Create New Account")
    		new_user = st.text_input("Username")
    		new_password = st.text_input("Password",type='password')

    		if st.button("Signup"):
    			create_usertable()
    			add_userdata(new_user,make_hashes(new_password))
    			st.success("You have successfully created a valid Account")
    			st.info("Go to Login Menu to login")



    if __name__ == '__main__':
    	main()

    
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Obesity Prediction',
                           'Dengue Prediction',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'PCOS Prediction',                           
                           'Covid Prediction'],
                          icons=['person','person','person','heart','person','person'],
                          default_index=0)
    
   # doctor = option_menu('Doctor Recommendation',
                          
    #                      ['Diabetes – (Endocrinologist)',
     #                      'Heart disease – (Cardiologist)',
      #                     'Obesity – ( Bariatricians )',
       #                    #'Cataract – (Ophthalmologist)',
        #                   'PCOS – (Gynecologist)'],
         #                 icons=['activity','heart','person','person'],
          #                default_index=0)
    

#st.info(username)
  
####################   Diabetes      ########################


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>Diabetes Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_diabetes,
              height=400,
              width=400)
    
    # getting the input data from the user
    col = st.columns(1)
    #with col:
    Pregnancies = st.text_input('Number of Pregnancies ','Enter number of pregnancies')

    col = st.columns(1)
    #with col:
    Glucose = st.text_input('Glucose Level (Enter Number only)','Enter glucose level in mg/dl')

    col = st.columns(1)
    #with col:
    BloodPressure = st.text_input('Blood Pressure value (Enter Number only)','Enter blood pressure in mm Hg') 
   

    col = st.columns(1)
    #with col:
    SkinThickness = st.text_input('Skin Thickness value (Enter Number only)','Enter the thickness of skin in mm')


    col = st.columns(1)
    #with col:
    Insulin = st.text_input('Insulin Level (Enter Number only)','Enter the insulin level inn mg per dl')

    col = st.columns(1)
    #with col:
    BMI = st.text_input('BMI value (Enter Number only)','Enter enter body mass index value in kg per m^2')


    col = st.columns(1)
    #with col:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (Enter Number only)','Enter value of diabetes pedigree function, it scores the likelihood of diabetes based on family history ')


    col = st.columns(1)
    #with col:
    Age = st.text_input('Age of the Person (Enter Number only)','Enter age in years ')

# code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic.. please  consult a  diagnostic specialist '
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)
        st.write('Recommended Doctors')
        df = pd.read_csv("Diabetes_doc.csv")
        st.dataframe(df)
    




##################### heart disease ###################

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_heart,
              height=400,
              width=400)
    
    col = st.columns(3)
    #with col1:
    age = st.text_input('Enter age (numbers only)','Enter age in years')
    

    col = st.columns(3)
    #with col1:
    sex = st.text_input('Gender (Enter Number only)','Enter 0 for female and 1 for male')

    col = st.columns(3)
    #with col1:
    cp = st.text_input('Enter Chest Pain types','Enter 0 for typical angina, 1 for atypical angina, 2 for non-typical angina and 3 for asymptomatic.')

    col = st.columns(3)
    #with col1:
    trestbps = st.text_input('Resting Blood Pressure (Enter Number only)','Enter restin blood pressure in mm Hg')

    col = st.columns(3)
    #with col1:
    chol = st.text_input('Serum Cholestoral in mg/dl (Enter Number only)','Enter Serum Cholestoral in mg/dl')

    col = st.columns(3)
    #with col1:
    fbs = st.text_input('Fasting Blood Sugar','Enter 0 if less than 120 mg/dl and 1 if greater than 120 mg/dl')

    col = st.columns(3)
    #with col1:
    restecg = st.text_input('Resting Electrocardiographic results ','Enter 0 for normal, enter 1 for having ST-T wave abnormality and enter 2 for showing probable or definite left ventricular') 

    col = st.columns(3)
    #with col1:
    thalach = st.text_input('Maximum Heart Rate achieved (Enter Number only)','Enter the maximum heart rate achieved')

    col = st.columns(3)
    #with col1:
    exang = st.text_input('Exercise Induced Angina','Enter 0 for no and 1 for yes') 

    col = st.columns(3)
    #with col1:
    oldpeak = st.text_input('ST depression induced by exercise (Enter Numbers )','This value ranges from -2.6 to 6.2') 

    col = st.columns(3)
    #with col1:
    slope = st.text_input('Slope of the peak exercise ST segment','Enter 0 for upsloping, enter 1 for flat and 2 for downsloping')

    col = st.columns(3)
    #with col1:
    ca = st.text_input('Major vessels colored by flourosopy (Enter Number in  0,1,2,3)','Enter major vessels coloured from 0-3 ')

    col = st.columns(3)
    #with col1:
    thal = st.text_input('Thal :A blood disorder called thalassemia','Enter 0 for thal, 1 for fixed defect:no blood flow in some part of the heart and 2 for reversable defect:a blood flow  is observed but it is not normal')


    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease or less chances '

        st.success(heart_diagnosis)
        st.write('Recommended Doctors')
        df = pd.read_csv("Heart_doc.csv")
        st.dataframe(df)
    
    
#########################   PCOS   ############################    
    
# PCOS Prediction    
if (selected == 'PCOS Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>PCOS Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_pcos,
              height=400,
              width=400)

    # getting the input data from the user
    col = st.columns(3)
    #with col1:
    Skin_darkening = st.text_input('Skin darkening (Enter Number only)','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    hairg_rowth  = st.text_input('Hair growth','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Weight_gain = st.text_input('Weight gain ','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Cycle = st.text_input('Cycle ','Enter no. of right cycles') 

    col = st.columns(3)
    #with col1:
    Fast_food = st.text_input('Fast food ','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Pimples = st.text_input('Pimples ','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Weight = st.text_input('Weight','Enter weight in kg')

    col = st.columns(3)
    #with col1:
    BMI = st.text_input('BMI  (Enter Number only)','Enter Body Mass Index ')

    col = st.columns(3)
    #with col1:
    Cycle_length = st.text_input('Cycle length (Enter Number only)','Enter cycle length in days')

    col = st.columns(3)
    #with col1:
    Hair_loss = st.text_input('Hair loss','Enter 0 for no and 1 for yes')
    
    col = st.columns(3)
    #with col1:
    Age  = st.text_input('Age (yrs) ','Enter age in years') 

    col = st.columns(3)
    #with col1:
    Waist = st.text_input('Waist(inch)','Enter waist size in inch')

    col = st.columns(3)
    #with col1:
    Hip = st.text_input('Hip(inch) ','Enter hip size in inches') 


    col = st.columns(3)
    #with col1:
    Marraige_Status  = st.text_input('Marraige Status (Yrs)','Enter the number of years after marriage') 

    col = st.columns(3)
    #with col1:
    Pulse_rate = st.text_input('Pulse rate(bpm)','Enter pulse rate in bpm')

    col = st.columns(3)
    #with col1:
    Hb = st.text_input('Hb(g/dl) ','Enter haemoglobin in g/dl')

    col = st.columns(3)
    #with col1:
    Height = st.text_input('Height(Cm) ','Enter height in centimetres')

    col = st.columns(3)
    #with col1:
    Reg_Exercise= st.text_input('Regular Exercise ','Enter 0 for no and 1 for yes')


    col = st.columns(3)
    #with col1:
    No_of_aborptions = st.text_input('No. of aborptions','Enter number of abortions')

    # creating a button for Prediction

    if st.button('PCOS Test Result'):
        prediction = data.predict([[Skin_darkening ,hair_growth  , Weight_gain ,Cycle ,Fast_food, Pimples ,Weight, BMI, Cycle_length , Hair_loss ,Age ,Waist , Hip , Marraige_Status ,Pulse_rate ,Hb, Height ,Reg_Exercise ,No_of_aborptions]])
        

        if (prediction[0] == 1):
            PCOS = 'The person is having PCOS '
        else:
           PCOS = 'The person dont have PCOS'

        st.success(PCOS)
        st.write('Recommended Doctors')
        df = pd.read_csv("PCOS_doc.csv")
        st.dataframe(df)
    
    
    

########################## Obesity Prediction   ########################################

if (selected == 'Obesity Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>Obesity Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_obesity,
              height=400,
              width=400)
    
    # getting the input data from the user
    col = st.columns(3)
    #with col1:
    Gender = st.text_input('Gender (Enter Numbers)','Enter 0 for female and 1 for male')

    col = st.columns(3)
    #with col1:
    Age = st.text_input('Age (yrs)','Enter age in years')

    col = st.columns(3)
    #with col1:
    Weight = st.text_input('Weight (kgs)','Enter weight in kgs')

    col = st.columns(3)
    #with col1:
    FamilyHistoryWithOverweight = st.text_input('Family History with Overweight','Enter 0 for no and 1 for yes') 

    col = st.columns(3)
    #with col1:
    Frequentconsumptionofhighcaloricfood = st.text_input('Frequent consumption of high caloric food','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Frequencyofconsumptionofvegetables = st.text_input('Frequency of consumption of vegetables','Enter number of times you consume vegetables')

    col = st.columns(3)
    #with col1:
    Numberofmainmeals = st.text_input('Number of main meals','Enter number of meals you intake')

    col = st.columns(3)
    #with col1:
    Consumptionoffoodbetweenmeals = st.text_input('Consumption of food between meals','Enter 0 for no, 1 for sometimes, 2 for frequently and 3 for always')

    col = st.columns(3)
    #with col1:
    Smoke = st.text_input('Smoke','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    Consumptionofwaterdaily = st.text_input('Consumption of water daily','Enter 1 for less than 1L, 2 for between 1-2L and 3 for more than 2 L')

    col = st.columns(3)
    #with col1:
    Caloriesconsumptionmonitoring = st.text_input('Calories consumption monitoring','Enter 0 for no and 1 for yes') 


    col = st.columns(3)
    #with col1:
    Physicalactivityfrequency = st.text_input('Physical activity frequency','Enter 0 for no, 1 for 1-2 days, 2 for 2-4 days and 3 for 4-5days')

    col = st.columns(3)
    #with col1:
    Timeusingtechnologydevices = st.text_input('Time using technology devices','Enter 0 for no,  0–2 hours, 1 for  3–5 hours , 2 for More than 5 hours')

    col = st.columns(3)
    #with col1:
    Consumptionofalcohol = st.text_input('Consumption of alcohol ','Enter 0 for no, 1 for sometimes, 2 for frequently and 3 for always')

    col = st.columns(3)
    #with col1:
    Transportationused = st.text_input('Transportation used','Enter 1 for Public_Transportation, 2 for Automobile , 3 for Walking, 4 for Motorbike and 5 for bike')

    # code for Prediction
    Obesity = ''

    # creating a button for Prediction

    if st.button('Obesity Test Result'):
        prediction = obesity_model.predict(
            [[Gender, Age, Weight, FamilyHistoryWithOverweight,Frequentconsumptionofhighcaloricfood, Frequencyofconsumptionofvegetables, Numberofmainmeals, Consumptionoffoodbetweenmeals, Smoke, Consumptionofwaterdaily, Caloriesconsumptionmonitoring, Physicalactivityfrequency, Timeusingtechnologydevices,Consumptionofalcohol, Transportationused]])
           
        if (prediction[0] == 0):
            Obesity = 'The person is having Normal Weight'
        elif (prediction[0] == 1):
            Obesity = 'The person is overweight level 1'
        elif (prediction[0] == 2):
            Obesity = 'The person is overweight level 2'
        elif (prediction[0] == 3):
            Obesity = 'The person is obesity level 1'
        elif (prediction[0] == 4):
            Obesity = 'The person is obesity level 2'
        elif (prediction[0] == 5):
            Obesity = 'The person is obesity level 3'
        else:
            Obesity = 'The person has insufficient weight'


        st.success(Obesity)
        st.write('Recommended Doctors')
        df = pd.read_csv("Obesity_doc.csv")
        st.dataframe(df)
    
    
    
##################################  COVID predictrion #####################################################

if (selected == 'Covid Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>Covid Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_covid,
              height=400,
              width=400)
    
    # getting the input data from the user
    col = st.columns(3)
    #with col1:
    cough = st.text_input('Cough (Enter Numbers only)','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    fever  = st.text_input('Fever','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    sorethroat = st.text_input('Sore throat','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    shortnessofbreath = st.text_input('Shortness of breath ','Enter 0 for no and 1 for yes') 

    col = st.columns(3)
    #with col1:
    headache = st.text_input('Headache','Enter 0 for no and 1 for yes')


    col = st.columns(3)
    #with col1:
    age60andabove = st.text_input('Age 60 and above ','Enter 0 for no and 1 for yes')

    col = st.columns(3)
    #with col1:
    gender = st.text_input('Gender ','Enter 1 for male and 0 for female')


    col = st.columns(3)
    #with col1:
    testindication= st.text_input('Test indication','Enter 1 for contact with confirmed covid, 2 for abroad and 0 for other ')


      
    # code for Prediction
    Covid = ''

    # creating a button for Prediction

    if st.button('Covid Test Result'):
        prediction = covid_model.predict([[cough ,fever,sorethroat, shortnessofbreath ,headache , age60andabove ,gender, testindication]])
        

        if (prediction[0] == 2):
            Covid = 'The person is having Covid '
        elif (prediction[0] == 0):
            Covid = 'The person is not having covid' 
        else:
            Covid = 'It is hard to say anything covid report'

        st.success(Covid)
        st.write('Recommended Doctors')
        df = pd.read_csv("No_info_doc.csv")
        st.dataframe(df)
        
    
#################################      Dengue Predictrion                 #########################################

# Dengue Prediction Page
if (selected == 'Dengue Prediction'):

    # page title
    st.markdown("<h1 style='text-align: center; color: green;'>Dengue Prediction</h1>", unsafe_allow_html=True)
    st_lottie(lottie_dengue,
              height=300,
              width=300)

    # getting the input data from the user
    col = st.columns(3)
    #with col1:
    bodytemperature = st.text_input('Body temperature (Enter numbers only)','Enter body temperatue in celcius')
    #with col2:
        #st.markdown('Enter body temperatue in celcius')
    #with col3:
        #st.markdown('Fever can be a symptom of dengue')

    col = st.columns(3)
    #with col1:
    whitebloodcellcount = st.text_input('White bloodcell count (Enter number only)','Enter number of white blood cells')
    #with col2:
     #   st.markdown('Enter number of white blood cells')
    #with col3:
     #   st.markdown('White blood cell count decreases in dengue patients')

    col = st.columns(3)
    #with col1:
    severeheadache  = st.text_input('Severe headache -> Enter(0,1)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    painbehindtheeyes = st.text_input('Pain behind the eyes (Enter Number only)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    jointmuscleaches = st.text_input('Joint muscle aches (Enter Number only)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown(' ')

    col = st.columns(3)
    #with col1:
    metallictasteinthemouth = st.text_input('Metallic taste in the mouth (Enter Number only)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    appetiteloss = st.text_input('Appetite loss (Enter Number only)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    abdominalpain = st.text_input('Abdominal pain (Enter Number only)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    nauseavomiting = st.text_input('Nausea vomiting (Enter Numbers 0 or 1)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    extremeloosemotions = st.text_input('Extreme loosemotions (Enter Numbers)','Enter 0 for no and 1 for yes')
    #with col2:
     #   st.markdown('Enter 0 for no and 1 for yes')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    haemoglobin = st.text_input('Haemoglobin (Enter Numbers only','Enter haemoglobin in g/dl')
    #with col2:
     #   st.markdown('Enter haemoglobin in g/dl')
    #with col3:
     #   st.markdown('')

    col = st.columns(3)
    #with col1:
    plateletcount = st.text_input('Platelet count (Enter Numbers only','Enter number of platelets per microliter of blood')
    #with col2:
     #   st.markdown('Enter number of platelets per microliter of blood')
    #with col3:
     #   st.markdown('')



    # code for Prediction
    dengue_diagnosis = ''

    # creating a button for Prediction

    if st.button('Dengue Disease Test Result'):
        dengue_prediction = dengue_model.predict(
            [[bodytemperature, whitebloodcellcount, severeheadache,
    painbehindtheeyes, jointmuscleaches,
       metallictasteinthemouth, appetiteloss, abdominalpain,
       nauseavomiting, extremeloosemotions, haemoglobin,
       plateletcount]])

        if (dengue_prediction[0] == 1):
            dengue_diagnosis = 'The person is having dengue Please consult doctor'
        else:
            dengue_diagnosis = 'The person does not have dengue or less chances '

        st.success(dengue_diagnosis)
        st.write('Recommended Doctors')
        df = pd.read_csv("No_info_doc.csv")
        st.dataframe(df)
    
    

       
 

    
   
 