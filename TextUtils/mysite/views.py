from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dictionary = {"name": "Nabin", "address": "Gurgaon"}
    return render(request, "index.html", dictionary)


def about(request):
    charNumbers = ""
    txtVal = request.POST.get('text', 'Default')
    removepunc = request.POST.get('removePunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(txtVal)
    print(removepunc)
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if removepunc == 'on':
        for char in txtVal:
            if char not in punctuations:
                analyzed = analyzed + char
        txtVal = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in txtVal:
            analyzed = analyzed + char.upper()
        txtVal = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in txtVal:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        txtVal = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, value in enumerate(txtVal):
            if not (txtVal[index] == " " and txtVal[index + 1] == " "):
                analyzed = analyzed + value
        txtVal = analyzed

    if charcount == "on":
        charNumbers = f"Number Of Characters: {len(txtVal)}"

    params = {"purpose": "Analyzed Data", 'analyzed_data': analyzed, 'char_numbers': charNumbers}

    return render(request, "about.html", params)
