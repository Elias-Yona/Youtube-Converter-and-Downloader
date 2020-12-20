from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class ConverterDownloader:
    def __init__(self, youtube_url, format):
        self.youtube_url = youtube_url
        self.format = format

    driver = webdriver.Chrome("C:\Python\chromedriver.exe")

    #open ytmp3.com
    def open_link(self):
        self.driver.get("https://ytmp3.cc/en13/")
        

    #Perform a clicking action on the shown buttons
    def button_clicks(self):
        url = self.driver.find_element_by_name ('video')
        btn = self.driver.find_element_by_id ('submit')

        def convert():
            url.send_keys(self.youtube_url)
            sleep(2)
            actions = webdriver.common.action_chains.ActionChains(self.driver)
            actions.click(btn)
            actions.perform()
            sleep(2)

        convert()

        def media_format():
            frt = self.driver.find_element_by_id(self.format)
            actions = webdriver.common.action_chains.ActionChains(self.driver)
            actions.click(frt)
            actions.perform()
            sleep(0.5)

        media_format()

        def download():
            #check for download link
            download_link = self.driver.find_element_by_css_selector('a[href*="."]')
            actions = webdriver.common.action_chains.ActionChains(self.driver)
            actions.click(download_link)
            actions.perform()  

        download()
        # driver.close()


if __name__ == "__main__":
    media = ConverterDownloader('https://www.youtube.com/watch?v=cXmscjras9o', 'mp3')
    media.open_link()
    media.button_clicks() 
