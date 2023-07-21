from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            feedback_text = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']
            feedback = Feedback(name=name, feedback=feedback_text, rating=rating)
            feedback.save()
            return redirect('success_message')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def success_message(request):
    return render(request, 'success_message.html')
