from bs4 import BeautifulSoup

def parse_content(content: bytes):
    soup = BeautifulSoup(content, 'html.parser')
