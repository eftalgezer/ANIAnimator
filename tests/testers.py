"""
Unit testers for the ANIAnimator library.
"""
import glob
import os
import shutil
from ANIAnimator import __file__ as mfile
from ANIAnimator.core import animate
from ANIAnimator.helpers import split_ani, write_xyzs, write_pngs

mpath = mfile.replace("/ANIAnimator/__init__.py", "")


def clear_temp():
    """Clears the temp folder"""
    for filename in os.listdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp"):
        filepath = os.path.join(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp", filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print(f'Failed to delete {filepath}. Reason: {e}')


def animate_tester(anifile=None, width=None, height=None, loop=None, bonds_param=None):
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
    return split_ani(anifile)


def write_xyzs_tester(xyzs):
    return write_xyzs(xyzs)


def write_pngs_tester(xyzfiles, width=None, height=None, bonds_param=None):
    return write_pngs(xyzfiles, width=width, height=height, bonds_param=bonds_param)
