import re


class SearchService:

    SEARCH_KEYWORDS = {
        "today",
        "latest",
        "current",
        "news",
        "live",
        "recent",
        "winner",
        "won",
        "score",
        "result",
        "price",
        "weather",
        "temperature",
        "forecast",
        "stock",
        "stocks",
        "crypto",
        "bitcoin",
        "ethereum",
        "gold",
        "silver",
        "election",
        "breaking"
    }

    @classmethod
    def is_search_query(cls, prompt):

        message = prompt.lower().strip()

        if any(keyword in message for keyword in cls.SEARCH_KEYWORDS):
            return True

        if re.search(r"\b20\d{2}\b", message):
            return True

        return False