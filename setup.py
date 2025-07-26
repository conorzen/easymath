from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="realmaths",
    version="1.0.2",
    author="Conor Reid",
    author_email="conoreid@me.com",
    description="Natural mathematical expressions for non-programmers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/conorzen/realmaths",
project_urls={
    "Bug Tracker": "https://github.com/conorzen/realmaths/issues",
    "Documentation": "https://github.com/conorzen/realmaths#readme",
    "Source Code": "https://github.com/conorzen/realmaths",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    keywords=[
        "mathematics", 
        "calculator", 
        "expressions", 
        "education", 
        "natural-language", 
        "non-programmer",
        "math-notation",
        "student-friendly"
    ],
    entry_points={
        "console_scripts": [
            "realmaths=realmaths.cli:main", 
        ],
    },
)