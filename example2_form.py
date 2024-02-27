import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# create browser variable and assign it to an instance of Chrome browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# Navigate to SoundRise website
browser.get('http://ec2-35-77-8-202.ap-northeast-1.compute.amazonaws.com/')
# Print current page Title
print(browser.title)
# Print current page URL
print(browser.current_url)
# wait for 2 seconds before closing the browser
time.sleep(2)
# find element on the page by text on the link which is "Artists" and click on it
browser.find_element(By.LINK_TEXT, 'CONTACT').click()
time.sleep(2)
# Print current page Title
print(browser.title)
# assert 'Artists Grid – Fullwidth – IT Simple' == browser.title
# assert 'Artists' in browser.title
# Print current page URL
print(browser.current_url)
# assert 'http://ec2-35-77-8-202.ap-northeast-1.compute.amazonaws.com/artists/artists-grid-fullwidth/' == browser.current_url
# assert 'artists' in browser.current_url
browser.find_element(By.NAME, "your-name").send_keys('Yury')
time.sleep(2)
browser.find_element(By.NAME, "your-email").send_keys("yuriy@gmail.com")
time.sleep(2)
browser.find_element(By.NAME, "your-subject").send_keys("I want to contact your label")
time.sleep(2)
browser.find_element(By.NAME, "your-message").send_keys("My message")
time.sleep(2)
browser.find_element(By.XPATH, "//input[@value='Send']").click()
time.sleep(2)
# full or absolute xpath /
# /html/body/div[2]/ul/li[2]/a

# xpath or relative xpath, it's showing where to find element from specific place in your website
# //*[@id="menu-item-1397"]/a