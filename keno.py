from selenium import webdriver
import time
# Options chrome
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")
    # driver_chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')
# End Options chrome

# Options firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--private")
driver_firefox = webdriver.Firefox(firefox_options=firefox_options, executable_path='./geckodriver')
# End Options firefox
url = "https://www.minhchinh.com/xo-so-dien-toan-keno.html"
driver_firefox.get(url)
time.sleep(10)
for i in range(3000):
    print('Loading page  : ',i+1)
    path_click = './/a[@href="javascript:chosePage('+str(i + 1)+')"]'
    print(path_click)
    try:
        click_button = driver_firefox.find_element_by_xpath(path_click)
        click_button.click()
    finally:
        elements = driver_firefox.find_elements_by_css_selector(".wrapperKQKeno")
        list_data = [str(el.text).replace('\n', ' ') for el in elements]
        with open('lab.txt', 'a') as f:
            f.write(str(list_data))
            f.write('\n')
        time.sleep(10)