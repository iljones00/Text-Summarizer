import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "iljones00"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "isaiahlkjones00@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for text summarization application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iljones00/textSummarizer",
    project_urls={
        "Bug Tracker": "https://github.com/iljones00/textSummarizer/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)


