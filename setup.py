from setuptools import setup, find_packages

setup(
    name="codescanning",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your project dependencies here
    ],
)