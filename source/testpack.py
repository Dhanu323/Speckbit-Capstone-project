from tabulate import tabulate
from datetime import datetime
import json
"""
Health Care Management Module
Authors:
    Dhanush Rao H S
"""
class Appointment:
    """
    General Appointment Class for a paticent
    """
    

    def __init__(self,doc_name,name,phone,height,weight,sex):
        """
        Constructor function for the Appointment Class
        Executed by interpreter to create an instance of this class.
        Attributes:
            self.doc_name -- name of the docter who will be treating the patcient (str)
            self.name -- name of the patcient (str)
            self.phno -- phone number of the patcient (int) 
            self.heigth -- height of the patcient (float)
            self.body_weigth -- body weight of the patcient (float)
            self.sex -- sex of the patcient (str)
            self.datetime -- Date and time of the Appointment 
        """
        self.doc_name = doc_name
        self.name = name
        self.phno = phone
        self.height = height
        self.body_weight = weight
        self.sex = sex
        self.datetime = datetime.now()
        self.prescription = {}
       
    def discription(self):
        '''
        gets the description and presciption

        '''
        self.description = input("Enter the description: ")
        # enter the total number of medicine like total no of total tablets number
        self.no = int(input("Enter the prescription quantity: "))
        
            
        for i in range(self.no):
            self.medic_name = input("Enter medicin: ")
            self.medic_quantity = int(input("Enter quantity : "))
            self.prescription[self.medic_name] = self.medic_quantity

    def get_medical_report(self):
        '''
        genrates the medical certificate for the respected pat
        '''
        print("-"*50)
        print("\t\t\t\t\t\tSpeckbit Health Care Center")
        table = self.prescription.items()
        print("Docter Name",self.doc_name,"Date time:",self.datetime,"paticent name: ",self.name,"paticent phone number :",self.phno, "paticent height in Kg :",self.height,"paticent weight :",self.body_weight ,"paticent sex:",self.sex ,sep="\n")
        print(tabulate(table, headers=["Medicen","Quantity","consume_timeing"],tablefmt="rst"))
        print("_"*50)
        

    def __json__(self):
        return dict(doc_name=self.doc_name,name=self.name,phone= self.phno,height =self.height,weight=self.body_weight,sex=self.sex,date = self.datetime,description=self.description,prescription=self.prescription)
