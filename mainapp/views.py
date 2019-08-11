from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/main.html')


def products(request):
    context = {'username': None, 'products': ['Люстра', 'Бра']}
    return render(request, 'mainapp/products.html', context=context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
