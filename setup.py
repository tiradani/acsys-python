import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acsys",
    version="1.0.0rc7",
    author="Rich Neswold",
    author_email="neswold@fnal.gov",
    description="ACSys Client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cdcvs.fnal.gov/redmine/projects/py/wiki/Acsys",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'gssapi',
        'nest_asyncio',
        'importlib-metadata; python_version < "3.8"',
    ],
    extras_require={  # Optional
        'settings': ['gssapi']
    },
    python_requires='>=3.6',
)
