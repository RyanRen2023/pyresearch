from django.shortcuts import render,redirect
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from project2.forms import LogMessageForm
from project2.models import LogMessage
from django.views.generic import ListView



# # Create your views here.
# def home(request):
#     # return HttpResponse("Hello, Django!")
#     return render(request, "project2/home.html")

class HomeListView(ListView):
    """Renders the home page with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView,self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "project2/about.html")

def contact(request):
    return render(request, "project2/contact.html")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(request, "project2/hello_there.html", {
        "name": name,
        "date": datetime.now()
    })

def log_message(request):
    form = LogMessageForm(request.POST or None)
    # import pdb; pdb.set_trace() # breakpoint 0b1b3b3e //
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        
    return render(request, "project2/log_message.html")


# def hello_there(request, name):
#     now = datetime.now();
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)
