#Developed by: Dallas Foster
#Date: March 17, 2023
#Desc: Healthcare System Program
#Inputs: PatientID, New Visits, 
#Outputs: Total visits, List of visits, Average vital signs
import datetime
from typing import List, Dict, Optional

#These constants are used to indicate which vital sign to access, making the code more maintainable.
#The following constants are used to index columns in the patient data file
FILE_PATIENTID = 0
FILE_VISIT_DATE = 1
FILE_BODY_TEMPERATURE = 2
FILE_HEART_RATE = 3
FILE_RESPIRATORY_RATE = 4
FILE_SYSTOLIC_BLOOD_PRESSURE = 5
FILE_DIASTOLIC_BLOOD_PRESSURE = 6
FILE_OXYGEN_SATURATION = 7
 
#The following constants are used to index vital signs in a patient's visit record
VISIT_VISIT_DATE = 0
VISIT_BODY_TEMPERATURE = 1
VISIT_HEART_RATE = 2
VISIT_RESPIRATORY_RATE = 3
VISIT_SYSTOLIC_BLOOD_PRESSURE = 4
VISIT_DIASTOLIC_BLOOD_PRESSURE = 5
VISIT_OXYGEN_SATURATION = 6
 

def formatContent(content):
    '''
    Function is used to format a line from the file

    If there is a formatting error, the error is passed to the calling function

    content: Content is the visit information from the text file. The expected format is:[date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)]

    the function then returns the formatted content in dictionary format
    '''

    #Strip leading/training spaces from the line and split the csv content
    content = content.strip()
    contents = content.split(',')
    contentClean = [contentItem.strip() for contentItem in contents]
 
    #Check the number of columns in the content
    if len(contentClean) != 8:
        raise ValueError(f"Invalid number of fields ({len(contentClean)})")
    
    formattedContent = []
    
    #Try to cast the columns into the correct format. If there is a casting error it will pass an error to the calling function
    try:
        formattedContent.append(int(contentClean[FILE_PATIENTID]))
        formattedContent.append(str(contentClean[FILE_VISIT_DATE]))
        formattedContent.append(float(contentClean[FILE_BODY_TEMPERATURE]))
        formattedContent.append(int(contentClean[FILE_HEART_RATE]))
        formattedContent.append(int(contentClean[FILE_RESPIRATORY_RATE]))
        formattedContent.append(int(contentClean[FILE_SYSTOLIC_BLOOD_PRESSURE]))
        formattedContent.append(int(contentClean[FILE_DIASTOLIC_BLOOD_PRESSURE]))
        formattedContent.append(int(contentClean[FILE_OXYGEN_SATURATION]))
    except:
        raise TypeError("Invalid data type")   
    
    #There where no issues with the content, so return it    
    return formattedContent
 

def validateVisit(visit):
    '''
    Function is used to validate visit data. If there is an invalid value, it raises an error to the calling function

    visit: is a dictionary representing the patients visits

    the function does not return a value
    '''

    #Check the temperature column
    if not isValidTemperature(visit[VISIT_BODY_TEMPERATURE]):
        raise ValueError(f"Invalid temperature value ({visit[VISIT_BODY_TEMPERATURE]})")
    
    #Check the Heart Rate column
    if not isValidHeartRate(visit[VISIT_HEART_RATE]):
        raise ValueError(f"Invalid heart rate value ({visit[VISIT_HEART_RATE]})")
    
    #Check the Respiratory Rate column
    if not isValidRespiratoryRate(visit[VISIT_RESPIRATORY_RATE]):
        raise ValueError(f"Invalid respiratory rate value ({visit[VISIT_RESPIRATORY_RATE]})")
      
    #Check the Systolic Blood Pressure column
    if not isValidSystolicBloodPressure(visit[VISIT_SYSTOLIC_BLOOD_PRESSURE]):
        raise ValueError(f"Invalid systolic blood pressure value ({visit[VISIT_SYSTOLIC_BLOOD_PRESSURE]})")
         
    #Check the Diastolic Blood Pressure column
    if not isValidDiastolicBloodPressure(visit[VISIT_DIASTOLIC_BLOOD_PRESSURE]):
        raise ValueError(f"Invalid diastolic blood pressure value ({visit[VISIT_DIASTOLIC_BLOOD_PRESSURE]})")
            
    #Check the Oxygen Saturation column
    if not isValidOxygenSaturation(visit[VISIT_OXYGEN_SATURATION]):
        raise ValueError(f"Invalid oxygen saturation value ({visit[VISIT_OXYGEN_SATURATION]})")


