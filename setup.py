import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shortsdl",
    version="0.1.0",
    author="Abhishek Verma",
    author_email="insightfulverma@gmail.com",
    description="A short video downloader for platforms like TikTok, Instagram, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w3Abhishek/shortsdl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'shortsdl=shortsdl.cli:main',
        ],
    },
    install_requires=[
        "requests",
    ],
)
