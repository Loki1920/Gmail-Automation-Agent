from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials
)

credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/","https://www.googleapis.com/auth/gmail.modify"],
    client_secrets_file="credentials.json"
)

api_resource = build_resource_service(credentials=credentials)

def fetch_mails():
    search = GmailSearch(api_resource=api_resource)
    emails = search("in:inbox")

    mails = []

    for email in emails:
        mails.append(
            {
                "id": email["id"],
                "threadId": email["threadId"],
                "snippet": email["snippet"],
                "sender": email["sender"],
            }

        )

    return mails


# res = fetch_mails()
# print(res)

def get_label_id(label_name):
    """Given a label name, returns its ID. Creates it if it doesn't exist."""
    try:
        results = api_resource.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])
        
        for label in labels:
            if label['name'] == label_name:
                return label['id']
        
        # If label is not found, create it
        print(f"Label '{label_name}' not found. Creating it.")
        label_body = {'name': label_name, 'labelListVisibility': 'labelShow', 'messageListVisibility': 'messageShow'}
        created_label = api_resource.users().labels().create(userId='me', body=label_body).execute()
        return created_label['id']
        
    except Exception as e:
        print(f"An error occurred while getting/creating label ID: {e}")
        return None

def move_email_to_label(message_id, label_name):
    """Moves an email to a specific label by adding the new label and removing INBOX."""
    label_id_to_add = get_label_id(label_name)
    if not label_id_to_add:
        return f"Could not find or create the label: {label_name}"

    try:
        # Body of the request to modify the labels
        body = {
            'addLabelIds': [label_id_to_add],
            'removeLabelIds': ['INBOX']
        }
        api_resource.users().messages().modify(
            userId="me",
            id=message_id,
            body=body
        ).execute()
        return f"Successfully moved message ID: {message_id} to label '{label_name}'"
    except Exception as e:
        return f"An error occurred while moving the email: {e}"
