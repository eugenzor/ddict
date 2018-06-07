from functools import lru_cache

from django.db import models


class Sound(models.Model):
    sign = models.CharField('Sign', max_length=5)
    freq = models.FloatField('Frequency', null=True)

    class Meta:
        ordering = ('-freq', )

    def __str__(self):
        return self.sign


class Word(models.Model):
    content = models.CharField('Content', max_length=100, unique=True)
    transcription = models.CharField('Transcription', max_length=100, null=True)
    freq = models.FloatField('Friquency', null=True, db_index=True)
    sounds = models.ManyToManyField(Sound)

    @property
    def transcription_sounds(self):
        sounds = []
        ignores = ['ˈ', 'ˌ', ' ', ',']
        opened = ''
        for sound in self.transcription:
            if sound == 'ː':
                sounds[-1] += sound
            elif sound in ignores:
                continue
            elif sound == '(':
                opened = sound
            elif sound == ')':
                opened += sound
                sounds.append(opened)
                opened = ''
            elif opened:
                opened += sound
            else:
                sounds.append(sound)
        return sounds


    class Meta:
        ordering = ('-freq', )

    def __str__(self):
        return self.content


@lru_cache(maxsize=None)
def get_word_top_freq(top=20):
    cnt = Word.objects.count()
    n = int(cnt * 20 / 100)
    return Word.objects.all()[n].freq




class Phrase(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    content = models.CharField('Content', max_length=255)

    def __str__(self):
        return self.content