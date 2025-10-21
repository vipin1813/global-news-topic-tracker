import streamlit as st
from news_scraper import NewsScraper
from summarizer import Summarizer
import os

# Inject custom CSS
css_path = os.path.join(os.path.dirname(__file__), "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from streamlit_extras.add_vertical_space import add_vertical_space

def main():
    st.markdown("<h1 style='text-align: center; margin-bottom: 1.5em;'>Global News Topic Tracker</h1>", unsafe_allow_html=True)

    # Sidebar with icons
    st.sidebar.markdown(
        """
        <div style="font-size:1.3em;font-weight:700;margin-bottom:1em;">
            <span style="vertical-align:middle;">🔎 Filters</span>
        </div>
        """, unsafe_allow_html=True
    )
    topic = st.sidebar.selectbox("📁 Choose Topic", ["AI", "Politics", "Sports", "Business", "Health", "Science", "Technology", "World"])
    source = st.sidebar.selectbox("📰 Choose Source", ["Any", "Google News", "Reuters", "BBC", "Al Jazeera", "Mint", "India Today", "News18"])
    country = st.sidebar.selectbox("🌍 Choose Country", ["Global (Default)", "India", "US", "UK", "Australia", "Canada"])
    fetch = st.sidebar.button("🚀 Fetch News")

    if fetch:
        news_scraper = NewsScraper()
        summarizer = Summarizer(model="llama2")
        articles = news_scraper.scrape_news(topic=topic, source=source, country=country)
        st.markdown("<h2 style='margin-top:0.5em;'>Latest Articles:</h2>", unsafe_allow_html=True)
        st.markdown('<div class="news-grid">', unsafe_allow_html=True)
        for article in articles:
            summary = article['content'][:180] + "..." if article['content'] else "No summary available."
            st.markdown(
                f"""
                <div class="news-card">
                    <a class="news-title" href="{article['link']}" target="_blank">{article['title']}</a>
                    <div class="news-meta">{article['source']} &nbsp;•&nbsp; {article['published']}</div>
                    <div class="news-summary">{summary}</div>
                </div>
                """, unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Use the filters on the left and click 'Fetch News' to see the latest articles.")

if __name__ == "__main__":
    main()

# filepath: /home/seq_vipin/learn python/ChatBot/phase2/global-news-topic-tracker/src/news_scraper.py
def scrape_news(self, topic=None, source=None, country=None):
    url = self.base_url
    if topic and topic != "World":
        url += f"/search?q={topic}"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:10]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published if "published" in entry else "",
            "source": entry.source.title if "source" in entry else "Google News",
            "content": entry.summary if "summary" in entry else ""
        })
    # Fallback to default feed if too few articles
    if len(articles) < 5:
        feed = feedparser.parse(self.base_url)
        for entry in feed.entries[:10 - len(articles)]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if "published" in entry else "",
                "source": entry.source.title if "source" in entry else "Google News",
                "content": entry.summary if "summary" in entry else ""
            })
    return articles