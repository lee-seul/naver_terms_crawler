# coding: utf-8


from requests_html import HTMLSession


def get_concept_list_per_page():
    result = {}
    session = HTMLSession()
    for i in range(1, 8):
        url = f'https://terms.naver.com/list.nhn?cid=58253&categoryId=58253&page={i}'
        r = session.get(url)    

        base = r.html.find('div.info_area')
        for d in base:
            title = d.find('span.info.book')[0].text
            if not title in result:
                result[title] = []
            
            concept = {}
            concept['name'] = d.find('div.subject')[0].text
            concept['url'] = list(d.find('div.subject')[0].absolute_links)[0]

            result[title].append(concept)
    return result


if __name__ == '__main__':
    concept_list = get_concept_list_per_page()

    print(concept_list)
