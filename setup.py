
from setuptools import setup

setup(
    name='salimcli',
    version='0.1',
    packages=['salimcli'],
    entry_points={
        'console_scripts': [
            'fortune-salim = salimcli.__main__:main'
        ]
    },
    install_requires=[
        'requests',
    ],
    author='Cappy Ishihara',
    author_email='cappy@cappuchino.xyz',
    description='Random salim quotes in your terminal',
    license='MIT',
    keywords='api, python, cli, quotes, politics, thailand',
    url='https://github.com/korewaChino/salimcli',
)
