'''
+----------------+        +----------------+        +----------------+
|   Web Scraper  |        |    Database    |        |     Entity     |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
| +scrape()      |        | +insert()      |        | +id: int       |
| +parse()       |        | +update()      |        | +title: string |
| +store()       |        | +delete()      |        | +url: string   |
|                |        |                |        | +content: text |
+----------------+        +----------------+        +----------------+
'''
# FILEPATH: scraper.py

import requests
from bs4 import BeautifulSoup
import sqlite3

class WebScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # parse the HTML content and extract the data you need
        title = soup.find('title').get_text()
        content = soup.find('div', {'class': 'content'}).get_text()
        return {'title': title, 'content': content}

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS entities (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()
    
    def insert(self, entity):
        self.cursor.execute('''
            INSERT INTO entities (title, url, content)
            VALUES (?, ?, ?)
        ''', (entity['title'], entity['url'], entity['content']))
        self.conn.commit()
    
    def update(self, entity):
        self.cursor.execute('''
            UPDATE entities
            SET title = ?, content = ?
            WHERE url = ?
        ''', (entity['title'], entity['content'], entity['url']))
        self.conn.commit()
    
    def delete(self, url):
        self.cursor.execute('''
            DELETE FROM entities
            WHERE url = ?
        ''', (url,))
        self.conn.commit()
    
    def get_all(self):
        self.cursor.execute('''
            SELECT * FROM entities
        ''')
        return self.cursor.fetchall()
