import requests
from bs4 import BeautifulSoup
import sqlite3
import os
import matplotlib.pyplot as plt

# Don't change anything in this function
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Create a function called grab_data
# It should return the data of the table that needs to be inserted in the database
# It should return a dictionary like this : {'Novak Djokovic': 2, 'Sofia Kenin': 1, 'Rafael Nadal': 1, 'Iga Świątek': 1, 'Simona Halep': 1, 'Dominic Thiem': 1, 'Naomi Osaka': 1}

def grab_data(url):
    pass


# Create a function called database to insert the values of the dictionary into the table called tennis
def database(dictionary):
    cur, conn = setUpDatabase('tennis.db')
    pass


# Create a vizualization using matplotlib
def viz(data):
    pass

# Create a vizualization using plotly
def plotly(data):
    pass



# Uncomment this to make sure your function works
# data = grab_data("https://en.wikipedia.org/wiki/Grand_Slam_(tennis)")
# database(data)
# viz(data)
# plotly(data)
