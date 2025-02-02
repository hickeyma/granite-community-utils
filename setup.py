# my_granite_package/setup.py

from setuptools import setup, find_packages

setup(
    name='ibm_granite_community',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'langchain_community<0.3.0',
        "langchain_ollama<0.2.0",
        "replicate",
        "langchain-pinecone",
        "langchain-milvus",
        "langchain-chroma",
        "langchain_ibm",
        "langchain_huggingface",
        "requests==2.32.3", # This is a `google-colab 1.0.0` dependency
    ],
    author='The IBM Granite Community Team',
    author_email='trevor.d.grant@gmail.com',
    description='A utility package of utility functions for IBM Granite Community notebooks.',
    url='https://github.com/ibm-granite-community/utils',
    keywords='notebook colab api key granite',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
