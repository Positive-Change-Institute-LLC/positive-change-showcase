from setuptools import setup, find_packages

setup(
    name="pci_defi_analysis_suite",
    version="1.0.0",
    description="PCI Sovereign DeFi Architecture Analysis Suite",
    author="Christopher S. Rowland Sr.",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pydantic",
        "fastapi",
        "uvicorn",
        "rich",
    ],
)
