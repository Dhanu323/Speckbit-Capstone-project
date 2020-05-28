"""
Health Care Management Application Script
Authors:
    Dhanush Rao H S
"""
from testpack import *
from tabulate import tabulate
import jsonpickle
''' 
Variables
    Visit_doc_paticent_name (list): holds the name of all the patcients who has got a apponintment
    
    doc_list(dict): {index : "docter : specilaization"}
                 holds the All the docter's name and specilaization
   
    Medical_ledger (dict) : {paticent name : Appointment object}
                            holds 
    ''' 
Visit_doc_paticent_name = []
Medical_ledger = {}
doc_list = {1:"Cardiologists : Dr.Vidyadhar sharma ",2:"Psychiatrists : Dr.Ashwini",3:"Dermatologists : Dr.Harsha",4:"Neurologists : Dr.PRIYANKA",5:"Dentist : Dr.Sai Samyam",6:"Ophthalmologists : Dr.Vibha",7:"Otolaryngologists : Dr.Rishabh",8:" Endocrinologists : Dr.Bhavana",9:"Rheumatologists : Dr.Tejes Muthya",10:"Medicine Specialists : Dr.Chandini",11:"Sports Medicine Specialists : Dr.Pavan Kumar",12:"Pulmonologists : Dr.Payaswini K Rao",13:"Hematologists : Dr.Sukesh Bairy",14:"Infectious Disease Specialists : Dr.Suhas Amarnath",15:"Nephrologists : Dr.Vivek Chandra",16:"Genral : Dr.Dhanush Rao"}
      
print("Welcome To Speckbit Health Care Center")
#Application loop
while True:

    # Print the options in a table and  Taking the user's choice from options as (int)
        print("*-*"*30)
        ch = int(input("What would u like to do: \n\
            1. Get Appointment\n\
            2. Consult Doctor\n\
            3. Medical_Certificate-->"))



        if ch == 1:
            '''
            If user choice is 2 (int) : Creation an object of Appoint class and passing the attributes
            '''
# Print the Avalable docters in a table
            table1 = doc_list.items()
            print(tabulate(table1, headers=["Index"," Docter"],tablefmt="fancy_grid"))
            consult_docter = int(input("Enter the index of docter you want to Visit: "))
            # get the paticent details
            doc_name = doc_list[consult_docter] 

            name = input(" paticent Name: ").upper()
            phno = input("paticent Phone: ")
            height = float(input("paticent height: "))
            weight = float(input("paticent weight: "))
            sex = input("paticent sex: ")
            
# Use the current paticent name an apponitment slot save the object
            appointment = Appointment(doc_name, name, phno,  height, weight, sex)
            frozen = jsonpickle.encode(appointment)
            with open('medicaldatabase.txt', 'w') as j_out:
                print(frozen, file=j_out)
            Medical_ledger[name] = appointment
            print(Medical_ledger)
        

                
        elif ch == 2:
            #If user choice is 2 (int) - perform consuluting docter,get the description and prescription operation
            # get the paticent name
            name = input(" paticent Name: ").upper()
            #storing the names of the paticent into a list
            Visit_doc_paticent_name.append(name)
            #cheaking that the patcient has taken an appointment
            if name in Medical_ledger.keys():
                appointment.discription()
            else:
                print("Please get the Appointment")   
           
        elif ch == 3:
            #If user choice is 3 (int) - creating the medical certificate 
            # get the paticent name
            name = input(" paticent Name: ").upper()
            # cheaking that the patcient has consulted the docter
            if name in Visit_doc_paticent_name:
                appointment = Medical_ledger[name]
                appointment.get_medical_report()
            else:
                print("Please get an appointment and consult the Doctor")   
                    

        else:
            # Exit the loop if input is invalid
            break
