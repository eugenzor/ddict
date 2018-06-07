import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .models import Sound, get_word_top_freq
from .forms import BlenderForm


class BlenderView(FormMixin, TemplateView):
    form_class = BlenderForm
    template_name = 'ddict/blender.html'

    def get_initial(self):
        return dict(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sound_list = self.request.GET.getlist('sounds')
        sounds = Sound.objects.prefetch_related('word_set', 'word_set__phrase_set').filter(id__in=sound_list)
        word_freq_limit = get_word_top_freq()
        context['words'] = []
        for sound in sounds:
            words = list(sound.word_set.filter(freq__gte=word_freq_limit))
            random.shuffle(words)
            context['words'] += words[:10]
        random.shuffle(context['words'])

        sentences = []
        for word in context['words']:
            sentences += list(word.phrase_set.all())
        random.shuffle(sentences)
        sentences = sentences[:30]
        context['sentences'] = sentences

        return context

