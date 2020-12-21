from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\rohit\\Documents\\chromedriver.exe")
driver.get('https://www.practically.com')
clicker = driver.find_element_by_xpath('//*[@id="offerModal"]')
clicker.click()
driver.quit('https://play.google.com/store/apps/details?id=com.thirdflix.practically&_branch_match_id=855399840502822675&utm_medium=marketing')
