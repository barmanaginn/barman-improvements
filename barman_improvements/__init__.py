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

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from barman.plugin import BarmanPlugin


class PluginApp(BarmanPlugin):
    name = "barman_improvements"

    class BarmanPluginMeta:
        name = "Improvements"
        author = "Yoann Pietri"
        description = _("Add an improvement form")
        version = 0.1
        url = "https://github.com/barmanaginn/barman-improvements"
        email = "me@nanoy.fr"

        # Define here urls for navbar. See documentation for more details.
        nav_urls = (
            {
                "text": _("Submit improvement"),
                "icon": "fas fa-bug",
                "link": reverse_lazy("plugins:barman_improvements:improvements-add"),
                "permission": None,
                "login_required": True,
                "admin_required": False,
                "superuser_required": False,
            },
            {
                "text": _("See improvements"),
                "icon": "fas fa-bug",
                "link": reverse_lazy("plugins:barman_improvements:improvements-index"),
                "permission": "barman_improvements.view_improvement",
                "login_required": True,
                "admin_required": False,
                "superuser_required": False,
            },
        )

        # Define here settings specific to this plugin. See documentation for more details.
        settings = (
            {
                "name": "IMPROVEMENTS_STORE",
                "description": _("Store improvements in database."),
                "default": True,
            },
            {
                "name": "IMPROVEMENTS_EMAILS",
                "description": _(
                    "Recipients of improvement email. If set None or empty array, no email is sent."
                ),
                "default": ["barman@nanoy.fr"],
            },
        )

        # Define here additionnal info for user profile. See documentation for more details.
        user_profile = ()

    def ready(self):
        from . import signals

        return super().ready()


default_app_config = "barman_improvements.PluginApp"
