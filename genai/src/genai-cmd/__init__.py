from setuptools import setup

setup(
    name='genai-cmd',
    version='1.0.1',
    packages=['genai'],
    entry_points={
        'console_scripts': [
            'gnenai=genai-cmd.genai-cmd:main',
        ],
    }
)