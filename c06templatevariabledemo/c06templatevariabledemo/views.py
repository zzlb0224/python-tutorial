from django.shortcuts import render


class person:
    def __init__(self, username):
        self.username = username


def index(request):
    context = {
        'username': 'zknu',
        'p': person('周'),
        'a': [person(1), person(2), person(3), person('周周')],
        'k': {'q': 1, "k": 2}
    }
    return render(request, 'index.html', context)
