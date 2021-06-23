from django.shortcuts import render


def index(request):
    """main page"""

    return render(
        request=request,
        template_name='index.html'
    )
