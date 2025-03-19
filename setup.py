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
        "plotly"  # Aquí debe ser "plotly", NO "plotly.express"
    ],
)