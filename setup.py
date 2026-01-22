from setuptools import setup, find_packages

setup(
    name="APITestDataGen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0",
        "click>=8.0",
        "pytest>=7.0",
        "requests>=2.28",
        "openapi-spec-validation>=0.5.0",
    ],
)
