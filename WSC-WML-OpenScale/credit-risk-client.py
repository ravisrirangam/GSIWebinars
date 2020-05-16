#!/usr/bin/env python
# coding: utf-8

# Sample Client for invoking Scoring Endpoint in Python
# 

# Get the IAM toen using the WML credentials

# In[1]:


import requests

# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
apikey = "UBkwDf3BBnLwZWJ84S3pPVFM5AuHYI-j9rLzbe0_02BQ"

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
print(iam_token)


# Invoke the Scoring endpoint, using the credit risk example

# In[2]:


import urllib3, requests, json

ml_instance_id = "017357e3-af97-414a-99d4-380b86b81a2e"

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {
"fields": ["CheckingStatus","LoanDuration","CreditHistory","LoanPurpose","LoanAmount","ExistingSavings","EmploymentDuration","InstallmentPercent","Sex","OthersOnLoan","CurrentResidenceDuration","OwnsProperty","Age","InstallmentPlans","Housing","ExistingCreditsCount","Job","Dependents","Telephone","ForeignWorker"],
  "values": [["less_0",6,"outstanding_credit","radio_tv",1169,"unknown","greater_7",4,"male","none",4,"real_estate",67,"none","own",2,"skilled",1,"yes","yes","No Risk"  ]]
  }

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/017357e3-af97-414a-99d4-380b86b81a2e/deployments/00ff0df2-7add-41da-a113-6e82145643e2/online', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))


# In[ ]:




