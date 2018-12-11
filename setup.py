from setuptools import setup

setup(
    name='HelloDolly',
    version='1.0.1',
    packages=['hellodolly'],
    url='https://github.com/fmaida/hello-dolly-mkdocs-plugin',
    license='MIT',
    author='Francesco Maida',
    author_email='fran@cesco.it',
    description='Hello Dolly is a very simple mkdocs plugin.',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'hello-dolly = hellodolly:HelloDolly',
        ]
    },
)
