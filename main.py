import input_api as datainput
import OutputAlert as output
from Database_Module import DataBaseModule
from datetime import datetime as dt
from time import sleep
import threading

# Login to the database
authenDB = {'admin':"123456"}
infoDB = {}
DB = DataBaseModule()
username = 'admin'
password = '123456'
DB.authen(username, password)

def read_data(filename):
    ''' Read data from txt file and save data to a 2D-array'''
    sign_array = []
    file = open(filename, 'r')
    
    # Traverse data in the file
    for line in file:
        fields = line.split()
        uid, age, gender, heartrate, SystolicBP, DiastolicBP, blood_oxygen, temp \
            = fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7]
        sign_array.append([uid, age, gender, heartrate, SystolicBP, DiastolicBP, blood_oxygen, temp])
    return sign_array

def main():
    '''main function of the system'''
    sign_array = read_data('vital_signs.txt')
    # Output patient information
    userID = sign_array[0][0]
    gender = sign_array[0][2]
    age = sign_array[0][1]
    output.print_title(userID, gender, age)
    sign = sign_array[0]
    patient = datainput.Patient(sign[0], sign[1], sign[2], sign[3], sign[4], sign[5], sign[6], sign[7], dt.now())

    def inputData():
        # Buit a patient instance from input module and filter the data
        patient.implement_filter()

    def dataBase():
        # Insert data to the database
        filtered_data = patient.return_request(2)
        DB.insert(userID, filtered_data)

    def outputData():
        # Transfer patient data to output, the analyze module is integrated in the output module
        output.print_patient_data(patient.dic['Systolic_BP'], patient.dic['Diastolic_BP'],\
                                patient.dic['heartrate'], patient.dic['blood_oxygen'],patient.dic['temperature'])

    def alert():
        # If data out of range, sound alert
        output.alert_management(patient.dic['Systolic_BP'], patient.dic['Diastolic_BP'],\
                                patient.dic['heartrate'], patient.dic['blood_oxygen'],patient.dic['temperature'])

    def aiModule():
        # Display AI prediction result
        output.display_AI_iuput_data(patient.dic['blood_oxygen'], patient.dic['Systolic_BP'], patient.dic['heartrate'])

    threads = []
    t1 = threading.Thread(target=inputData)
    threads.append(t1)
    t2 = threading.Thread(target=dataBase)
    threads.append(t2)
    t3 = threading.Thread(target=outputData)
    threads.append(t3)
    t4 = threading.Thread(target=alert)
    threads.append(t4)
    t5 = threading.Thread(target=aiModule)
    threads.append(t5)
    for thread in threads:
        thread.start()
        sleep(0.1)

if __name__ == "__main__":
    main()