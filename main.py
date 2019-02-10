import input_api as datainput
import Analyzer as analysis
import OutputAlert as output
import AI_module as AI
from datetime import datetime as dt

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
    sign_array = read_data('vital_signs.txt')
    output.print_title(sign_array[0][0], sign_array[0][2], sign_array[0][1])
    for sign in sign_array:
        patient = datainput.Patient(sign[0], sign[1], sign[2], sign[3], sign[4],sign[5], sign[6], sign[7], dt.now())
        patient_analyze = analysis.Analyzer(patient.dic['Systolic_BP'], patient.dic['Diastolic_BP'],\
                                patient.dic['heartrate'], patient.dic['blood_oxygen'],patient.dic['temperature'])
        output.print_patient_data(patient.dic['Systolic_BP'], patient.dic['Diastolic_BP'],\
                                patient.dic['heartrate'], patient.dic['blood_oxygen'],patient.dic['temperature'])
        output.alert_management(patient.dic['Systolic_BP'], patient.dic['Diastolic_BP'],\
                                patient.dic['heartrate'], patient.dic['blood_oxygen'],patient.dic['temperature'])
        

if __name__ == "__main__":
    main()