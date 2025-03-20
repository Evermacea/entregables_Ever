from setuptools import setup, find_namespace_packages

from setuptools import setup

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
        "plotly",
        "requests"  # Asegurar que 'requests' está aquí
    ],
    zip_safe=False,
)

