from django.core.management.base import BaseCommand

from ddict.models import Word, Sound


class Command(BaseCommand):
    help = 'Create the sound objects and connect them to the words'

    def handle(self, *args, **options):
        sounds = {}
        cnt = 0
        freq = 0.0
        for word in Word.objects.filter(transcription__isnull=False):
            for sound in word.transcription_sounds:
                if sound not in sounds:
                    sounds[sound] = {'cnt': 0, 'freq': 0.0, 'obj': None}
                sounds[sound]['cnt'] += 1
                sounds[sound]['freq'] += word.freq
                cnt += 1
                freq += word.freq
        Sound.objects.all().delete()

        for sound, data in sounds.items():
            obj = Sound(sign=sound, freq=data['freq'] / freq)
            obj.save()
            data['obj'] = obj

        for word in Word.objects.filter(transcription__isnull=False):
            for sign in word.transcription_sounds:
                word.sounds.add(sounds[sign]['obj'])
