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

from django.urls import path

from . import views

app_name = "barman_improvements"
urlpatterns = [
    path("improvements/", views.improvements_index, name="improvements-index"),
    path("improvements/new", views.add_improvement, name="improvements-add"),
    path(
        "improvements/<int:pk>", views.improvement_profile, name="improvements-detail",
    ),
    path(
        "improvements/<int:pk>/delete",
        views.delete_improvement,
        name="improvements-delete",
    ),
]
