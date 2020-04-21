# barman-improvements - plugin for barman
# Copyright © 2020 Yoann Pietri <me@nanoy.fr>
#
# barman-improvements is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# barman-improvements is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with barman-improvements.  If not, see <https://www.gnu.org/licenses/>.

from barman_improvements import PluginApp
from barman_improvements.forms import ImprovementForm
from barman_improvements.models import Improvement
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from barman.acl import active_required


"""
Improvments views of preferences app.
"""


@active_required
@login_required
def add_improvement(request):
    """Display a form to add an improvement

    Save the argument if IMPROVEMENTS_STORE is set to True

    If IMPROVEMENTS_EMAILS is not empyt, send a mail to the recipient.
    If SMTP settings are not set (or wrong) it fails silently.

    Args:
        request (dict): django request
    
    Returns:
        HttpResponse: render form.html
    """
    form = ImprovementForm(request.POST or None)
    if form.is_valid():
        improvement = form.save(commit=False)
        improvement.barman = request.user
        if PluginApp.BarmanPluginMeta.IMPROVEMENTS_STORE:
            improvement.save()
        if PluginApp.BarmanPluginMeta.IMPROVEMENTS_EMAILS:
            template = _(
                """
            A new improvement proposal was sent : {title}, {mode}.

            Description :

            {description}
            """
            )
            try:
                send_mail(
                    _("New improvement proposal"),
                    template.format(
                        title=improvement.title,
                        mode=improvement.get_mode_display(),
                        description=improvement.description,
                    ),
                    settings.SERVER_EMAIL,
                    PluginApp.BarmanPluginMeta.IMPROVEMENTS_EMAILS,
                )
            except:
                pass
        messages.success(request, _("Improvement proposal has been sent."))
        return redirect(reverse("home"))
    return render(
        request,
        "form.html",
        {
            "form": form,
            "form_title": _("Improvement proposal"),
            "form_button": _("Send"),
            "form_button_icon": "fas fa-bug",
        },
    )


@active_required
@login_required
@permission_required("preferences.view_improvement")
def improvements_index(request):
    """Display all improvements
    
    Args:
        request (dict): django request
    
    Returns:
        HttpResponse: render improvements_index.html
    """
    improvements = Improvement.objects.all().order_by("-date")
    return render(
        request,
        "barman_improvements/improvements_index.html",
        {"improvements": improvements,},
    )


@active_required
@login_required
@permission_required("preferences.view_improvement")
@permission_required("preferences.change_improvement")
def improvement_profile(request, pk):
    """Display the improvement's profile
    
    Args:
        request (dict): django request
        pk (int): primary key of the improvement
    
    Returns:
        HttpResponse: render improvement_profile.html
    """
    improvement = get_object_or_404(Improvement, pk=pk)
    return render(
        request,
        "barman_improvements/improvement_profile.html",
        {"improvement": improvement},
    )


@active_required
@login_required
@permission_required("preferences.delete_improvement")
def delete_improvement(request, pk):
    """Delete an improvement
    
    Args:
        request (dict): django request
        pk (int): primary key of improvement
    
    Returns:
        HttpResponse: redirection to improvements index
    """
    improvement = get_object_or_404(Improvement, pk=pk)
    improvement.delete()
    messages.success(request, _("Improvement was deleted."))
    return redirect(reverse("plugins:barman_improvements:improvements-index"))
