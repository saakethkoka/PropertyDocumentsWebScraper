from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

class scraper:
    my_url = 'https://denton.tx.publicsearch.us/results?department=RP&limit=250&offset=100&recordedDateRange=18510326%2C20210507&searchOcrText=false&searchType=quickSearch'
    driver = webdriver.Chrome('/Users/saakethkoka/Documents/Dev/WebScraping/chromedriver')
    driver.get(my_url)
    time.sleep(2)

    def set_document_filter(self, filter_name):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tour-filter')))
        filter_name = filter_name.upper()
        filter_container = scraper.driver.find_element_by_class_name('tour-filter')
        filter_container = filter_container.find_element_by_class_name('filter__content')

        search_box = filter_container.find_element_by_class_name('react-tokenized-select__token-wrap-container')
        search_box = search_box.find_element_by_class_name('react-tokenized-select__input')
        search_box.clear()
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

    def scrape_data(self, file_name, print_status):
        total_docs_to_parse = self.get_num_docs()
        num_docs_parsed = 0
        start_time = time.time()
        with open(file_name, mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['Grantor', 'Grantee', 'Doc Type', 'Recorded Date', 'Doc Number',
                             'Book/Volume/Page', 'Legal Description', 'Lot', 'Block'])
            while True:
                if (print_status and num_docs_parsed > 0):
                    print('Estimated Time Remaining: ',
                          (total_docs_to_parse - num_docs_parsed) / (num_docs_parsed / (time.time() - start_time)), 'Seconds')
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'a11y-table')))
                p_element = self.driver.find_element_by_class_name('a11y-table').find_element_by_tag_name(
                    'table').find_element_by_tag_name('tbody')
                list = p_element.find_elements_by_tag_name('tr')
                for item in list:
                    writer.writerow([item.find_element_by_class_name('col-3').text,
                                     item.find_element_by_class_name('col-4').text,
                                     item.find_element_by_class_name('col-5').text,
                                     item.find_element_by_class_name('col-6').text,
                                     item.find_element_by_class_name('col-7').text,
                                     item.find_element_by_class_name('col-8').text,
                                     item.find_element_by_class_name('col-9').text,
                                     item.find_element_by_class_name('col-10').text,
                                     item.find_element_by_class_name('col-11').text])
                    num_docs_parsed = num_docs_parsed + 1

                button_list = self.driver.find_elements_by_class_name('pagination__page-jump')
                if (button_list[1].get_attribute('aria-disabled') == 'true'):
                    break
                button_list[1].click()

    def close_driver(self):
        self.driver.close()

    def get_num_docs(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-results-header__left-wrap')))
        search_results_summary = self.driver.find_element_by_class_name('search-results')\
            .find_element_by_class_name('search-results-header__left-wrap')
        list = search_results_summary.text.partition('\n')
        text_line = list[2]
        num_docs = text_line.partition(' ')
        return int(num_docs[2].partition('\n')[0].partition(' ')[0].replace(',', ''))









