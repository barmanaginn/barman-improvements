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

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Improvement

# BarMan - Bar Management webapp
# Copyright © 2019-2020 Yoann Pietri <me@nanoy.fr>
#
# BarMan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BarMan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BarMan.  If not, see <https://www.gnu.org/licenses/>.

"""
Admin models of the preferences app.
"""



class ImprovementAdmin(SimpleHistoryAdmin):
    """
    The admin class for Improvement.
    """

    list_display = ("title", "mode", "date")
    ordering = ("-date",)
    search_fields = ("title", "description")
    list_filter = ("mode",)


admin.site.register(Improvement, ImprovementAdmin)
