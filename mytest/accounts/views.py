from django.shortcuts import render


def home(request):
    my_array = [1, 2, 3, 4, 5]
    my_name = "Alex"
    args = {
        "name": my_name,
        'array': my_array
    }

    return render(request, 'accounts/home.html', args)
