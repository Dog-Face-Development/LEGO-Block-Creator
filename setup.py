"""Setup file for LEGO Block Creator."""

from setuptools import setup


def readme():
    """Read the README.md file."""
    with open("README.md", encoding="UTF-8") as f:
        return f.read()


setup(
    name="lego-block-creator",
    version="0.3.0",
    description="Offline inventory tracking of LEGO parts and sets through an easy to use CLI.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    keywords="lego block blocks inventory sets sort cli",
    url="https://github.com/Dog-Face-Development/LEGO-Block-Creator",
    author="willtheorangeguy",
    entry_points={"console_scripts": ["lego-block-creator=main:lego_cmd"]},
)
