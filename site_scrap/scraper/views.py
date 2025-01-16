import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Link


def scrape(request):
    page = requests.get('https://facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        Link.objects.create(address=link_address, name=link_text)
    links = Link.objects.all()
    return render(request, 'result.html', {'links':links})



