"""
Unit testers for the ANIAnimator library.
"""
from __future__ import absolute_import
import glob
import os
import shutil
import io
import sys
import re
from ANIAnimator import __file__ as mfile
from ANIAnimator.core import animate
from ANIAnimator.helpers import split_ani, write_xyzs, write_pngs

MPATH = mfile.replace("/ANIAnimator/__init__.py", "")


def clear_temp():
    """Clears the temp folder"""
    for filename in os.listdir("{0}{1}tests{1}assets{1}temp".format(MPATH, os.sep)):
        filepath = os.path.join("{0}{1}tests{1}assets{1}temp".format(MPATH, os.sep), filename)
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)


def sort_(files):
    """Naive sort function for files"""
    sortedfiles = []
    match = [re.search(r"{0}([0-9]+)\.[A-Za-z]+".format(os.sep), file) for file in files]
    sortedmatch = [[m.group(0), m.group(1)] for m in match]
    sortedmatch = [x for _, x in sorted(zip([int(m[1]) for m in sortedmatch], sortedmatch))]
    for s in sortedmatch:
        for file in files:
            filematch = re.search(r"{0}[0-9]+\.[A-Za-z]+".format(os.sep), file)
            if s[0] == filematch.group(0) and file not in sortedfiles:
                sortedfiles.append(file)
    return sortedfiles


def animate_tester(anifile=None, width=None, height=None, loop=None, bonds_param=None):
    """Tester function for animate"""
    fname = anifile.split(".")[0]
    animate(
        anifile=anifile,
        width=width,
        height=height,
        loop=loop,
        bonds_param=bonds_param
    )
    return list(glob.glob("{0}.gif".format(fname)))


def split_ani_tester(anifile):
    """Tester function for split_ani"""
    return split_ani(anifile)


def write_xyzs_tester(xyzs):
    """Tester function for write_xyzs"""
    return write_xyzs(xyzs)


def write_pngs_tester(xyzfiles, width=None, height=None, bonds_param=None):
    """Tester function for write_pngs"""
    return write_pngs(xyzfiles, width=width, height=height, bonds_param=bonds_param)


def main_tester(command):
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    from ANIAnimator.__main__ import main as rtmain
    rtmain(args=command.split(" "))
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()
