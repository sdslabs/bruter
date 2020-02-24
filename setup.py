import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bruter",
    version="0.0.2",
    author="SDSLabs",
    author_email="contact@sdslabs.co.in",
    description="String bruteforcer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdslabs/bruter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
