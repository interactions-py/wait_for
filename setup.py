import re

from setuptools import setup

with open("interactions/ext/wait_for/base.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="interactions-wait-for",
    version=version,
    description="Add a wait_for function to discord-py-interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Catalyst4222/interactions-wait-for",
    author="Catalyst4",
    author_email="catalyst4222@gmail.com",
    license="MIT",
    packages=["interactions.ext.wait_for"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["discord-py-interactions>=4.1.0"],
)
