import feedparser

class NewsScraper:
    def __init__(self):
        self.base_url = "https://news.google.com/rss"

    def scrape_news(self, topic=None, source=None, country=None):
        url = self.base_url
        if topic and topic != "World":
            url += f"/search?q={topic}"
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:10]:  # Limit to 10 articles
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if "published" in entry else "",
                "source": entry.source.title if "source" in entry else "Google News",
                "content": entry.summary if "summary" in entry else ""
            })
        return articles

    def get_trending_topics(self):
        # For simplicity, just return the top headlines
        feed = feedparser.parse(self.base_url)
        return [entry.title for entry in feed.entries[:10]]