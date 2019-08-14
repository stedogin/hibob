# https://apidocs.hibob.com/reference

import requests
import json

# read company people
url = "https://api.hibob.com/v1/people"
querystring = {"showInactive":"true"}
response = requests.request("GET", url, params=querystring)
print(response.text)


# get company users by id/email
url = "https://api.hibob.com/v1/people/123%40dgdfsg.com"
response = requests.request("GET", url)
print(response.text)


# get public user profile
url = "https://api.hibob.com/v1/profiles"
querystring = {"sortBy":"firstName"}
response = requests.request("GET", url, params=querystring)
print(response.text)


# get employee avatar
url = "https://api.hibob.com/v1/avatars"
querystring = {"email":"yoav@domain.com"}
response = requests.request("GET", url, params=querystring)
print(response.text)

url = "https://api.hibob.com/v1/avatars/123"
response = requests.request("GET", url)
print(response.text)

url = "https://api.hibob.com/v1/my/avatar"
response = requests.request("GET", url)
print(response.text)


# update email
url = "https://api.hibob.com/v1/people/123/email"
payload = "{\"email\":\"yoav@domain.com\"}"
response = requests.request("PUT", url, data=payload)
print(response.text)


# get work history
url = "https://api.hibob.com/v1/people/123/work"
response = requests.request("GET", url)
print(response.text)


# new work entry for employee
url = "https://api.hibob.com/v1/people/123/work"
response = requests.request("POST", url)
print(response.text)


# delete work entry
url = "https://api.hibob.com/v1/people/132/work/456"
response = requests.request("DELETE", url)
print(response.text)


# update work entry
url = "https://api.hibob.com/v1/people/id/work/entry_id"
response = requests.request("PUT", url)
print(response.text)


# salary history
url = "https://api.hibob.com/v1/people/123/salaries"
response = requests.request("GET", url)
print(response.text)


# add new salary entry
url = "https://api.hibob.com/v1/people/id/salaries"
response = requests.request("POST", url)
print(response.text)


# delete salary entry
url = "https://api.hibob.com/v1/people/123/salaries/456"
response = requests.request("DELETE", url)
print(response.text)


# get equity
url = "https://api.hibob.com/v1/people/id/equities"
response = requests.request("GET", url)
print(response.text)


# create equity
url = "https://api.hibob.com/v1/people/id/equities"
response = requests.request("POST", url)
print(response.text)


# delete equity
url = "https://api.hibob.com/v1/people/id/equities/entry_id"
response = requests.request("DELETE", url)
print(response.text)


# company reports
url = "https://api.hibob.com/v1/company/reports"
response = requests.request("GET", url)
print(response.text)


# download report
url = "https://api.hibob.com/v1/company/reports/:reportId/download"
querystring = {"reportId":"123","format":"csv","includeInfo":"true"}
response = requests.request("GET", url, params=querystring)
print(response.text)


# open tasks
url = "https://api.hibob.com/v1/tasks"
response = requests.request("GET", url)
print(response.text)


# my tasks
url = "https://api.hibob.com/v1/my/tasks"
response = requests.request("GET", url)
print(response.text)


# get time off info
url = "https://api.hibob.com/v1/timeoff/employees/123/requests/456"
response = requests.request("GET", url)
print(response.text)


# get new time off requests since date
url = "https://api.hibob.com/v1/timeoff/requests/changes"
querystring = {"since":"2007-04-05T14:30:24.345Z / 2007-04-05T12:30-02:00"}
response = requests.request("GET", url, params=querystring)
print(response.text)


# who's out of office
url = "https://api.hibob.com/v1/timeoff/whosout"
querystring = {"from":"from","to":"to"}
response = requests.request("GET", url, params=querystring)
print(response.text)

url = "https://api.hibob.com/v1/timeoff/outtoday"
querystring = {"today":"2018-09-09"} # remove for just today
response = requests.request("GET", url, params=querystring)
print(response.text)


# payroll
url = "https://api.hibob.com/v1/payroll/history"
querystring = {"department":"departmentname","showInactive":"true"}
response = requests.request("GET", url, params=querystring)
print(response.text)


# documents
url = "https://api.hibob.com/v1/docs/people/id"
response = requests.request("GET", url)
print(response.text)

url = "https://api.hibob.com/v1/docs/people/123/confidential"  # replace with shared for other type
payload = "{\"tags\":[\"tag\",\"tag2\"],\"documentName\":\"name\",\"documentUrl\":\"url\"}"
response = requests.request("POST", url, data=payload)
print(response.text)


