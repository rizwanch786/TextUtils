from django.http import HttpResponse
from django.shortcuts import render


def run_template(request):
    return render(request, 'index.html')


def analyze(request):
    # get the data
    string = request.POST.get('text', 'default')
    rPun = request.POST.get('RemoveP', 'off')
    capital = request.POST.get('Cap', 'off')
    rSpace = request.POST.get('RemoveSp', 'off')
    rline = request.POST.get('RemoveNewLine', 'off')
    # create an empty dictionary
    d = {}
    # return an msg if switches are off
    if rPun != "on" and capital != "on" and rSpace != "on" and rline != "on":
        return HttpResponse("Please select any operation and try again")
    # remove Punctuations
    if rPun == "on":
        analyzed_pun = ''
        punch = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in string:
            if char not in punch:
                analyzed_pun += char
        d = {"purpose": "Remove Punctuation", "analyzed_text": analyzed_pun}
        string = analyzed_pun
    # Upper case
    if capital == "on":
        analyze_cap = string.upper()
        d = {"purpose": "Capital All Characters", "analyzed_text": analyze_cap}
        string = analyze_cap
    # Remove extra spaces
    if rSpace == "on":
        analyzed_spaces = ''
        for index, char in enumerate(string):
            if string[index] == " " and string[index + 1] == " ":
                pass
            else:
                analyzed_spaces += char
        d = {"purpose": "Remove Extra Spaces", "analyzed_text": analyzed_spaces}
        string = analyzed_spaces
    # Remove new lines
    if rline == "on":
        remove_new_line = ''
        for char in string:
            if char != "\n" and char != "\r":
                remove_new_line += char
        d = {"purpose": "Remove NewLines", "analyzed_text": remove_new_line}
        string = remove_new_line

    return render(request, 'data.html', d)
