# Discord Login and Captcha Solver

This is a Python script that automates the login process on Discord and solves text-based captchas using Selenium and OpenAI's GPT-3 language model.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x
- Selenium library (you can install it using `pip install selenium`)
- OpenAI library (you can install it using `pip install openai`)
- Mozilla Firefox browser (Geckodriver) installed and added to the system's PATH

## Setup

1. Clone the repository:

```bash
git clone https://github.com/verifizieren/discord-login-captcha
```

2. Install the required dependencies:

```bash
pip install selenium openai
```

3. Download and install the Geckodriver for Firefox from the following link: [Geckodriver Download](https://github.com/mozilla/geckodriver/releases)

4. Add the Geckodriver executable to the system's PATH.

5. Create a `.env` file in the root directory of the project and add the following environment variables:

```
OPENAI=YOUR_OPENAI_API_KEY
CAPTCHA_PROMPT=YOUR_CAPTCHA_PROMPT
```

## Usage

1. Open the `main.py` file and modify the login credentials in the `discord_login.login("login", "password")` line.

2. Run the script:

```bash
python main.py
```

3. The script will open the Discord login page in a Firefox browser window and automatically fill in the login credentials.

4. It will then attempt to solve the text-based captchas by using OpenAI's GPT-3 language model.

5. After completing the captchas, the script will print the questions and answers in the terminal.

**Note:** Make sure to comply with Discord's terms of service and avoid using this script for any malicious purposes.
