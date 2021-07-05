# PROGRAM : EMAIL SCRAPPING FROM WEBSITES
# WRITTEN BY : SUMAN GANGOPADHYAY
# EMAIL ID : linuxgurusuman@gmail.com
# DATE : 5-July-2021
# PROGRAMMING LANGUAGE : Python (3.9.1)
# CAVEATS : None

import re
from urllib.request import urlopen

class Suman_Web_Scrapper:
    """The Python Class for Web Scrapping Developed by Suman Gangopadhyay"""
    email_regex = "(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})"
    mobile_regex = "^[987]\d{9}$"
    
    def __init__(self, url):
        self.url = url
        self.data = urlopen(self.url).read().decode("utf-8")

    # The Email scrapping method
    def Email_Scrapper(self):
        email_result = ""
        final_list = []
        email_result = re.findall(self.email_regex, self.data)        
        #Removal of Duplicate Emails from the Final EMail List
        for email in email_result:
            if email not in final_list:
                final_list.append(email)
        return final_list 

    # The Indian Mobile scrapping method
    def Indian_Mobile_Number_Scrapper(self):              
        tmp =[]
        result = []
        tmp = list(self.data.split(" ")) 
        for i in tmp:            
            if(re.findall(self.mobile_regex, i)):
                result.append(i[:10])
        return result

data1 = "https://indusdictum.com/contact/"
data2 = "https://www.signalhire.com/companies/cnn"
data3 = "https://notionpress.com/contact"
data4 = "https://rekhtadictionary.com/contact-us?lang=hi"

print(Suman_Web_Scrapper(data1).Email_Scrapper())
print()
print(Suman_Web_Scrapper(data2).Email_Scrapper())
print()
print(Suman_Web_Scrapper(data3).Email_Scrapper())
print()
print(Suman_Web_Scrapper(data4).Email_Scrapper())