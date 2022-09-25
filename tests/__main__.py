"""
Evaluate unit tests for the ANIAnimator library.
"""
from __future__ import absolute_import
from .tests import test_animate, test_split_ani, test_write_xyzs, test_write_pngs
from .testers import clear_temp

clear_temp()
test_animate()
clear_temp()
test_split_ani()
clear_temp()
test_write_xyzs()
clear_temp()
test_write_pngs()
clear_temp()
