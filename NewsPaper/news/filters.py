from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post


class PostFilter(FilterSet):
    date = DateFilter(field_name='in_time', widget=forms.DateInput(attrs={'type': 'date'}), lookup_expr='date__gte')
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__author_user__username': ['icontains']
        }