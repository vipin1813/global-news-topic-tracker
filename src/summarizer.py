import subprocess

class Summarizer:
    def __init__(self, model="llama2"):
        self.model = model

    def summarize_article(self, article_content):
        prompt = f"Summarize the following news article:\n\n{article_content}\n\nSummary:"
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error generating summary: {e}"