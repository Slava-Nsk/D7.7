from django import template

register = template.Library()

cens_list = ['ублюдок', 'мать твою', 'говно', 'засранец', 'трахну', 'онанист', 'чёрт', 'идиот', 'трахать',
             'жлоб', 'вонючий', 'дерьмо', 'сука', 'падла', 'мерзавец', 'негодяй', 'гад', 'говно', 'жопа',
             'мать твою']


@register.filter()
def censor(text):
    """
    text: строковое значение, к которому применяем фильтр проверки на цензурированные слова
    cens_list: список слов, недопущенных к использованию
    """
    if isinstance(text, str):
        for i in cens_list:
            if i in text.lower():
                text = text.replace(i, i[0] + (len(i) - 1) * '*')
                text = text.replace(i.capitalize(), i[0].upper() + (len(i) - 1) * '*')
        return text
    else:
        raise TypeError('Фильтр <censor> применен не к строковому значению')
