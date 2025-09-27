# tools.py

#from langchain.tools import tool
from crewai.tools import tool
from gmail_service import move_email_to_label

class EmailTools:
    @tool("Move Email to Label")
    def move_email(message_id: str, label_name: str) -> str:
        """
        Moves an email to a specified label in Gmail.
        The `message_id` is the unique identifier of the email to move.
        The `label_name` is the name of the destination label (e.g., 'From Marketing Lists').
        """
        return move_email_to_label(message_id, label_name)