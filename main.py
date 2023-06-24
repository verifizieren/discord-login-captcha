from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openai
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordLogin:
    def __init__(self, driver):
        self.driver = driver
        api_key = os.getenv('OPENAI')
        self.openai = openai
        self.openai.api_key = api_key
    
    def answer_question(self, question):
        text = self.openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{os.getenv('CAPTCHA_PROMPT')}{question}",
            max_tokens=15,
            temperature=0
        )
        answer = str(text['choices'][0]['text']).strip("\n")

        answer_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "input-field")))
        answer_input.send_keys(answer)
        answer_input.send_keys(Keys.ENTER)
    
    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "uid_5")))
        username_input.send_keys(username)
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "uid_7")))
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
    
    def check_box(self, xpath):
        iframe_xpath = xpath
        iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
        self.driver.switch_to.frame(iframe)
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "checkbox")))
        checkbox.send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
    
    def select_text_challenge(self, xpath):
        iframe_xpath = xpath
        iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
        self.driver.switch_to.frame(iframe)
        sleep(1)
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "menu-info")))
        options.send_keys(Keys.ENTER)
        text_challenge = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "text_challenge")))
        text_challenge.send_keys(Keys.ENTER)
    
    def get_question(self):
        prompt_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-text")))
        return prompt_text.text

# Initialize the webdriver and open the login page
driver = webdriver.Firefox()
driver.get("https://discord.com/login")

# Initialize the DiscordLogin object
discord_login = DiscordLogin(driver)

# Enter the login credentials and submit the form
discord_login.login("login", "passworn")

# Check the checkbox
discord_login.check_box('//*[@id="app-mount"]/div[2]/div[1]/div[4]/div[2]/div/div/div/div[1]/div[4]/div/iframe')

# Select the text challenge
discord_login.select_text_challenge('/html/body/div[8]/div[1]/iframe')

def complete_challenge(driver):
    question = discord_login.get_question()
    discord_login.answer_question(question)
    sleep(1)

# Complete the challenge multiple times
for i in range(3):
    complete_challenge(driver)
