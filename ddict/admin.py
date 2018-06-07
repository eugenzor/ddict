from django.contrib import admin

from .models import Sound, Word, Phrase

# admin.site.index_template = "admin/index_mine.html"

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    model = Sound
    list_display = ('sign', 'frequency')

    def frequency(self, obj):
        return round(obj.freq * 100, 2)
    frequency.admin_order_field = 'freq'

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    model = Word
    list_display = ('content', 'transcription', 'frequency')
    search_fields = ('content',)

    def frequency(self, obj):
        return round(obj.freq * 100, 4)
    frequency.admin_order_field = 'freq'


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    model = Phrase
    list_display = ('content',)
    search_fields = ('content',)
