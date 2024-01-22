from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, RedirectView, TemplateView, UpdateView

from erp_greenwich.users.models import Client

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse("users:detail", kwargs={"username": request.user.username})
        )
    return redirect("home/")


class HomeView(TemplateView):
    template_name = "pages/home.html"


@require_http_methods(["POST"])
@login_required
def change_profile(request):
    try:
        user = User.objects.get(pk=request.user.id)
        data = request.POST.dict()
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        client, created = Client.objects.get_or_create(
            user=user,
            defaults={
                "user": user,
                "address": data.get("address"),
                "city": data.get("city"),
                "country": data.get("country"),
                "postal_code": data.get("postal_code"),
                "about_me": data.get("about_me"),
            },
        )
        if created:
            client.address = data.get("address")
            client.city = data.get("city")
            client.country = data.get("country")
            client.postal_code = data.get("postal_code")
            client.about_me = data.get("about_me")
            client.save()
        user.save()
        messages.success(request, "User info update successfully")
        return HttpResponseRedirect(
            reverse("users:detail", kwargs={"username": request.user.username})
        )
    except User.DoesNotExist:
        messages.error(request, "User info not found")
        return redirect("home/")
