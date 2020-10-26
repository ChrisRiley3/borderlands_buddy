from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm

from profiles.models import UserProfile


def feedback(request):
    """ A view to render the feedback page """
    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'feedback/feedback.html', context)


@login_required
def add_feedback(request):
    """ A view for users to add feedback """

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedbacks = form.save(commit=False)
            feedbacks.user = UserProfile.objects.get(user=request.user)
            feedbacks.save()
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


@login_required
def edit_feedback(request, feedback_id):
    """ Edit feedback in the feedback section """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('feedback'))

    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated feedback!')
            return redirect('feedback')
        else:
            messages.error(request, 'Failed to update feedback. Please ensure the form is valid.')
    else:
        form = FeedbackForm(instance=feedback)
        messages.info(request, f'You are editing {feedback.feedback}')

    template = 'feedback/edit_feedback.html'
    context = {
        'form': form,
        'feedback': feedback,
    }

    return render(request, template, context)


@login_required
def delete_feedback(request, feedback_id):
    """ Delete feedback from the feedback section """

    feedback = get_object_or_404(Feedback, pk=feedback_id)
    feedback.delete()
    messages.success(request, 'Feedback deleted')
    return redirect(reverse('feedback'))
