from bs4 import BeautifulSoup
import glob
import os
from pathlib import Path
from pystardict import Dictionary

from django.core.management.base import BaseCommand

from ddict.models import Word, Phrase


class Command(BaseCommand):
    help = 'Import 10 sentences per each word'

    def handle(self, *args, **options):
        for fname in glob.glob('sources/*.dict'):
            dict_name = Path(fname).stem
            dict1 = Dictionary(os.path.join('sources', dict_name))
            print('Importing the %s dictionary...' % dict_name)
            for word in Word.objects.all():
                word_data = dict1.get(word.content)
                soup = BeautifulSoup(word_data, "html.parser")

                word.phrase_set.all().delete()
                i = 0
                for ex in soup.find_all('ex'):
                    if ex.text:
                        phrase = Phrase(word=word, content=ex.text)
                        phrase.save()
                        i += 1
                    if i >= 10:
                        break
            # One dictionary is enough for now
            break