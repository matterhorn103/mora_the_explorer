"""
Mora the Explorer checks for new NMR spectra at the Organic Chemistry department at the University of Münster.
Copyright (C) 2023 Matthew J. Milner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
from pathlib import Path

import mora_the_explorer


def get_rsrc_dir():
    """Gets the location of the program's resources, which is platform-dependent."""
    # For whatever reason __file__ doesn't give the right location on a mac when a .app has
    # been generated with pyinstaller
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    else:
        return Path(__file__).parent


if __name__ == "__main__":
    rsrc_dir = get_rsrc_dir()

    mora_the_explorer.run_desktop_app(rsrc_dir)
