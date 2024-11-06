from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from ads.models import Ads
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"


class Logout(LoginView):
    next_page = reverse_lazy("accounts:login")


class IndexView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = [
            ["products_count", Product],
            ["advertisements_count", Ads],
            ["leads_count", Lead],
        ]
        result = {
            variable: model.objects.aggregate(count=Count("id"))["count"]
            for variable, model in data
        }
        context.update(result)
        context["customers_count"] = Customer.objects.aggregate(
            count=Count("lead_id", distinct=True)
        )["count"]
        return context