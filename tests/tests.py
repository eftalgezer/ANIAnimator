"""
Unit tests for the ANIAnimator library.
"""
from __future__ import absolute_import
import os
import shutil
import glob
from ANIAnimator import __file__ as mfile
from .testers import (
    sort_,
    animate_tester,
    split_ani_tester,
    write_xyzs_tester,
    write_pngs_tester,
    main_tester
)

MPATH = mfile.replace("/ANIAnimator/__init__.py", "")


def test_animate():
    """Tests for animate"""
    shutil.copy(
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI",
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-merged.ANI"
    )
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp")
    assert animate_tester("C-merged.ANI") == glob.glob("C-merged.gif")


def test_split_ani():
    """Tests for split_ani"""
    shutil.copy(
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI",
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-merged.ANI"
    )
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp")
    assert split_ani_tester("C-merged.ANI") == [
        (
            "    2\n \nC       0.037417    0.000000   -0.000000\nC       1.962580   -0.000000   -0.000000\n",
            "C       1.962580   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.090331    0.000000   -0.000000\nC       1.909662   -0.000000   -0.000000\n",
            "C       1.909662   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.143244    0.000000   -0.000000\nC       1.856745   -0.000000   -0.000000\n",
            "C       1.856745   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.196158    0.000000   -0.000000\nC       1.803827   -0.000000   -0.000000\n",
            "C       1.803827   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.166174    0.000000   -0.000000\nC       1.833813   -0.000000   -0.000000\n",
            "C       1.833813   -0.000000   -0.000000\n"
        ),
        ("    2\n \nC       0.219091   -0.000000   -0.000000\nC       1.878644    0.000000    0.000000\n",
         "C       1.878644    0.000000    0.000000\n"
         ),
        ("    2\n \nC       0.176136   -0.000000   -0.000000\nC       1.842253    0.000000    0.000000\n",
         "C       1.842253    0.000000    0.000000\n"
         ),
        (
            "    2\n \nC       0.213585    0.000000   -0.000000\nC       1.804865    0.000000   -0.000000\n",
            "C       1.804865    0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.266503    0.000000   -0.000000\nC       1.752035    0.000000   -0.000000\n",
            "C       1.752035    0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.319421    0.000000   -0.000000\nC       1.699204    0.000000   -0.000000\n",
            "C       1.699204    0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.269022    0.000000   -0.000000\nC       1.749520    0.000000   -0.000000\n",
            "C       1.749520    0.000000   -0.000000\n"
        ),
        ("    2\n \nC       0.306420   -0.000000   -0.000000\nC       1.712082   -0.000000    0.000000\n",
         "C       1.712082   -0.000000    0.000000\n"
         ),
        ("    2\n \nC       0.306420   -0.000000   -0.000000\nC       1.712082   -0.000000    0.000000\n",
         "C       1.712082   -0.000000    0.000000\n"
         ),
        (
            "    2\n \nC       0.359281   -0.000000   -0.000000\nC       1.659164   -0.000000    0.000000\n",
            "C       1.659164   -0.000000    0.000000\n"
        ), (
            "    2\n \nC       0.306420   -0.000000   -0.000000\nC       1.712082   -0.000000    0.000000\n",
            "C       1.712082   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.359281   -0.000000   -0.000000\nC       1.659164   -0.000000    0.000000\n",
            "C       1.659164   -0.000000    0.000000\n"
        ),
        ("    2\n \nC       0.333370   -0.000000   -0.000000\nC       1.685103   -0.000000    0.000000\n",
         "C       1.685103   -0.000000    0.000000\n"
         ),
        ("    2\n \nC       0.386288   -0.000000   -0.000000\nC       1.637408   -0.000000   -0.000000\n",
         "C       1.637408   -0.000000   -0.000000\n"
         ),
        ("    2\n \nC       0.335327   -0.000000   -0.000000\nC       1.683340   -0.000000   -0.000000\n",
         "C       1.683340   -0.000000   -0.000000\n"
         ),
        (
            "    2\n \nC       0.337208   -0.000000   -0.000000\nC       1.681497    0.000000    0.000000\n",
            "C       1.681497    0.000000    0.000000\n"
        ),
        ("    2\n \nC       0.335673   -0.000000   -0.000000\nC       1.683000   -0.000000   -0.000000\n",
         "C       1.683000   -0.000000   -0.000000\n"
         ),
        (
            "    2\n \nC       0.373094    0.000000   -0.000000\nC       1.645584   -0.000000    0.000000\n",
            "C       1.645584   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.426012    0.000000   -0.000000\nC       1.592674   -0.000000    0.000000\n",
            "C       1.592674   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.380780    0.000000   -0.000000\nC       1.637899   -0.000000    0.000000\n",
            "C       1.637899   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.423654   -0.000000    0.000000\nC       1.590669   -0.000000   -0.000000\n",
            "C       1.590669   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.382121   -0.000000    0.000000\nC       1.636423   -0.000000   -0.000000\n",
            "C       1.636423   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.383517   -0.000000   -0.000000\nC       1.634999    0.000000    0.000000\n",
            "C       1.634999    0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.382434   -0.000000   -0.000000\nC       1.636103   -0.000000   -0.000000\n",
            "C       1.636103   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.419848   -0.000000   -0.000000\nC       1.598680   -0.000000    0.000000\n",
            "C       1.598680   -0.000000    0.000000\n"
        ), (
            "    2\n \nC       0.414689   -0.000000   -0.000000\nC       1.603840   -0.000000    0.000000\n",
            "C       1.603840   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.447199   -0.000000    0.000000\nC       1.571835   -0.000000   -0.000000\n",
            "C       1.571835   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.416174   -0.000000    0.000000\nC       1.602378   -0.000000   -0.000000\n",
            "C       1.602378   -0.000000   -0.000000\n"
        ),
        (
            "    2\n \nC       0.417654   -0.000000   -0.000000\nC       1.600911   -0.000000    0.000000\n",
            "C       1.600911   -0.000000    0.000000\n"
        ),
        (
            "    2\n \nC       0.416416   -0.000000   -0.000000\nC       1.602139   -0.000000   -0.000000\n",
            "C       1.602139   -0.000000   -0.000000\n"
        )
    ]


def test_write_xyzs():
    """Tests for write_xyzs"""
    shutil.copy(
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI",
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-merged.ANI"
    )
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp")
    assert write_xyzs_tester(split_ani_tester("C-merged.ANI")) == sort_(glob.glob("ANIAnimator_temp/*.xyz"))


def test_write_pngs():
    """Tests for write_pngs"""
    shutil.copy(
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI",
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-merged.ANI"
    )
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp")
    assert write_pngs_tester(write_xyzs_tester(split_ani_tester("C-merged.ANI"))) == sort_(
        glob.glob("ANIAnimator_temp/*.png"))

def test_main():
    shutil.copy(
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI",
        f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-merged.ANI"
    )
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets{os.sep}temp")
    assert "is created" in main_tester("ANIAnimator C-merged.ANI")
