# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

value=pd.read_csv(path)
data=pd.DataFrame(value)

plt.figure(figsize=[14,8])
plt.xlabel("Status of Loan Approval")
plt.ylabel("No of Loan Approved")
# title the plot
plt.title("Loan Status for Customer Approved/Not - Approved")
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
plt.show()

#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby([data['Property_Area'],data['Loan_Status']])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here
education_and_loan= data.groupby([data['Education'],data['Loan_Status']])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(stacked=False, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# --------------
#Code starts here



graduate=pd.DataFrame(data[data['Education'] == 'Graduate'])
not_graduate=pd.DataFrame(data[data['Education'] == 'Not Graduate'])
#print(data[data['Education'] == 'Graduate']['LoanAmount'])
#data[data['Education'] == 'Graduate']['LoanAmount'].Series.plot(kind='density',label='Graduate')

data[data['Education'] == 'Graduate']['LoanAmount'].plot(kind='density',label='Graduate')
data[data['Education'] == 'Not Graduate']['LoanAmount'].plot(kind='density',label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(20,10))
ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'], c='Red')
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'], c='Green')
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'], data['LoanAmount'], c='Blue')
ax_3.set_title('Total Income')


