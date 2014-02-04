#!/usr/bin/env python3

import datetime
import re
import urllib.request
from bs4 import BeautifulSoup

def main():
  weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
  url = 'http://www.stw-thueringen.de/deutsch/mensen/einrichtungen/weimar/mensa-am-park.html'
  response = urllib.request.urlopen(url)
  soup = BeautifulSoup(response.read())
  for week in soup.find_all('div', class_='tabber'):
    for day in week.find_all('div', class_='tabbertab'):
      if day['title'] == weekdays[datetime.datetime.today().weekday()]:
        for menu in day.find_all('td'):
          if not ('Ausgabe' in menu.get_text() or 'Sonderausgabe' in menu.get_text()):
            text = re.sub(' ( )*', ' ', menu.get_text(strip=True).split('Inhalt')[0])
            if not re.match('[0-9],[0-9][0-9] €', text):
              print(text.strip(), end='')
            else:
              print(' (' + text + ')')
        print()

if __name__ == '__main__':
  main()