# coding: utf-8
# 학습용어 개념사전, 초등수학 개념사전 대응


from requests_html import HTMLSession


def get_book_info(r):
    data = {}
    base = r.html.find('.cite_info')[0]

    data['title'] = base.find('strong')[0].text
    data['publisher'] = base.find('.sub_info')[2].text 

    return data


def get_concept_list(r, subject='수학'):
    data = {}
    base = r.html.find('.contents_sub')

    for idx, sub in enumerate(base):
        raw_subject = sub.find('.contents_item')[0].text
        raw_subject = raw_subject.replace(' 더보기', '')

        if raw_subject.split()[0] == subject or not subject:
            raw_list = sub.find('ul')
            concept_list = raw_list[0].text
            data[raw_subject] = concept_list.split('\n')
        
    return data


def print_data(url, subject=None): 
    session = HTMLSession()
    response = session.get(url)

    book_info = get_book_info(response)
    concept_list = get_concept_list(response, subject)

    print(book_info)
    print(concept_list)


if __name__ == '__main__':
    urls = [
        'https://terms.naver.com/list.nhn?cid=43672&categoryId=43672&so=st4.asc',
        'https://terms.naver.com/list.nhn?cid=42426&categoryId=42426',
        'https://terms.naver.com/list.nhn?categoryId=43669&so=st4.asc',
    ]
    
    for idx, url in enumerate(urls):
        subject = None
        if not idx:
            subject = '수학'

        print_data(url, subject)


