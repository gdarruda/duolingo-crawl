from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = False

browser = Firefox(options=opts)
browser.get('https://www.duolingo.com')

results = browser.find_elements_by_xpath('//a[@class="_3mSsk _2AkYE _1figt whuSQ _2gwtT _1nlVc _2fOC9 t5wFJ _3dtSu _25Cnc _3yAjN UCrz7 yTpGk _2QOX5"]')

if len(results) == 0:
	raise "Não encontrou botão de login!"

results[0].click()

results = browser.find_elements_by_xpath('//input[@data-test="email-input"]')

if len(results) == 0:
	raise "Não encontrou email!"

results[0].send_keys("student.duo01@gmail.com")


results = browser.find_elements_by_xpath('//input[@data-test="password-input"]')

if len(results) == 0:
	raise "Não encontrou password!"

results[0].send_keys("Estudante01")


results = browser.find_elements_by_xpath('//button[@data-test="register-button"]')

if len(results) == 0:
	raise "Não encontrou botão!"

results[0].click()    