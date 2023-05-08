from django.urls import reverse

manu = [
    {'title': 'Форум', "url_name": 'forum'},
    {'title': 'Магазин', "url_name": "shop"},
    {'title': 'Отзывы', "url_name": "feedback"},
    {'title': 'главная', "url_name": "main"}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['manu'] = manu
        return context
