from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video= self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()






