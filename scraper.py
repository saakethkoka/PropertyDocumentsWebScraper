from selenium import webdriver
import time
import csv
my_url = 'https://denton.tx.publicsearch.us/results?_docTypes=AB&department=RP&limit=250&offset=0&recordedDateRange=18510326%2C20210507&searchOcrText=false&searchType=quickSearch'
driver = webdriver.Chrome('/Users/saakethkoka/Documents/Dev/WebScraping/chromedriver')
driver.get(my_url)
with open('data.csv', 'w', newline='') as f:
    the_writer = csv.writer(f)
    the_writer.writerow(['Grantor', 'Recorded Date', 'Doc Number'])
    while True:
        p_element = driver.find_element_by_class_name('a11y-table').find_element_by_tag_name(
            'table').find_element_by_tag_name('tbody')
        list = p_element.find_elements_by_tag_name('tr')
        for item in list:
            the_writer.writerow([item.find_element_by_class_name('col-3').text,
                                 item.find_element_by_class_name('col-6').text,
                                item.find_element_by_class_name("col-7").text])

        button_list = driver.find_elements_by_class_name('pagination__page-jump')
        if(button_list[1].get_attribute('aria-disabled') == 'true'):
            break
        button_list[1].click()
        time.sleep(2)

driver.close()





