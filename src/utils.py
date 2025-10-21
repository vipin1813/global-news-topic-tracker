def format_news_data(news_data):
    formatted_data = []
    for article in news_data:
        formatted_data.append({
            'title': article.get('title'),
            'link': article.get('link'),
            'published': article.get('published'),
            'source': article.get('source')
        })
    return formatted_data

def handle_api_request(url, params=None):
    import requests
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None