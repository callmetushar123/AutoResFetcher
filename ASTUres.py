from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os.path


#year =Select(driver.find_element_by_xpath("//*[@id='txtRoll']"))
#s= input("Enter the Semester-1,2,3 ")
class auto:
    def __init__(self, rollno, sem, db, y):
        self.rollno = rollno
        self.sem = sem
        self.db = db
        self.y =  y

    def result(self):
        driver = webdriver.Chrome(executable_path=r"C:/Users/Tushar/Desktop/chromedriver.exe")

        driver.get("https://www.astuonline.in/studentresult.aspx")

        year =Select(driver.find_element_by_id("ddYear"))
        year.select_by_value(self.y)

        sem = Select(driver.find_element_by_id("ddSem"))
        sem.select_by_value(self.sem)

        type = Select(driver.find_element_by_id("ddType"))
        type.select_by_value("Regular")

        dob = driver.find_element_by_id("txtDob")
        dob.send_keys(self.db)

        roll = driver.find_element_by_id("txtRoll")
        roll.send_keys(self.rollno)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(10)


#print("Enter the required fields")
d = {'roll':None, 'sem':None, 'dob':None, 'year':None}

v = os.path.isfile("res.dll")
if v == True:
    h=open("res.dll", "r")
    if h.mode == "r":
        contents = h.read()
        p = contents.split("\t")
        for line,key in zip(p,d):
            d[key] = line
    a = auto(d['roll'], d['sem'], d['dob'], d['year'])
    a.result()
else:
    roll, sem, dob, year = input("Enter rollno, Semester, DOB, Year").split()
#input(roll, sem, dob, year)
    f= open("res.dll", "w+")
    f.write("%s\t" % roll)
    f.write("%s\t" % sem)
    f.write("%s\t" % dob)
    f.write("%s\t" %year)
    f.close()
    a = auto(roll, sem, dob ,year)
    a.result()
#print(d["roll"])
#a =auto("170610007033", "3", "13/02/1998", "2018")






















































'''
'''
'''def First():

    driver = webdriver.Chrome(executable_path=r"C:/Users/Tushar/Desktop/chromedriver.exe")

    driver.get("https://www.astuonline.in/studentresult.aspx")

    year =Select(driver.find_element_by_id("ddYear"))

    year.select_by_value('2018')

    sem = Select(driver.find_element_by_id("ddSem"))
    sem.select_by_value('1')

    type = Select(driver.find_element_by_id("ddType"))
    type.select_by_value("Regular")

    dob = driver.find_element_by_id("txtDob")
    dob.send_keys("13/02/1998")

    roll = driver.find_element_by_id("txtRoll")
    roll.send_keys("170610000033")
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(10)

def second():

    driver = webdriver.Chrome(executable_path=r"C:/Users/Tushar/Desktop/chromedriver.exe")

    driver.get("https://www.astuonline.in/studentresult.aspx")

    year =Select(driver.find_element_by_id("ddYear"))

    year.select_by_value('2018')

    sem = Select(driver.find_element_by_id("ddSem"))
    sem.select_by_value('2')

    type = Select(driver.find_element_by_id("ddType"))
    type.select_by_value("Regular")

    dob = driver.find_element_by_id("txtDob")
    dob.send_keys("13/02/1998")

    roll = driver.find_element_by_id("txtRoll")
    roll.send_keys("170610007018")
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(10)

def third():

    driver = webdriver.Chrome(executable_path=r"C:/Users/Tushar/Desktop/chromedriver.exe")

    driver.get("https://www.astuonline.in/studentresult.aspx")

    year =Select(driver.find_element_by_id("ddYear"))

    year.select_by_value('2019')

    sem = Select(driver.find_element_by_id("ddSem"))
    sem.select_by_value('3')

    type = Select(driver.find_element_by_id("ddType"))
    type.select_by_value("Regular")

    dob = driver.find_element_by_id("txtDob")
    dob.send_keys("13/02/1998")

    roll = driver.find_element_by_id("txtRoll")
    roll.send_keys("170610007033")
    driver.find_element_by_id("btnSubmit").click()
    time.sleep(10)


if s == '1':
    First()
elif s == '2':
    second()
elif s== '3':
    third()
else :
    print("Wrong input")
'''

#driver.find_element_by_id("btnSubmit").click()