def validateInput(temp, hr, rr, sbp, dbp, spo2):
    '''    
    #Function is used to validate user input. If there is an invalid value, it raises an error to the calling function

    temp: Patients temperature
    hr: Patients heart rate
    rr: Patients repiratory rate
    sbp: Patients systolic blood pressure
    dpb: Patients diastolic blood pressure
    spo2: Patients Oxygen saturation

    The function does not return a value
    '''

    #Check the temperature column
    if not isValidTemperature(temp):
        raise ValueError("Invalid temperature. Please enter a temperature between 35 and 42 degrees C")
    
    #Check the Heart Rate column
    if not isValidHeartRate(hr):
        raise ValueError("Invalid heart rate. Please enter a heart rate between 30 and 180 BPM")
    
    #Check the Respiratory Rate column
    if not isValidRespiratoryRate(rr):
        raise ValueError("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 BPM")
      
    #Check the Systolic Blood Pressure column
    if not isValidSystolicBloodPressure(sbp):
        raise ValueError("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg")
         
    #Check the Diastolic Blood Pressure column
    if not isValidDiastolicBloodPressure(dbp):
        raise ValueError("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg")
            
    #Check the Oxygen Saturation column
    if not isValidOxygenSaturation(spo2):
        raise ValueError("Invalid oxygen saturation. Please enter a oxygen saturation between 70 and 100%")
 

#This function checks if a given value is a valid temperature reading in Celsius
def isValidTemperature(value):
    return value >= 35 and value <= 42

#This function checks if a given value is a valid heart rate reading in beats per minute
def isValidHeartRate(value):
    return value in range (30, 181)

#This function checks if a given value is a valid respiratory rate reading in breaths per minute
def isValidRespiratoryRate(value):
    return value in range (5, 41)

#This function checks if a given value is a valid systolic blood pressure reading in mmHg
def isValidSystolicBloodPressure(value):
    return value in range (70, 201)

#This function checks if a given value is a valid diastolic blood pressure reading in mmHg
def isValidDiastolicBloodPressure(value):
    return value in range (40, 121)

#This function checks if a given value is a valid oxygen saturation reading in percent
def isValidOxygenSaturation(value):
    return value in range (70, 101)
 
#This function checks if a given value is a valid date in ISO format (yyyy-mm-dd)
def isValidDate(value):
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return True
 

#This function opens the given plaintext file and formats it, as well as reads it.
def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.
 
    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    #This sets patients as a dicitonary
    patients = {}
    try:
        #We try to open the file, if an error occurs, it falls to the IOError handler
        f = open(fileName, 'r')
        #Do not skip the first line as there are no headers.  Go right into the loop and read the 1st line
        for line in f.readlines():       
            try:
                #This formats the line of data from the file, if there is an error, it falls to the TypeError handler
                formattedContent = formatContent(line)
                patientId = formattedContent[FILE_PATIENTID]
                visit = formattedContent[1:]
                #This ensures that the elements of the visit are valid, if there is an error, it falls to the ValueError handler
                validateVisit(visit)

                if patientId not in patients:
                    #Make sure to add the missing patient 
                    patients[patientId] = []
                
                #Update the patient's list of visits
                patients[patientId].append(visit)
                
            except (ValueError, TypeError) as err:
                #If an error has been raised, we effectively skip the input line, print the error, and continue to the next line
                print(f"{err} in line: {line}")
        #close the file
        f.close()
    #except the IO error to handle as specified
    except IOError as err:
        print(f"The file '{fileName}' could not be found")
        exit()
    #except all other errors
    except:
        #An error occured while reading the file
        print("An unexpected error occurred while opening the file.")
        
    #Reached the end of the file, so return the patients dictionary
    return patients


