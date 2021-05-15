
import sys
from web_scraper import scraper


output_file_name = sys.argv[1]

scraper = scraper()

while True:
    print('Choose a Document Type or Type NO if done selecting:')
    response = input()
    if(response == 'NO'):
        break
    try:
        scraper.set_document_filter(response)
    except:
        print('Invalid Document type, please try again.')

scraper.scrape_data(output_file_name, True)
scraper.close_driver()




