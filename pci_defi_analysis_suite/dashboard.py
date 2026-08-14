# dashboard.py — Rich Terminal Dashboard
from rich.table import Table
from rich.console import Console

from pci_defi_analysis_suite.main import run_defi_analysis


def render_dashboard():
    console = Console()
    data = run_defi_analysis()

    table = Table(title="PCI DeFi Structural Analysis")
    table.add_column("Module", style="cyan", no_wrap=True)
    table.add_column("Key", style="magenta")
    table.add_column("Value", style="green")

    for module_name in ["amm", "lp", "yield", "lending", "bridge", "routing"]:
        module = data[module_name]
        for k, v in module.items():
            table.add_row(module_name, k, str(v))

    console.print(table)
    console.print(f"\nResilience Score: {data['resilience_score']}")


if __name__ == "__main__":
    render_dashboard()
