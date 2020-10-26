from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, TemplateView

from .forms import EmailForm, NumberForm
from .models import Post


# def index_view(request):
#     return render(request, "index.html")


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class ContentView(TemplateView):
    template_name = 'content.html'


def index_view(request):
    if request.method == "POST" and 'btn1' in request.POST:
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            # Form fields passed validation
            cd = email_form.cleaned_data
        return render(request, "index.html", {"form": email_form})
    else:
        email_form = EmailForm()

    if request.method == "POST" and 'btn1' in request.POST:
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "index.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()

    return render(request, "index.html", {"form": email_form, "footer_form": number_form})


def repair_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "repair.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "repair.html", {"footer_form": number_form})


def levkas_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "levkas.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "levkas.html", {"footer_form": number_form})


def farmer_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "farmer.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "farmer.html", {"footer_form": number_form})


def home_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "home.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "home.html", {"footer_form": number_form})


def foreman_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "foreman.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "foreman.html", {"footer_form": number_form})


def blacksmith_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "blacksmith.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "blacksmith.html", {"footer_form": number_form})


def antiques_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "antiques.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "antiques.html", {"footer_form": number_form})


def stove_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "stove.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "stove.html", {"footer_form": number_form})


def electrician_view(request):
    if request.method == "POST":
        number_form = NumberForm(request.POST)
        if number_form.is_valid():
            # Form fields passed validation
            cd = number_form.cleaned_data
        return render(request, "electrician.html", {"footer_form": number_form})
    else:
        number_form = NumberForm()
    return render(request, "electrician.html", {"footer_form": number_form})