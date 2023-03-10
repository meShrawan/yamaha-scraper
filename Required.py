import pandas as pd
import requests
from bs4 import BeautifulSoup


def return_response(url):
    return requests.get(url)


def return_soup(url):
    response = return_response(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup