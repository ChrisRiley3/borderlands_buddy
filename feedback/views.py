from django.shortcuts import render


def feedback(request):
    """ A view to render the feedback page """
    return render(request, 'feedback/feedback.html')
