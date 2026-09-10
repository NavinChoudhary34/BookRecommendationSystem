from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "BookRecommendationSystem"
AUTHOR_USER_NAME = "Navin Choudhary"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Navin Choudhary",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NavinChoudhary34/BookRecommendationSystem.git",
    author_email="navin.r.choudharylj@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.12.10",
    install_requires=LIST_OF_REQUIREMENTS
)