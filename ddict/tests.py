import pytest

from .models import Word

@pytest.mark.parametrize('transcription, sounds', [
    ('əv', ['ə', 'v']),
    ('ænd', ['æ', 'n', 'd']),
    ('æ', ['æ']),
    ('ɔːl', ['ɔː', 'l']),
    ('ˈeni', ['e', 'n', 'i']),
    ('əˈbaʊt', ['ə', 'b', 'a', 'ʊ', 't']),
    ('ˈɑːftə(r)', ['ɑː', 'f', 't', 'ə', '(r)'])
])
def test_sounds(transcription, sounds):
    word = Word(transcription=transcription)
    assert word.transcription_sounds == sounds