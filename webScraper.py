from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import DocObject

class WebScraper:
    my_url = 'https://denton.tx.publicsearch.us/results?department=RP&limit=250&offset=100&recordedDateRange=18510326%2C20210507&searchOcrText=false&searchType=quickSearch'
    driver = webdriver.Chrome('/Users/saakethkoka/Documents/Dev/WebScraping/chromedriver')
    driver.get(my_url)

    def set_document_filter(self, filter_name):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tour-filter')))
        filter_name = filter_name.upper()
        filter_container = WebScraper.driver.find_element_by_class_name('tour-filter')
        filter_container = filter_container.find_element_by_class_name('filter__content')

        search_box = filter_container.find_element_by_class_name('react-tokenized-select__token-wrap-container')
        search_box = search_box.find_element_by_class_name('react-tokenized-select__input')
        search_box.send_keys(filter_name) # Sends filter to search box

        try: # Checks to see if filter exists by checking if search box returned anything
            filter_list = filter_container.find_elements_by_class_name('tokenized-nested-select__item')
        except:
            raise ValueError('Filter not found')

        filter_exists = False
        for item in filter_list:
            if item.text.partition('\n')[0] == filter_name:
                filter = item.find_element_by_tag_name('label')
                filter_exists = True
                break

        if not filter_exists:
            raise ValueError('Filter not found')

        try: # Attempts to click to wake up web page and then clicks to select filter
            filter.click()
        except:
            filter.click()
        


    def get_document_objects(self):
        doc = DocObject.DocOject('me', 'you')
        doc_list = []
        while True:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'a11y-table')))
            p_element = self.driver.find_element_by_class_name('a11y-table').find_element_by_tag_name(
                'table').find_element_by_tag_name('tbody')
            list = p_element.find_elements_by_tag_name('tr')
            for item in list:
                doc = DocObject.DocOject(item.find_element_by_class_name('col-3').text, item.find_element_by_class_name('col-4').text)
                doc_list.append(doc)

            button_list = self.driver.find_elements_by_class_name('pagination__page-jump')
            if(button_list[1].get_attribute('aria-disabled') == 'true'):
                break
            button_list[1].click()
        return doc_list

    def close_driver(self):
        self.driver.close()








