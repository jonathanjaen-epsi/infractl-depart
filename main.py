import yaml, json, typer
from pathlib import Path
from datetime import datetime

app = typer.Typer()

@app.callback()
def main():
    """infractl-depart"""

@app.command()
def liste(inventory_path: str = "./inventory.yaml",
          group: str = typer.Option(None)
):  
    try:
        with open(inventory_path) as f:
            w = yaml.safe_load(f)
            for i in w.get('hosts', []):
                for key, value in i.items():
                    if group and value != group:
                        continue
                    print(f"{i.get('name')} {i.get('address')}:{i.get('port')} {value}")

    except FileNotFoundError:
        print(f"{inventory_path} introuvable")


if __name__ == "__main__":
    app()

def main():
    print("Hello from infractl-depart!")

if __name__ == "__main__":
    main()

path = Path("inventory.yaml")
try:
    text = path.read_text()
except FileNotFoundError:
    print(f"{path} introuvable")

