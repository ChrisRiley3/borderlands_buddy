from django.shortcuts import render
from .models import Feedback


def feedback(request):
    """ A view to render the feedback page """
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'feedback/feedback.html', context)
