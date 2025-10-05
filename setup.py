from setuptools import setup, find_packages

setup(
    name="orpheussay",
    version="0.1.1",
    description="A cowsay-like tool with Orpheus ASCII art :3",
    author="Nullsec0x",
    author_email="contact@nullsec0x.dev",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "orpheussay=orpheussay.__main__:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
