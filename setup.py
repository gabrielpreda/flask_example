from setuptools import setup, find_packages

from version import __version__

test_requirements = [
    'pytest==4.0.1',
    'coverage==4.5.2',
    'pytest-cov==2.6.0'
]

setup(
    name='iri-model-api',
    packages=find_packages(exclude=["tests*"]),
    package_data={'': ['app.py', 'model']},
    extras_require={'test': test_requirements},
    version=__version__,
    description='Iris Model API',
    author='Gabriel Preda',
    author_email='gabi.preda@gmail.com',
    license='MIT',
    url='https://pypi.example.com',
    python_requires='>=3'
)