def displaySinglePatientData(patients, patientId):
    '''
    #This function displays the vital sign data for a single patient with a given ID

    patients: patients is a dictionary of all the patient data

    patientId: patientId is the key that we want to print the data for. 

    the function does not return a value
    '''

    try:
        #Get all the visits for the patient with the given ID
        visits = patients[patientId]
        print("Patient ID:", patientId)
        #Loop over all the visits for the patient and print the vital sign data
        for visit in visits:
            #Print the statistics of the visits
            print(" Visit Date:", visit[VISIT_VISIT_DATE])
            print("  Temperature:", "%.2f" % visit[VISIT_BODY_TEMPERATURE], "C")
            print("  Heart Rate:", visit[VISIT_HEART_RATE], "bpm")
            print("  Respiratory Rate:", visit[VISIT_RESPIRATORY_RATE], "bpm")
            print("  Systolic Blood Pressure:", visit[VISIT_SYSTOLIC_BLOOD_PRESSURE], "mmHg")
            print("  Diastolic Blood Pressure:", visit[VISIT_DIASTOLIC_BLOOD_PRESSURE], "mmHg")
            print("  Oxygen Saturation:", visit[VISIT_OXYGEN_SATURATION], "%")
    #If the patient ID is not found, print an error message
    except KeyError:
        print("Patient with ID", patientId, "not found.")

    
#This function displays patient data for a given patient ID or for all patients.
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.
 
    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #If patientId is 0, display data for all patients
    if patientId == 0:
        #Loop over all patient IDs and call displaySinglePatientData for each patient
        for patientKey in patients.keys():
            displaySinglePatientData(patients, patientKey)
    else:
         #If a patient ID is provided, call displaySinglePatientData for that patient
        displaySinglePatientData(patients, patientId)

    
