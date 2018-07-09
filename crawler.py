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
        temp = sub.find('.contents_item')[0].text
        raw_subject = temp.split()[0]
        if raw_subject == subject or not subject:
            raw_list = sub.find('ul')
            concept_list = raw_list[0].text
            data[raw_subject] = concept_list.split('\n')
        
    return data




if __name__ == '__main__':
    # 학습용어 개념사전
    url = 'https://terms.naver.com/list.nhn?cid=43672&categoryId=43672&so=st4.asc'

    session = HTMLSession()
    response = session.get(url)

    book_info = get_book_info(response)
    concept_list = get_concept_list(response)

    print(book_info)
    print(concept_list)
    
    print()


    # 초등수학 개념사전
    url = 'https://terms.naver.com/list.nhn?cid=42426&categoryId=42426'

    response = session.get(url)

    book_info = get_book_info(response)
    concept_list = get_concept_list(response, subject=None)
