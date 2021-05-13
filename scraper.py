import time
import csv
from webScraper import WebScraper


start_time = time.time()
scraper = WebScraper()
scraper.set_document_filter('ABANDONMENT OF ASSUMED NAME')
list = scraper.get_document_objects()
for item in list:
    item.print_object()

time_to_run = time.time() - start_time
print("Run Time: ")
print(time_to_run)




# my_url = 'https://denton.tx.publicsearch.us/results?_docTypes=AB&department=RP&limit=250&offset=0&recordedDateRange=18510326%2C20210507&searchOcrText=false&searchType=quickSearch'
# driver = webdriver.Chrome('/Users/saakethkoka/Documents/Dev/WebScraping/chromedriver')
# driver.get(my_url)
# time.sleep(2)
# filter_element = driver.find_element_by_class_name('ReactVirtualized__Grid__innerScrollContainer')
# filter_element.find_elements_by_class_name('tokenized-nested-select__button')[3].find_element_by_class_name('icon--small').click() #opening filter
# time.sleep(2)
# # After Click
# filter_element = driver.find_element_by_class_name('ReactVirtualized__Grid__innerScrollContainer')
# first_filter = filter_element.find_element_by_class_name('tokenized-nested-select__item')
#
# element_to_scroll_to = first_filter.click()
# scroll_window = driver.find_element_by_class_name('ReactVirtualized__Grid__innerScrollContainer')
# filter_list = filter_element.find_elements_by_class_name('tokenized-nested-select__item')
#
# filter_container = driver.find_element_by_class_name('tour-filter')
# filter_container = filter_container.find_element_by_class_name('filter__content')
#
#
# search_box = filter_container.find_element_by_class_name('react-tokenized-select__token-wrap-container')
# search_box = search_box.find_element_by_class_name('react-tokenized-select__input')
# search_box.send_keys('ABANDONMENT')
# time.sleep(32)
#
#
#
#
# for item in filter_list:
#     time.sleep(2)
#     try:
#         item.find_element_by_tag_name('label').click()
#     except:
#         item.find_element_by_tag_name('label').click()
#
# with open('data.csv', 'w', newline='') as f:
#     the_writer = csv.writer(f)
#     the_writer.writerow(['Grantor', 'Recorded Date', 'Doc Number'])
#     while True:
#         p_element = driver.find_element_by_class_name('a11y-table').find_element_by_tag_name(
#             'table').find_element_by_tag_name('tbody')
#         list = p_element.find_elements_by_tag_name('tr')
#         for item in list:
#             the_writer.writerow([item.find_element_by_class_name('col-3').text,
#                                  item.find_element_by_class_name('col-6').text,
#                                 item.find_element_by_class_name("col-7").text])
#
#         button_list = driver.find_elements_by_class_name('pagination__page-jump')
#         if(button_list[1].get_attribute('aria-disabled') == 'true'):
#             break
#         button_list[1].click()
#         time.sleep(2)
#
# driver.close()





