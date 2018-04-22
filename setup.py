from setuptools import setup

setup(
    name='HelloDolly',
    version='1.0.0',
    packages=['hellodolly'],
    url='',
    license='',
    author='Francesco Maida',
    author_email='francesco.maida@gmail.com',
    description='Hello Dolly is a very simple mkdocs plugin.',
    install_requires=['mkdocs'],


    entry_points={
        'mkdocs.plugins': [
            'hello-dolly = hellodolly:HelloDolly',
        ]
    },
)
