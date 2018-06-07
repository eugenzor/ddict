from bs4 import BeautifulSoup
import glob
import os
from pathlib import Path
from pystardict import Dictionary

from django.core.management.base import BaseCommand

from ddict.models import Word, Phrase


class Command(BaseCommand):
    help = 'Add transcription and create sentence examples for each word'

    def handle(self, *args, **options):
        for fname in glob.glob('sources/*.dict'):
            dict_name = Path(fname).stem
            dict1 = Dictionary(os.path.join('sources', dict_name))
            print('Updating transcription from %s dictionary...' % dict_name)
            for word in Word.objects.all():
                word_data = dict1.get(word.content)
                soup = BeautifulSoup(word_data, "html.parser")
                trans_vars = soup.find_all('c', attrs={'c': 'teal'})
                for trans_var in trans_vars:
                    if trans_var.text.startswith('['):
                        word.transcription = trans_var.text[1:-1]
                        word.save()
                        break

                word.phrase_set.all().delete()
                for ex in soup.find_all('ex'):
                    if ex.text:
                        phrase = Phrase(word=word, content=ex.text)
                        phrase.save()
                        break
            break

