import pandas as pd
from datetime import date, timedelta
from requests_html import HTMLSession

def get_article_content(article_url):
    session = HTMLSession()
    response = session.get(article_url)
    if response.status_code == 200:
        content = response.html.find('div.read__content p')
        return ''.join([p.text for p in content])
    return ""

def scrape_news_data(start_date, end_date):
    base_url = "https://health.kompas.com/search/{}-{}-{}"
    data = []

    current_date = start_date
    while current_date <= end_date:
        url = base_url.format(current_date.year, current_date.month, current_date.day)
        session = HTMLSession()
        response = session.get(url)

        if response.status_code == 200:
            news_elements = response.html.find('h3.article__title.article__title--medium')

            for element in news_elements:
                title = element.text
                article_url = element.find('a', first=True).attrs['href']

                article_response = session.get(article_url)
                date_time = article_response.html.find('div.read__time', first=True).text.replace('Kompas.com -', '').strip()
                article_link = article_response.html.find('a.article__link', first=True).attrs['href']
                class_info = article_response.html.find('div.article__subtitle.article__subtitle--inline', first=True).text.strip()

                content = get_article_content(article_url)

                data.append({
                    'Date': date_time,
                    'Title': title,
                    'URL': article_link,
                    'Content': content,
                    'Class': class_info
                })

            current_date += timedelta(days=1)
        else:
            print(f"Failed to fetch data for {current_date.strftime('%d-%m-%Y')}")

    return data

start_date = date(2024, 2, 23)
end_date = date(2024, 2, 24)

news_data_health = scrape_news_data(start_date, end_date)
df_health = pd.DataFrame(news_data_health)
df_health
