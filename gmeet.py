
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
import time
    
edge_options = EdgeOptions()
edge_options.use_chromium = True
#deny the permission
edge_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })
 
#Here you set the path of the profile ending with User Data not the profile folder
#edge_options.add_argument(r"C:\Users\sakth\AppData\Local\Microsoft\Edge\User Data"); 




browser = Edge(options = edge_options, executable_path = r"D:/msedgedriver.exe")

# add the meet link here and username & password
site =( "https://gmail.com")
meet = ("enter the meet link")
username = "Enter_your_Email"
password = "Enter_your_password"


#open gmail and logins
browser.get(site);
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(username)
browser.find_element_by_class_name("VfPpkd-RLmnJb").click();

time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
browser.find_element_by_class_name("VfPpkd-RLmnJb").click();

#open new tab to join meetlink
time.sleep(3)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get(meet)

#dimiss the popup
time.sleep(5)
browser.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span").click();


# join the class
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()

#By Alchemist