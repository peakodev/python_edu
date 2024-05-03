# Homework 9

## Description

Scrap http://quotes.toscrape.com/ using BeautifulSoup and Scrapy

The project is structured as follows:

- `db/config.ini`: config file with database connections credentials
- `db/conf.py`: get conf variable from config.ini
- `db/connect_mongo.py`: prepare connection to Mongo DB
- `db/models.py`: Author and Quotes Document model for mongoengine
- `beautifulsoup.py`: parse site using beautifulsoup4 and put result into data folder
- `seed.py`: populate DB with data from authors.json and quotes.json
- `data/`: folder with authors.json and quotes.json which to be placed by beautifulsoup.py script
- `requirements.txt`: This file lists the Python dependencies that need to be installed

### Prepare env

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
