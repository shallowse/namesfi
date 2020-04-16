import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namesfi",
    version="0.0.1",
    author="Shallowse",
    author_email="noemail@example.com",
    description="Generate random Finnish names",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shallowse/namesfi",
    packages=setuptools.find_packages(),
    package_data={'namesfi': ['dist.*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