#This function prints the average of each vital sign for all patients or for the specified patient.
def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.
 
    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    #Check if patientId is a valid integer, If not print an error message and exit the function
    try:
        patientId = int(patientId)
    except ValueError:
        print("Error: 'patientId' should be an integer.")
        return
    #Check if patients is a dictionary, if not, print an error message and exit the function
    if type(patients) != dict:
        print("Error: 'patients' should be a dictionary.")
        return
    
    #Initialize the counts of the total visits, and the total visit statistics to zero
    visitCount = 0
    bodyTemperatureTotal = 0
    heartRateTotal = 0
    respiratoryRateTotal = 0
    systolicBloodPressureTotal = 0
    diastolicBloodPressureTotal = 0
    oxygenSaturationTotal = 0

    #If patient ID is 0, loop through all patients
    if patientId == 0:
        for patientVisits in patients.values():
            for visit in patientVisits:
                #Add body temperature of visit to total
                bodyTemperatureTotal += visit[VISIT_BODY_TEMPERATURE]
                #Add heart rate of visit to total
                heartRateTotal += visit[VISIT_HEART_RATE]
                # Add respiratory rate of visit to total
                respiratoryRateTotal += visit[VISIT_RESPIRATORY_RATE]
                #Add systolic blood pressure of visit to total
                systolicBloodPressureTotal += visit[VISIT_SYSTOLIC_BLOOD_PRESSURE]
                # Add diastolic blood pressure of visit to total
                diastolicBloodPressureTotal += visit[VISIT_DIASTOLIC_BLOOD_PRESSURE]
                # Add oxygen saturation of visit to total
                oxygenSaturationTotal += visit[VISIT_OXYGEN_SATURATION]
                #Incriment visit count
                visitCount += 1
    #If patient ID is not 0, get data for the specified patient
    else:
        try:
            visits = patients[patientId]
            for visit in visits:
                #Add body temperature of visit to total
                bodyTemperatureTotal += visit[VISIT_BODY_TEMPERATURE]
                #Add heart rate of visit to total
                heartRateTotal += visit[VISIT_HEART_RATE]
                #Add respiratory rate of visit to total
                respiratoryRateTotal += visit[VISIT_RESPIRATORY_RATE]
                  #Add systolic blood pressure of visit to total
                systolicBloodPressureTotal += visit[VISIT_SYSTOLIC_BLOOD_PRESSURE]
                 # Add diastolic blood pressure of visit to total
                diastolicBloodPressureTotal += visit[VISIT_DIASTOLIC_BLOOD_PRESSURE]
                 # Add oxygen saturation of visit to tota
                oxygenSaturationTotal += visit[VISIT_OXYGEN_SATURATION]
                #Incriment visit count
                visitCount += 1
        #If patient ID is not found in the data, print an error message and return
        except KeyError:
            print(f"No data found for patient with ID {patientId}.")
            return

    #Checks if patientId is equal to 0
    if patientId == 0:
        #If true, prints the message for displaying vital signs for all patients
        print("Vital Signs for All Patients:")
    else:
        #If false, prints the message for displaying vital signs for the specified patient
        print("Vital Signs for Patient", str(patientId))

    #Checks if visitCount is equal to 0
    if visitCount == 0:
        #If true, prints a message indicating no data was found. Also exit the function
        print("No data found")
        return
    
    #Print the average of each vital sign
    print(" Average temperature:", "%.2f" % (bodyTemperatureTotal / visitCount), "C")
    print(" Average heart rate:", "%.2f" % (heartRateTotal / visitCount), "bpm")
    print(" Average respiratory rate:", "%.2f" % (respiratoryRateTotal / visitCount), "bpm")
    print(" Average systolic blood pressure:", "%.2f" % (systolicBloodPressureTotal / visitCount), "mmHg")
    print(" Average diastolic blood pressure:", "%.2f" % (diastolicBloodPressureTotal / visitCount), "mmHg")
    print(" Average oxygen saturation:", "%.2f" % (oxygenSaturationTotal / visitCount), "%")


#function to add new patient data to the patient list
def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.
 
    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #Check if the date is in valid format
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        print("Invalid date. Please enter a valid date.")
        return
    
    #Validate the input data for temperature, heart rate, respiratory rate, systolic and diastolic blood pressure, and oxygen saturation level
    try:
        validateInput(temp, hr, rr, sbp, dbp, spo2)
    except ValueError as err:
        print(err)
        return
    #Ask TA if he wants data added to the dictionary or only appended to the file
    if patientId not in patients:
        #Make sure to add the missing patient 
        patients[patientId] = []

    #Create a visit list containing the new data
    visit = [date, temp, hr, rr, sbp, dbp, spo2]
    #Update the patient's list of visits
    patients[patientId].append(visit)
    #Append the new data to the specified file
    try:
        f = open(fileName, 'a')
        f.write('\n' + str(patientId) + ',')
        f.write(date + ',')
        f.write(str(temp) + ',')
        f.write(str(hr) + ',')
        f.write(str(rr) + ',')
        f.write(str(sbp) + ',')
        f.write(str(dbp) + ',')
        f.write(str(spo2))
        f.close()

    except IOError:
            print(f"Error writing to file: {fileName}")


