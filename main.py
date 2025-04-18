from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium, time, pyautogui

service = webdriver.chrome.service.Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)
time.sleep(0.5)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
time.sleep(0.25)
driver.get(f'https://10fastfingers.com/typing-test/{input("Enter lang: ")}')

input('[!] Start? (just "Enter"): ')

time.sleep(0.1)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
time.sleep(0.1)
wait = WebDriverWait(driver, 3)
span_container_xpath = "/html/body/div[4]/div/div[4]/div/div[1]/div[7]/div[1]/div"
wait.until(webdriver.support.expected_conditions.presence_of_element_located((By.XPATH, span_container_xpath)))

span_container = driver.find_element(By.XPATH, span_container_xpath)
all_spans = span_container.find_elements(By.TAG_NAME, "span")
total_spans = len(all_spans)
print(f"[info] Totally {total_spans} words finded.")

textbox_xpath = "/html/body/div[4]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input"
textbox = driver.find_element(By.XPATH, textbox_xpath)
textbox.click()

for i in range(total_spans):
    try:
        word = all_spans[i].text.strip()
        if word:
            textbox.send_keys(word)
            textbox.send_keys(webdriver.common.keys.Keys.SPACE)
    except Exception as e:
        print("[Error!]", e)

waiting = float(0.1)
time.sleep(2)
textbox.send_keys("                                                                                                                                                                     ")
for i in "Yes we finished :) good boy. Now i hack your pc wait 1 min ...":
        textbox.send_keys(i)
        time.sleep(waiting)
        waiting+=0.005
input()
