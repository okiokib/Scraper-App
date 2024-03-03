import streamlit as st
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

def scrape_news_data(start_date, end_date, category):
    base_url_dict = {
        "Health": "https://health.kompas.com/search/{}-{}-{}",
        "Travel": "https://travel.kompas.com/search/{}-{}-{}",
        "Sports": "https://www.kompas.com/sports/search/{}-{}-{}",
        "Education": "https://edukasi.kompas.com/search/{}-{}-{}",
        "Technology": "https://tekno.kompas.com/search/{}-{}-{}",
        "Property": "https://properti.kompas.com/search/{}-{}-{}",
        "Food": "https://www.kompas.com/food/search/{}-{}-{}"
    }

    data = []
    base_url = base_url_dict.get(category)

    if base_url:
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
                    if article_response.status_code == 200:
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
                    else:
                        st.warning(f"Failed to fetch data for {current_date.strftime('%d-%m-%Y')}")

                current_date += timedelta(days=1)
            else:
                st.warning(f"Failed to fetch data for {current_date.strftime('%d-%m-%Y')}")
                break

    return data

# Streamlit code
st.title("News Scraper")

categories = ["Health", "Travel", "Sports", "Education", "Technology", "Property", "Food"]
selected_category = st.selectbox("Select Category", categories)

start_date = st.date_input("Start Date", date(2024, 2, 23))
end_date = st.date_input("End Date", date(2024, 2, 24))

if start_date > end_date:
    st.error("End date must be after start date.")
else:
    if st.button("Scrape"):
        with st.spinner("Scraping in progress..."):
            news_data = scrape_news_data(start_date, end_date, selected_category)
            if not news_data:
                st.error("No data found for the selected category and date range.")
            else:
                df = pd.DataFrame(news_data)

                # Show DataFrame
                st.write("News Data:")
                st.dataframe(df)

                # Download CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='news_data.csv',
                    mime='text/csv'
                )
