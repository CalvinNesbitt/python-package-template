from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.1",
    description="This is a package.",
    author="Calvin Nesbitt",
    author_email="cf.nesbitt94@gmail.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
)
