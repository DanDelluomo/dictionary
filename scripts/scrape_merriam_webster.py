#!/usr/bin/env python

"""Scrape the definition of a word from merriam-webster.com"""

import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.merriam-webster.com/dictionary/"

def merriam_webster_def(word: str) -> str:
    """Scrape a word's definition on merriam-webster.com"""
    word_url = base_url + word
    response = requests.get(word_url)
    soup = bs(response.content, 'lxml')
    # print(soup.select_one('.mw_t_bc').next_sibling.strip())
    return soup.select_one('.mw_t_bc').next_sibling.strip()