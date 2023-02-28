import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection  import GridSearchCV
import pickle
import json

class LoanPrediction():
    def __init__(self,Gender,Married,Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea):
        self.Gender = Gender
        self.Married = Married
        self.Dependents = Dependents
        self.Education = Education
        self.SelfEmployed = SelfEmployed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.LoanAmountTerm = LoanAmountTerm
        self.CreditHistory = CreditHistory
        self.PropertyArea = PropertyArea
        return
    def load_model(self):
        with open('artifacts/rf_model_cls_.pickle','rb') as fp:
            self.model = pickle.load(fp)
        with open('artifacts/project_data_rf_cls.json') as fp1:
            self.project_data = json.load(fp1)
    def get_status(self):
        self.load_model()
        test_array = np.zeros(self.model.n_features_in_)
        test_array[0] = self.project_data['Gender'][self.Gender]
        test_array[1] = self.project_data['Married'][self.Married]
        test_array[2] = self.Dependents
        test_array[3] = self.project_data['Education'][self.Education]
        test_array[4] = self.project_data['SelfEmployed'][self.SelfEmployed]
        test_array[5] = self.ApplicantIncome
        test_array[6] = self.CoapplicantIncome
        test_array[7] = self.LoanAmount
        test_array[8] = self.LoanAmountTerm
        test_array[9] = self.CreditHistory
        area = 'PropertyArea_' + self.PropertyArea
        index = self.project_data['Column Name'].index(area)
        test_array[index] = 1
        predict_loan = self.model.predict([test_array])[0]
        return predict_loan