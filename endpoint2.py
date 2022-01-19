import requests
import json

# URL for the web service, should be similar to:
# 'http://13a2d52c-6ace-4dd4-806d-b89b7f16de6a.southcentralus.azurecontainer.io/score'
scoring_uri = 'http://13a2d52c-6ace-4dd4-806d-b89b7f16de6a.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '80hhu20gx1ymUobSXKN8QQnEbc9MxUc0'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 17,
	    "job": "blue-collar",
	    "marital": "married",
	    "education": "university.degree",
            "default": "no",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "month": "may",
            "day_of_week": "mon",
            "duration": 971,
            "campaign": 1,
            "pdays": 999,
            "previous": 1,
            "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "euribor3m": 1.299,
            "nr.employed": 5099.1
          },
          {
            "age": 87,
	    "job": "blue-collar",
	    "marital": "married",
	    "education": "university.degree",
            "default": "no",
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "month": "may",
            "day_of_week": "mon",
            "duration": 471,
            "campaign": 1,
            "pdays": 999,
            "previous": 1,
            "poutcome": "failure",
            "emp.var.rate": -1.8,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "euribor3m": 1.299,
            "nr.employed": 5099.1
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


