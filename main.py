from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SECRET = os.getenv("SECRET")

#
app = FastAPI()

urls = [
    "https://radiant-hummingbird-697a83.netlify.app/",
    "http://trialserver.rf.gd/trial6/www.classcentral.com/index.html",
    "https://class-central.vercel.app/www.classcentral.com/index.html",
    "https://5dcookie.github.io/",
    "https://www.census2011.co.in/city.php#:~:text=Here%20are%20the%20details%20of,%2D%203%2C124%2C458%2C%20Jaipur%20%2D%203%2C046%2C163",
]

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    driver = webdriver.Firefox()
    for i in urls:
        driver.get(i)
        webpage_lang = driver.find_element(By.XPATH, "//html[@lang='hi']")
        if (webpage_lang.is_displayed()):
            return "pass"
        return "fail"


