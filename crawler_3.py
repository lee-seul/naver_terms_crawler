# coding: utf-8
# Basic 고교생을 위한 수학공식 활용사전 대응

from requests_html import HTMLSession
from crawler_main import get_book_info 


def get_concept_list_3(r):
    data = {}
    base = r.html.find()
    

    return data


if __name__ == '__main__':
    url = 'https://terms.naver.com/list.nhn?cid=42427&categoryId=42427'

    session = HTMLSession()
    response = session.get(url) 

    book_info = get_book_info(response)
    concept_list = get_concept_list_3(response)

    print(book_info)
    print(concept_list)
