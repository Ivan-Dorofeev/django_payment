from django.shortcuts import render


def main(request):
    pass
    context = {'text': 'ooops'}
    return render(request, 'index.html', context)
