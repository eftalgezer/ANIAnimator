"""
Setup file for ANIanimator
"""
from __future__ import absolute_import
import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent.resolve()

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="ANIAnimator",
    version="0.0.1",
    description="ANIAnimator makes the GIF file from a given chemical ANI file",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eftalgezer/ANIanimator",
    author="Eftal Gezer",
    author_email="eftal.gezer@astrobiyoloji.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="ANI, GIF, animation, molecular calculations, chemistry, physics," +
    "ANI to GIF converter",
    packages=["ANIAnimator"],
    install_requires=[
        "mogli",
        "pillow",
        ],
    project_urls={
        "Bug Reports": "https://github.com/eftalgezer/ANIAnimator/issues",
        "Source": "https://github.com/eftalgezer/ANIAnimator/",
        "Blog": "https://beyondthearistotelian.blogspot.com/search/label/ANIAnimator",
        "Developer": "https://www.eftalgezer.com/",
    },
)