#Function designed to find a patieents visits by either year, or year and month
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.
 
    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    #Create a list of matching visits
    visitsByDate = []

    #We want to validate the year and month by trying to build a date. If the date we build is valid, then we know that the user input acceptable values
    #Convert test month and year to string
    testYear = str(year)
    testMonth = str(month)
    #if year is not provided, set testYear to '2020'
    if year == None: 
        testYear = "2020"
    #if month is not provided, set testMonth to '01'
    if month == None:
        testMonth = "01"
    #if testMonth is a single digit, add leading zero
    if len(testMonth) == 1:
        testMonth = "0" + testMonth
    #check if the provided year-month is valid
    validDate = isValidDate(str(testYear) + "-" + str(testMonth) + "-01")

    if validDate:
        #iterate over visits for each patient
        for patientKey in patients:
            for visit in patients[patientKey]:
                #Create the visit date variable so we can test year and month matches
                visitDate = datetime.date.fromisoformat(visit[VISIT_VISIT_DATE])
                visitYear = visitDate.year
                visitMonth = visitDate.month
                
                if year and month:
                    #Since year and month were both passed, make sure both match
                    if visitYear == year and visitMonth == month:
                        visitsByDate.append((patientKey, visit))
                elif year: 
                    #Since only year was passed, make sure it matches
                    if visitYear == year:
                        visitsByDate.append((patientKey, visit))
                elif not year and not month: 
                    #Since no year or month were passed, add the visit 
                    visitsByDate.append((patientKey, visit))

    #The function will return an updated dictionary. If the year is valid, it will be added like any other date. If not, the dicitonary will be empty
    return visitsByDate
    
 
#Function designed to find patients with abnormal vital signs. It then displays a list of these patients to be booked for a follow up appointment
def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.
 
    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    #create an empty list to store patient IDs who need follow-up visits
    followupPatients = []
    #iterate over all patients
    for patientKey in patients:
        #iterate over all visits for a patient
        for visit in patients[patientKey]:
            #check if vital signs are abnormal for a visit and add the patient ID to the follow-up list
            if visit[VISIT_HEART_RATE] > 100 or visit[VISIT_HEART_RATE] < 60 or visit[VISIT_SYSTOLIC_BLOOD_PRESSURE] > 140 or visit[VISIT_DIASTOLIC_BLOOD_PRESSURE] > 90 or visit[VISIT_OXYGEN_SATURATION] < 90:
                followupPatients.append(patientKey)
                #once a patient has been added to the list, stop checking for more visits for that patient
                break
    #if len(followupPatients) == 0:
    #Provided code already has print statement
    #print("No patients found who need follow-up visits")
    return followupPatients
 

def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.
 
    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
   """
    #Check if patientId exists in patients dictionary
    if patientId in patients:
        #Delete patient's visit data
        del patients[patientId]
        #Open the file in write mode
        try:
            f = open(filename, "w")
            writeNewLine = False
            #Write updated data to file
            for patientKey in patients:
                for visit in patients[patientKey]:
                    #Write a newline character if it's not the first record
                    if writeNewLine:
                        f.write("\n")
                    #Write patient ID and visit details to file
                    f.write(str(patientKey) + ',')
                    f.write(visit[VISIT_VISIT_DATE] + ',')
                    f.write(str(visit[VISIT_BODY_TEMPERATURE]) + ',')
                    f.write(str(visit[VISIT_HEART_RATE]) + ',')
                    f.write(str(visit[VISIT_RESPIRATORY_RATE]) + ',')
                    f.write(str(visit[VISIT_SYSTOLIC_BLOOD_PRESSURE]) + ',')
                    f.write(str(visit[VISIT_DIASTOLIC_BLOOD_PRESSURE]) + ',')
                    f.write(str(visit[VISIT_OXYGEN_SATURATION]))
                    writeNewLine = True

            f.close()
        except IOError:
            print(f"Error writing to file: {filename}")

        #Print success message
        print (f"Data for patient {patientId} have been deleted.")
    else:
        #Print error message if patientId not found in patients dictionary
        print(f"No data found for patient with ID {patientId}")
 

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")
 
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
 
 
if __name__ == '__main__':
    main()
