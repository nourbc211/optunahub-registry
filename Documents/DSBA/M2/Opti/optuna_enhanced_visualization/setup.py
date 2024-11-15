from setuptools import setup, find_packages

setup(
    name="optuna_enhanced_visualization",
    version="0.1.0",
    description="Enhanced visualization tools for Optuna.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "optuna",
        "numpy",
        "plotly",
    ],
    python_requires=">=3.7",
)
