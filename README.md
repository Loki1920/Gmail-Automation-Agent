# AI Email Automation Agent using CrewAI 📧🤖

This project deploys a team of autonomous AI agents built with the **CrewAI** framework to automatically read, analyze, and organize your Gmail inbox. The agents work together to distinguish important emails from promotional content and newsletters, moving the important ones to a designated label.



---

## ✨ Features

-   **Automated Email Analysis:** The system fetches unread emails from your Gmail inbox for processing.
-   **Intelligent Filtering:** An "Analyst" agent uses AI to analyze email snippets and senders to identify which messages are important and which are not.
-   **Automatic Organization:** A "Specialist" agent takes the list of important emails and moves them to a custom Gmail label (e.g., `IMPORTANT_EMAILS`), cleaning up your main inbox.
-   **Secure Gmail Integration:** Utilizes the official Google Gmail API with OAuth 2.0 for secure and authorized access to your account.

---

## 🛠️ How It Works

The project operates using a two-agent crew that executes tasks sequentially:

1.  **Analyst Agent:** Its primary task is to go through a list of unread emails. It analyzes the content and metadata (like the sender) to create a definitive list of emails that are deemed "important."
2.  **Specialist Agent:** This agent receives the list of important emails from the Analyst. It then uses a custom `move_email` tool to interact with the Gmail API, moving each identified email from the inbox to the `IMPORTANT_EMAILS` label.

This multi-agent approach allows for a clear separation of concerns, making the system easy to understand and extend.

---

## 💻 Technology Stack

-   **Framework:** `CrewAI`
-   **Language:** `Python`
-   **Toolkits:** `LangChain` (for the Gmail API tool)
-   **API:** `Google Gmail API`

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### **Prerequisites**

-   Python 3.8+
-   Git

### **1. Clone the Repository**

First, clone this repository to your local machine.
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```

### **2. Set Up Google API Credentials**

This is the most crucial step for allowing the application to access your Gmail.

1.  **Enable the Gmail API:** Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project. In that project, enable the "Gmail API".
2.  **Create Credentials:** Go to the **Credentials** tab and create an **OAuth 2.0 Client ID** for a **Desktop application**.
3.  **Configure Consent Screen:** You will be prompted to configure the OAuth consent screen. Add the required scope: `.../auth/gmail.modify`.
4.  **Add Test User:** While your app is in "testing" mode, you must add your own Gmail address to the "Test users" section.
5.  **Download JSON:** Download the OAuth client ID JSON file.
6.  **Rename and Place File:** Rename the downloaded file to `credentials.json` and place it in the root directory of this project.

### **3. Create a Virtual Environment**

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **4. Install Dependencies**

Install all the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

With the setup complete, you can now run the email sorter.

1.  Execute the main application file from the terminal:
    ```bash
    python app.py
    ```
2.  **First-Time Authorization:** The first time you run the script, a new tab will open in your web browser asking you to log in to your Google account and grant permission for the app to access your Gmail.
3.  After you approve, a `token.json` file will be created in the project directory. This file stores your authorization so you won't have to log in every time.
4.  **Watch the Magic!** The agents will now start their work. You will see their progress printed in the terminal. Once they are finished, check your Gmail for the new `IMPORTANT_EMAILS` label!
