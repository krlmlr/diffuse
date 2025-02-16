# Diffuse: a graphical tool for merging and comparing text files.
#
# Copyright (C) 2019 Derrick Moser <derrick_moser@yahoo.com>
# Copyright (C) 2021 Romain Failliot <romain.failliot@foolstep.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from gettext import gettext as _
from typing import Final

APP_NAME: Final[str] = 'Diffuse'
COPYRIGHT: Final[str] = '''{copyright} © 2006-2019 Derrick Moser
{copyright} © 2015-2021 Romain Failliot'''.format(copyright=_("Copyright"))
WEBSITE: Final[str] = 'https://mightycreak.github.io/diffuse/'

# Constants are set in main()
VERSION: str = '0.0.0'
