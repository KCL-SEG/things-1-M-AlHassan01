from django.shortcuts import render
from django.http import HttpRequest


def render_main_page(request: HttpRequest):
    return render(request=request, template_name='main_page.html')

