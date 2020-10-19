from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm


def feedback(request):
    """ A view to render the feedback page """
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'feedback/feedback.html', context)


def add_feedback(request):
    """ A view for users to add feedback """

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedbacks = form.save()
            messages.success(request, 'Successfully added feedback!')
            return redirect('feedback')
            feedbacks.objects.create(feedbacks=feedbacks)
        else:
            messages.error(request, 'Failed to add feedback. Please ensure the form is valid.')
    else:
        form = FeedbackForm()
    template = 'feedback/add_feedback.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
