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

# Define here models or additionnal fields.o

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Improvement(models.Model):
    """
    Stores bugs and amelioration proposals.
    """

    BUG = 0
    AMELIORATION = 1
    NEWFEATURE = 2

    MODES = (
        (BUG, _("Bug")),
        (AMELIORATION, _("Improvement")),
        (NEWFEATURE, _("New feature")),
    )

    class Meta:
        verbose_name = _("improvement")
        verbose_name_plural = _("improvements")

    title = models.CharField(max_length=255, verbose_name=_("title"))
    mode = models.IntegerField(choices=MODES, verbose_name=_("type"))
    description = models.TextField()
    barman = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="improvement_submitted",
        verbose_name=_("barman"),
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))
