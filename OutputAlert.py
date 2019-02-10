from AI_module import AI_module
import Analyzer as analysis
from datetime import datetime as dt

def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
 ##Boolean Parameters
 ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {'Signal_Loss':False, 'Shock_Alert':False,'Oxygen_Supply':False,'Fever':False,'Hypotension':False,'Hypertension':False}
    if(Singal_Loss == True):
        BasicResult['Signal Loss']=True
    if(Shock_Alert == True):
        BasicResult['Shock_Alert']=True 
    if(Oxygen_Supply == True):
        BasicResult['Oxygen_Supply']=True 
    if(Fever == True):
        BasicResult['Fever']=True
    if(Hypotension == True):
        BasicResult['Hypotension']=True
    if(Hypertension == True):
        BasicResult['Hypertension']=True 

    return BasicResult



#def send_basic_input_data(BasicResult, BasicData):
 ## Receive the result and show it on terminal or web page
 #   sentData = analyze(BasicResult)
 #   return sentData, BasicData

def print_patient_data(Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
    print("Time: ", dt.now())
    print('Systolic Blood Pressure: ', Systolic_BP)
    print('Diastolic Blood Pressure: ', Diastolic_BP)
    print('Heart Rate: ', Heart_Rate)
    print('Heart Oxygen Level', Heart_O2_Level)
    print('Body Temperature: ', Body_temp)

def print_title(patientID, gender, age):
    print("Welcome to the Vital Sign Montitoring System")
    print("============================================")
    print('Patient ID: ', patientID)
    print('Gender:', gender)
    print('Age: ', age)
    print("============================================")
    print("|Vital Sign|")

def alert_management(Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
    new_alert = analysis.Analyzer(Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp)
        
    if (new_alert.Shock_Alert(int(Heart_Rate), int(Body_temp)) == True or\
        new_alert.Signal_Loss(int(Heart_Rate), int(Body_temp)) == True or\
        new_alert.Oxygen_Supply(int(Heart_O2_Level)) == True or\
        new_alert.Fever(int(Body_temp)) == True or\
        new_alert.Hypotension(int(Systolic_BP), int(Diastolic_BP)) == True or\
        new_alert.Hypertension(int(Systolic_BP), int(Diastolic_BP)) == True):
        print('\n\033[1;31;40m|Alert|\033[0m')
    else:
        print('All the vital signs were within normal limits.\n')

    if new_alert.Shock_Alert(int(Heart_Rate), int(Body_temp)) == True:
        print('\033[1;31;40mShock_Alert!\033[0m')

    if new_alert.Signal_Loss(int(Heart_Rate), int(Body_temp)) == True:
        print('\033[1;31;40mWarning: Signal_Loss!\033[0m')

    if new_alert.Oxygen_Supply(int(Heart_O2_Level)) == True:
        print('\033[1;31;40mPlease Increase Oxygen_Supply!\033[0m')

    if new_alert.Fever(int(Body_temp)) == True:
        print('\033[1;31;40mFever!\033[0m')

    if new_alert.Hypotension(int(Systolic_BP), int(Diastolic_BP)) == True:
        print('\033[1;31;40mHypotension\033[0m')

    if new_alert.Hypertension(int(Systolic_BP), int(Diastolic_BP)) == True:
        print('\033[1;31;40mHypertension\033[0m')
    
    print("---------------")

def display_AI_iuput_data():
 ## Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
 ## Paramter is boolean
 ## If paramter is True, means it should be alerted, then add it to the array
  
    AI_module.AI_Module(Blood_oxygen, Blood_pressure, Pulses)
    print('blood pressure prediction:')
    print(pressure_predict_result)
    print('blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse_predict_result:')
    print(Pulse_predict_result)
    
#def send_AI_input_data(AIResult):
 ## Receive the result and show it on terminal or web page
 #   sentData = analyze(AIResult)
 #   return sentData
