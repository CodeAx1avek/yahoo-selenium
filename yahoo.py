# Yahoo automation @CodeAx1
from selenium import webdriver
import time
import pyfiglet
print("-"*100)
# email = input("Enter Your Email id: ")
# passwdq = input("Enter Your Password : ")
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(R+br)
print(B+"We Are here To Automate the Software with our pc")
print(B+'The loading content can be change with your clicking any button')
print(B+"Please wait till anything load")
print(B+"Check terminal if error occurs")
nummail = int(input(Y+"Enter how many mail want to do :"))
print("-"*100)



driver = webdriver.Chrome("C:\Selenium And Appium\chromedriver_win32\chromedriver.exe")
driver.get("https://login.yahoo.com/?.intl=in&rl=1&.src=ym")

user_name = driver.find_element("xpath",'//*[@id="login-username"]')
user_name.send_keys("lazenbygrace@yahoo.com")    #faustino_brennan@yahoo.com  #carl_engstrom@yahoo.com #irenegoodman358@yahoo.com

driver.find_element("xpath",'//*[@id="login-signin"]').click()

time.sleep(2)
user_passwd = driver.find_element("xpath",'//*[@id="login-passwd"]')  
user_passwd.send_keys("iop890890")   #Askme@123
driver.find_element("xpath",'//*[@id="login-signin"]').click()
time.sleep(1)
driver.find_element("xpath",'//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[1]/ul/li[7]').click()   #spamm button inbox
try:
    driver.find_element("xpath",'//*[@id="app"]/div[7]/div/div[1]/div/div[2]/div/button[2]').click() #calender error only first time comes
except:
    print("A")
for i in range(nummail):
    time.sleep(3)
    try:
        driver.find_element("xpath",'//*[@id="mail-app-component"]/div/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li[2]').click() #show email in spam
    except:
        driver.find_element("xpath",'//*[@id="mail-app-component"]/div/div/div/div[2]/div/div/div[3]/div/div[1]/ul/li[3]').click() #show email in spam
    time.sleep(3)
    try:
        driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li/div/div[2]/div[1]/div[1]/div/div/span[2]/button/span/span').click() #show image
        time.sleep(3)
    except:
        pass
    time.sleep(2)
    driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[4]/div/button/span/span/span').click()          #not spam button
