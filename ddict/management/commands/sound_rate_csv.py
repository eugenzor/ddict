import random

from django.core.management.base import BaseCommand

from ddict.models import Sound


class Command(BaseCommand):
    help = 'Make sentences for each sound'

    def handle(self, *args, **options):
        sounds = Sound.objects.prefetch_related('word_set', 'word_set__phrase_set').all()
        for sound in sounds:
            words = list(sound.word_set.all())
            random.shuffle(words)
            words = words[:10]
            self.stdout.write(
                '"%s", "%s [%s], %s [%s]"' % (
                    sound,
                    words[0], words[0].transcription,
                    words[1], words[1].transcription,
                ), ending="\n"
            )
