from setuptools import setup, find_namespace_packages

setup(
    name="pad",
    version="0.0.1",
    author="Ever Macea",
    author_email="ever.macea@est.iudigital.edu.co",
    description="",
    py_modules=["actividad_1"],
    install_requires=[
        "pandas",
        "matplotlib",
        "plotly",  # Aquí debe ser "plotly", NO "plotly.express"
        "requests" # Agregamos requests aquí
    ],
    py_modules=["actividad_2"],
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn>=0.11.2",
        "plotly",  
        "requests",
        "openpyxl",
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0"
    ],
)
