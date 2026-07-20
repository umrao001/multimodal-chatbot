from datetime import datetime

from services.calculator_service import CalculatorService


class ToolService:

    @staticmethod
    def execute(prompt):
        message = prompt.lower().strip()

        if ToolService.is_date_query(message):
            return datetime.now().strftime(
                "Today is %A, %d %B %Y."
            )

        if ToolService.is_time_query(message):
            return datetime.now().strftime(
                "Current time is %I:%M %p."
            )

        calculator_result = CalculatorService.evaluate(message)

        if calculator_result:
            return calculator_result

        return None

    @staticmethod
    def is_date_query(message):
        keywords = [
            "today",
            "date",
            "day",
            "what day",
            "what's the date",
            "todays date"
        ]

        return any(keyword in message for keyword in keywords)

    @staticmethod
    def is_time_query(message):
        keywords = [
            "time",
            "current time",
            "what time",
            "clock"
        ]

        return any(keyword in message for keyword in keywords)