"""
Helper functions for ANIAnimator
"""

import os
import re
import mogli

ANI_PATTERN = re.compile(
    r"([ \t]+[0-9]+\n" +
    r".+\n" +
    r"(\S+[ \t]+-?[0-9]+\.[0-9]+[ \t]+-?[0-9]+\.[0-9]+[ \t]+-?[0-9]+\.[0-9]+\n)+)"
)


def split_ani(anifile):
    """Split ANI files to xyz"""
    with open(anifile, encoding="utf-8") as f:
        print(f"Opening {anifile}")
        ani = f.read()
        f.close()
        return ANI_PATTERN.findall(ani)


def write_xyzs(xyzs):
    """Write xyz files"""
    xyzfiles = []
    print("Making directory ANIAnimator_temp")
    if not os.path.exists("ANIAnimator_temp"):
        os.mkdir("ANIAnimator_temp")
    for i, xyz in enumerate(xyzs):
        with open(f"ANIAnimator_temp{os.sep}{i}.xyz", "w", encoding="utf-8") as f:
            print(f"Creating xyz files ({i + 1}/{len(xyzs)})", end="\r")
            f.write(xyz[0])
            f.close()
        xyzfiles.append(f"ANIAnimator_temp{os.sep}{i}.xyz")
    return xyzfiles


def write_pngs(xyzfiles, width=None, height=None, bonds_param=None):
    """Write png files"""
    if width is None:
        width = 1920
    if height is None:
        height = 1080
    if bonds_param is None:
        bonds_param = 1.3
    pngfiles = []
    print()
    for i, xyzfile in enumerate(xyzfiles):
        molecules = mogli.read(xyzfile)
        print(f"Creating png files ({i + 1}/{len(xyzfiles)})", end="\r")
        mogli.export(
            molecules[0],
            f"ANIAnimator_temp{os.sep}{i}.png",
            width=width,
            height=height,
            bonds_param=bonds_param
        )
        pngfiles.append(f"ANIAnimator_temp{os.sep}{i}.png")
    return pngfiles
