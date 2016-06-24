from django.views.generic.list import ListView
from images.models import Image
# from random import randint


class IndexView(ListView):
    model = Image
    image_count = 3
    template_name = 'images/index.html'

    # def get_queryset(self):
    #     indexes = [randint(0, Image.objects.count()) for i in range(self.image_count)]
    #     for i in
