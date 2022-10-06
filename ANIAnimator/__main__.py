"""
Terminal client for ANIAnimator
"""

from __future__ import absolute_import
import sys
from .core import animate


def main(args):
    """Main function"""
    width = None
    height = None
    loop = None
    bonds_param = None
    camera = None
    try:
        width = args[2]
    except IndexError:
        pass
    try:
        height = args[3]
    except IndexError:
        pass
    try:
        loop = args[4]
    except IndexError:
        pass
    try:
        bonds_param = args[5]
    except IndexError:
        pass
    try:
        camera = args[6]
    except IndexError:
        pass
    if width is None:
        width = 1920
    if height is None:
        height = 1080
    if loop is None:
        loop = 1
    if bonds_param is None:
        bonds_param = 1.3
    if camera == "default":
        camera = None
    elif camera is not None:
        cameraparams = camera.split(",")
        camera = (
            (int(cameraparams[0]), int(cameraparams[1]), int(cameraparams[2])),
            (int(cameraparams[3]), int(cameraparams[4]), int(cameraparams[5])),
            (int(cameraparams[6]), int(cameraparams[7]), int(cameraparams[8]))
        )
    animate(args[1], width, height, loop, bonds_param, camera)


if __name__ == "__main__":
    main(sys.argv)
