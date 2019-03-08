from setuptools import setup

setup(
    name='requests-filecache',
    version='0.0.2',
    packages=['requests_filecache'],
    url='https://github.com/strizhechenko/requests-filecache',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description='Saves fetched HTML into files in current directory.',
    install_requires=['requests']
)
