# coding: utf-8
# Basic 고교생을 위한 수학공식 활용사전 대응

from requests_html import HTMLSession
from crawler_main import get_book_info 


def get_concept_list_3(r):
    result = []
    subjects = r.html.find('div.subject')[1:]
    
    for sub in subjects:
        concept = {}
        concept['name'] = sub.text
        concept['url'] = list(sub.absolute_links)[0]

        result.append(concept)
    return result


def request_concept_list_per_page():
    data = {}
    session = HTMLSession()

    data['수학'] = []
    for i in range(1, 16):
        url = f'https://terms.naver.com/list.nhn?cid=42427&page={i}&categoryId=42427'
        response = session.get(url)
        
        concept_list = get_concept_list_3(response)
        data['수학'].append(concept_list)

    return data    



if __name__ == '__main__':
    url = 'https://terms.naver.com/list.nhn?cid=42427&categoryId=42427'

    session = HTMLSession()
    response = session.get(url) 

    book_info = get_book_info(response)
    concept_list = request_concept_list_per_page()

    print(book_info)
    print(concept_list)
