#Creating a python file having selenium code in it 

#Considering we have a login page having username password and full name of the user

#import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  


#creating driver instance to get the path
Mydriver = webdriver.Chrome(executable_path='')

# Navigating to the login page of the web application project
# index.html has our html code for the web login page 
Mydriver.get("http://127.0.0.1:5500/index.html")  

#fetch the details/inputs entered by the user in our case it's full name, username and password
fullname_field=Mydriver.find_element_by_id("fullname")
username_field = Mydriver.find_element_by_id("username") 
password_field = Mydriver.find_element_by_id("password") 

login_button = Mydriver.find_element_by_id("button")

# Enter your login credentials (replace with actual credentials)
fullname_field.send_keys("name")
username_field.send_keys("username")
password_field.send_keys("password")

# Click the login button to submit the form
login_button.click()

# Wait for a few seconds to allow the login to complete
Mydriver.implicitly_wait(6)

#last step will be to check title of the next page to verify if login was successful
#Considering out redirection page title is "Homepage"
if "Homepage" in Mydriver.title: 
    print("Successful login!")
else:
    print("Login failed! ")


Mydriver.close()
