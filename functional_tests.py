from selenium import webdriver

#Edith has heard about a cool new online to-do app
#She goes to check out its homepage
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title