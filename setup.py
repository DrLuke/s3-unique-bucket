from setuptools import setup
from pathlib import Path

with Path(__file__).parent.joinpath("README.md").open(encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="s3_unique_bucket",
    version="0.1.0",
    description="Insures a unique S3 bucket exists for the account",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/DrLuke/s3-unique-bucket",
    author="Lukas Jackowski",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    keywords="aws s3 bucket unique ci cd",

    python_requires=">=3.6, <4",
    install_requires=["boto3"],

    py_modules=["s3_unique_bucket"],
    entry_points={
        "console_scripts": [
            "s3_unique_bucket=s3_unique_bucket:main",
        ],
    },
)
