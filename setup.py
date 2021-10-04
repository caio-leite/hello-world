import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="caioleite",
    version="1.1.1",
    author="caioleite",
    author_email="caioleite@grupoboticario.com.br",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/caio-leite/hello-world",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'dask==2021.2.0',
        'numpy==1.21.0',
        'pandas==1.3.0',
        'pandas_gbq==0.15.0',
        'psycopg2-binary',
        'pysftp==0.2.9',
        'urllib3==1.24.1',
        'googleads==21.0.0',
        'google-cloud-bigquery==1.18.0',
        'google-cloud-core==1.0.3',
        'pymongo==3.11.0',
        'SQLAlchemy==1.3.5',
    ],
)
