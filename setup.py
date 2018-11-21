# Copyright 2018 ImpactoJOR <https://github.com/Impacto-jor/fetchrss-api/>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.

#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
from setuptools import setup, find_packages


base_path = Path(__file__).parent
with open(base_path / "README.md", encoding="utf-8") as fobj:
    readme_contents = fobj.read()

setup(
    name="fetchrss-api",
    description="A simple interface for FetchRSS.com API",
    long_description=readme_contents,
    long_description_content_type="text/markdown",
    version="0.1.4",
    author="Álvaro Justen",
    author_email="alvarojusten@gmail.com",
    url="https://github.com/Impacto-jor/fetchrss-api/",
    py_modules=["fetchrss"],
    install_requires=["requests", "feedparser"],
    keywords="api rss facebook instagram",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
