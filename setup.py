import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


install_requires = [
    'requests>=2.9.1',
    'markdown>=2.6.0',
    'open-humans-api>=0.2.2',
]

setuptools.setup(
    name="jupyter-notebook-importer",
    version="0.0.1",
    author="Bastian Greshake Tzovaras",
    author_email="bgreshake@gmail.com",
    description="Import a notebook from Open Humans",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gedankenstuecke/jupyter-bundler-openhumans",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)