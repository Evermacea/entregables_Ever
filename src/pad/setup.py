from setuptools import setup, find_packages

setup(
    name="pad",
    version="0.0.1",
    author="Ever Macea",
    author_email="ever.macea@est.iudigital.edu.co",
    description="",
    py_modules=["actividad_1", "actividad_2","actividad_3"],
    install_requires=[
        "pandas",
        "matplotlib>=3.5.0",
        "plotly",
        "requests",
        "seaborn>=0.11.2",
        "openpyxl",
        "kagglehub[pandas-datasets]>=0.3.8"
    ],
)