#!/usr/bin/env python

"""Scrape the definition of a word from merriam-webster.com"""

# Import Standard Libary Packages
import pathlib

# Import external packages
import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.merriam-webster.com/dictionary/"

def merriam_webster_def(word: str) -> str:
    """
    Scrape a word's definition on merriam-webster.com
    
    Returns scraped definition.
    
    """
    word_url = base_url + word
    response = requests.get(word_url)
    soup = bs(response.content, 'lxml')
    return soup.select_one('.dtText').get_text()