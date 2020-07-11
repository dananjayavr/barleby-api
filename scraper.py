from bs4 import BeautifulSoup
import requests
import json


def get_all_quotation_books():
    # Fetching the Quotations index page:
    quotations = requests.get('https://www.bartleby.com/quotations/')

    # Turning it in to a BeautifulSoup
    quotations_bs4 = BeautifulSoup(quotations.text, "html.parser")

    # Getting all the tables
    tables = quotations_bs4.findChildren('table')

    # Iterating and extracting URLs of quotation books
    # Full URLs will be appended to the array quotation books.
    quotation_books = []
    for table in tables:
        for row in table.findChildren(['tr']):
            for cell in row.findChildren('dt'):
                for link in cell.findChildren('a'):
                    if '.html' not in link['href']:
                        quotation_books.append('https://www.bartleby.com' + link['href'])
                    else:
                        pass

    return quotation_books


def get_quotes_index(url='https://www.bartleby.com/78/index1.html'):
    index = requests.get(url)
    index_bs4 = BeautifulSoup(index.text, 'html.parser')
    subjects = {}
    # Quote subjects
    for link in index_bs4.findChildren('ol'):
        for list_item in link.findChildren('li'):
            for anchor in list_item.findChildren('a'):
                subjects[(anchor.contents[0])] = 'https://www.bartleby.com' + anchor['href']

    return json.dumps({'results': subjects})


def get_quotes_by_subject(subject="Reading", url="https://www.bartleby.com/78/677.html"):
    index = requests.get(url)
    index_bs4 = BeautifulSoup(index.text, 'html.parser')
    quotes = []

    tables = index_bs4.find_all('table', {"align": "CENTER"})

    for td in tables[1].find_all('tr'):
        quotes.append(td.text.replace(u'\xa0', u' ').strip())

    filter(None, quotes)

    return json.dumps({subject: quotes})
