import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="SiSedeInversiones",
    version="0.0.1",  
    author="Jelsin Stalin Palomino Huaytapuma",
    author_email="jstpalomino@hotmail.com",
    description="This package is dedicated to automating the extraction of data found in the Peruvian state's Investment Monitoring System - SSI portal, where public investment projects in Peru can be monitored through Unique Investment Codes (CUI).",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JelsinPalomino/SiSedeInversiones",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Microsoft ",
        "Intended Audience :: Education",
    ],
    install_requires=["pandas", "rpa", "openpyxl"],
    keywords=['web-scraping', 'Peru', 'rpa', 'SSI'],
)