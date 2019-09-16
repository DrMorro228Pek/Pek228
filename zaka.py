from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

target_server_1 = "https://zaka-zaka.com/game/gifts/random-steam/"
target_server_2 = "https://zaka-zaka.com/game/gifts/good-game/"
target_server_3 = "https://zaka-zaka.com/game/gifts/coupons"
target_server_4 = "https://zaka-zaka.com/game/gifts/skins-random"

def click(link):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    
    driver.get(link)

    driver.add_cookie({'name' : '6f61a6f73492e7d3f30c772dd02c16e0', 'value' : '57fd186e8dd0c581546107e0c8ef4b1cb90bd31fs%3A169%3A%221e9056f8c029ef1533619084fa50099b85209f37a%3A4%3A%7Bi%3A0%3Bs%3A6%3A%22266871%22%3Bi%3A1%3Bs%3A22%3A%22sergey.igymn%40gmail.com%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A2%3A%7Bs%3A5%3A%22login%22%3Bs%3A7%3A%22%23266871%22%3Bs%3A2%3A%22id%22%3Bs%3A6%3A%22266871%22%3B%7D%7D%22%3B'})
    driver.add_cookie({'name' : 'PHPSESSID', 'value' : 'mufiujku5magn6vljpcgso75npeutf2o'})
    driver.add_cookie({'name' : '__cfduid', 'value' : 'd7400db8aa0b4662347f07ffd873e35631560574970'})
    driver.add_cookie({'name' : '_ga', 'value' : 'GA1.2.1968617286.1560574975'})
    driver.add_cookie({'name' : '_gid', 'value' : 'GA1.2.1217770604.1568374795'})
    driver.add_cookie({'name' : '_ym_d', 'value' : '1560574975'})
    driver.add_cookie({'name' : '_ym_uid', 'value' : '1560574975843231290'})
    driver.add_cookie({'name' : 'agent_id', 'value' : 'ef1ff8ecb2ce746c415ac27590bf8dc33630e3e5'})
    driver.add_cookie({'name' : 'disclaimer', 'value' : '1568485539310'})
    
    driver.get(link)    

    try:
        element = driver.find_element_by_id("gift_confirm")
        element.click()

    except:
        pass
    
    driver.quit()

while True:
   
    
    click(target_server_1)
    click(target_server_2)
    click(target_server_3)
    click(target_server_4)

    
    time.sleep(43200)
