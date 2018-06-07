from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import requests

from ddict.models import Word


class Command(BaseCommand):
    help = 'Import words with frequency from wikipedia'

    def handle(self, *args, **options):
        resp = requests.get('https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000')
        soup = BeautifulSoup(resp.text, "html.parser")
        for tr in soup.find_all('tr'):
            tds = tr.find_all('td')
            try:
                freq = float(tds[2].text) / 1_000_000_000
                word = Word(content=tds[1].text, freq=freq)
                word.save()
            except Exception as e:
                continue
