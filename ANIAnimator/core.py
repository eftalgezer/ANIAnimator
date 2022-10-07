"""
Module bundling all functions needed to animate an ANI file
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import shutil
from PIL import Image
from .helpers import split_ani, write_xyzs, write_pngs


def animate(anifile=None, width=None, height=None, loop=None, bonds_param=None, camera=None):
    """Create a gif file from given ANI file"""
    if width is None:
        width = 1920
    if height is None:
        height = 1080
    if loop is None:
        loop = 0
    if bonds_param is None:
        bonds_param = 1.3
    fname = anifile.split(".")[0]
    frames = []
    imgfiles = write_pngs(write_xyzs(split_ani(anifile)), width, height, bonds_param, camera)
    print("")
    for i, imgfile in enumerate(imgfiles):
        print("Creating GIF ({0}/{1})".format(i + 1, len(imgfiles)), end="\r")
        new_frame = Image.open(imgfile)
        frames.append(new_frame)
    frames[0].save("{0}.gif".format(fname),
                   format="GIF",
                   append_images=frames[1:],
                   save_all=True,
                   duration=300,
                   loop=loop,
                   disposal=2)
    print("\n{0}.gif is created".format(fname))
    print("Deleting directory ANIAnimator_temp")
    shutil.rmtree("ANIAnimator_temp")
    print("Directory ANIAnimator_temp is deleted")
