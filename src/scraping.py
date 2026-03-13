import requests
from bs4 import BeautifulSoup
def get_titles(url):
    response =requests.get(url)
    soup =BeautifulSoup(response.content,"html.parser")
    return [t.text for t in soup.find_all("h3")]