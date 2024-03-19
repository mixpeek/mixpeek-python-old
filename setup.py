from setuptools import setup, find_packages


setup(
    name="mixpeek",
    version="0.2",
    license="MIT",
    author="Ethan Steininger",
    author_email="info@mixpeek.com",
    packages=["mixpeek"],
    url="https://github.com/mixpeek/mixpeek-python",
    keywords="file search",
    description="full-text file search API",
    install_requires=["requests"],
)
