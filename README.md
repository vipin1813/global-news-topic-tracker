# Global News Topic Tracker

This project is designed to scrape trending topics from Google News and summarize the articles using a language model. It leverages Streamlit for a user-friendly interface and provides real-time insights into current news trends.

## Project Structure

```
global-news-topic-tracker
├── src
│   ├── main.py          # Entry point of the application
│   ├── news_scraper.py  # Contains the NewsScraper class for scraping news
│   ├── summarizer.py    # Contains the Summarizer class for summarizing articles
│   └── utils.py         # Utility functions for supporting functionalities
├── requirements.txt     # Lists project dependencies
├── README.md            # Documentation for the project
└── .gitignore           # Specifies files to ignore in version control
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/global-news-topic-tracker.git
   cd global-news-topic-tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Run the application:**
   ```bash
   streamlit run src/main.py
   ```

2. **Navigate to the provided local URL to access the application.**

## Functionalities

- **News Scraping:** The application fetches the latest articles from Google News and retrieves trending topics.
- **Article Summarization:** It summarizes the content of the articles using a language model, providing concise insights.
- **User Interface:** Built with Streamlit, the app offers an interactive experience for users to explore trending news topics and their summaries.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.