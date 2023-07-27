import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firerip",
    version="0.0.1",
    author="Sayed Ahmed",
    description="A CLI tool to download courses from https://fireship.io",
    author_email="sayeed205@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: MIT LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4>=4.12.2",
        "inquirer>=3.1.3",
        "Requests>=2.31.0",
        "yt_dlp>=2023.7.6",
    ],
    entry_points={"console_scripts": ["firerip=firerip.main:main"]},
)
