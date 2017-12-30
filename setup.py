from setuptools import find_packages, setup

setup(
    name="microblog",
    version='0.1',
    description="Morepath microblog",
    author='Morepath developer',
    author_email='you@example.com',
    packages=find_packages(),
    install_requires=['morepath']
)
