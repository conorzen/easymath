from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easymath",
    version="1.0.0",
    author="Conor Reid",
    author_email="conoreid@me.com",
    description="Natural mathematical expressions for non-programmers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/conorzen/easymath",
    project_urls={
        "Bug Tracker": "https://github.com/conorzen/easymath/issues",
        "Documentation": "https://github.com/conorzen/easymath#readme",
        "Source Code": "https://github.com/conorzen/easymath",
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
            "easymath=easymath.cli:main", 
        ],
    },
)