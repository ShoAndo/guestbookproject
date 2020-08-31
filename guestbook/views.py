from .models import Greeting
from .forms import GreetingForm
from django.template.response import TemplateResponse

def index(request):
  if request.method == 'POST':
    form = GreetingForm(request.POST)
    if form.is_valid():
      form.save()
      form.clean()
  else:
    form = GreetingForm()

  greetings = Greeting.objects.order_by('-created_at')[:5]
  return TemplateResponse(request, 'guestbook/index.html', { 'greetings': greetings, 'form': form })