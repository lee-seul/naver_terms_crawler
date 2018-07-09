# coding: utf-8


import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    if not response.status_code == 200:
        print(response.status_code)
        return 

    return response.text


def parsing_book_info(html_data):
    data = {}

    soup = BeautifulSoup(html_data, 'html.parser')
    base = '#content > div.cite_area_wrap > div.cite_area > div '

    data['title'] = soup.select(base + '> strong')[0].text
    data['publisher'] = soup.select(base + '> p > span')[1].text
    
    return data


if __name__ == "__main__":

    # 초등수학 개념사전
    #url = 'https://terms.naver.com/list.nhn?cid=42426&categoryId=42426'

    # 학습용어 개념사전 
    url = 'https://terms.naver.com/list.nhn?cid=43672&categoryId=43672&so=st4.asc' 

    html = get_html(url)
    if html:
        book_info = parsing_book_info(html)
        print(book_info)

        




