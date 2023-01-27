"""
Helper functions for ANIAnimator
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals
import os
import io
import re
import mogli

ANI_PATTERN = re.compile(
    r"([ \t]+[0-9]+\n" +
    r".*\n" +
    r"(\S+[ \t]+-?[0-9]+\.[0-9]+[ \t]+-?[0-9]+\.[0-9]+[ \t]+-?[0-9]+\.[0-9]+\n)+)"
)


def split_ani(anifile):
    """Split ANI files to xyz"""
    with io.open(anifile, "r", encoding="utf-8") as file:
        print("Opening {0}".format(anifile))
        ani = file.read()
        file.close()
        return ANI_PATTERN.findall(ani)


def write_xyzs(xyzs):
    """Write xyz files"""
    xyzfiles = []
    print("Making directory ANIAnimator_temp")
    if not os.path.exists("ANIAnimator_temp"):
        os.mkdir("ANIAnimator_temp")
    for i, xyz in enumerate(xyzs):
        with io.open("ANIAnimator_temp{0}{1}.xyz".format(os.sep, i), "w", encoding="utf-8") as file:
            print("Creating xyz files ({0}/{1})".format(i + 1, len(xyzs)), end="\r")
            file.write(xyz[0])
            file.close()
        xyzfiles.append("ANIAnimator_temp{0}{1}.xyz".format(os.sep, i))
    return xyzfiles


def write_pngs(xyzfiles, width=None, height=None, bonds_param=None, camera=None):
    """Write png files"""
    if width is None:
        width = 1920
    if height is None:
        height = 1080
    if bonds_param is None:
        bonds_param = 1.3
    pngfiles = []
    print("")
    for i, xyzfile in enumerate(xyzfiles):
        molecules = mogli.read(xyzfile)
        print("Creating png files ({0}/{1})".format(i + 1, len(xyzfiles)), end="\r")
        mogli.export(
            molecules[0],
            "ANIAnimator_temp{0}{1}.png".format(os.sep, i),
            width=width,
            height=height,
            bonds_param=bonds_param,
            camera=camera
        )
        pngfiles.append("ANIAnimator_temp{0}{1}.png".format(os.sep, i))
    return pngfiles
