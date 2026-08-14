# cli.py — Command Line Tool
import json
import argparse

from pci_defi_analysis_suite.main import run_defi_analysis


def main():
    parser = argparse.ArgumentParser(description="PCI DeFi Analysis CLI")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    result = run_defi_analysis()
    if args.pretty:
        print(json.dumps(result, indent=4))
    else:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
