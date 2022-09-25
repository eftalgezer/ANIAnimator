"""
Unit testers for the ANIAnimator library.
"""
from __future__ import absolute_import
import glob
import os
import shutil
import re
from ANIAnimator import __file__ as mfile
from ANIAnimator.core import animate
from ANIAnimator.helpers import split_ani, write_xyzs, write_pngs

MPATH = mfile.replace("/ANIAnimator/__init__.py", "")


def clear_temp():
    """Clears the temp folder"""
    for filename in os.listdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp"):
        filepath = os.path.join(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp", filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print(f'Failed to delete {filepath}. Reason: {e}')


def sort_(files):
    """Naive sort function for files"""
    sortedfiles = []
    match = [re.search(rf"{os.sep}([0-9]+)\.[A-Za-z]+", file) for file in files]
    sortedmatch = [[m[0], m[1]] for m in match]
    sortedmatch = [x for _, x in sorted(zip([int(m[1]) for m in sortedmatch], sortedmatch))]
    for s in sortedmatch:
        for file in files:
            filematch = re.search(rf"{os.sep}[0-9]+\.[A-Za-z]+", file)
            if s[0] == filematch[0] and file not in sortedfiles:
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
    return list(glob.glob(f"{fname}.gif"))


def split_ani_tester(anifile):
    """Tester function for split_ani"""
    return split_ani(anifile)


def write_xyzs_tester(xyzs):
    """Tester function for write_xyzs"""
    return write_xyzs(xyzs)


def write_pngs_tester(xyzfiles, width=None, height=None, bonds_param=None):
    """Tester function for write_pngs"""
    return write_pngs(xyzfiles, width=width, height=height, bonds_param=bonds_param)
