
from setuptools import setup, find_packages

import os

def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
            return f.read()
    except Exception:
        return ''

setup(
    name='github-pr-summarizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-generativeai>=0.3.2',
        'requests>=2.31.0',
        'python-dotenv>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pr-summary=main:main',
        ],
    },
    author='Your Name',
    description='A GitHub Action bot that summarizes pull requests using Google Gemini API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)