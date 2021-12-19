# https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/
# https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
import requests
from parser import parse_content

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
parse_content(page.content)
