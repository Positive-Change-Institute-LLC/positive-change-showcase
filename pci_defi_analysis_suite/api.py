# api.py — FastAPI Wrapper
from fastapi import FastAPI
from pci_defi_analysis_suite.main import run_defi_analysis

app = FastAPI(title="PCI DeFi Analysis API")


@app.get("/analysis")
def get_analysis():
    return run_defi_analysis()
