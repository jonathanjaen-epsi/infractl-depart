import yaml, json, typer, time, os, requests
from pathlib import Path
from datetime import datetime
from socket import create_connection

token = os.environ.get("API_TOKEN", "")
headers = {"Authorization": f"Bearer {token}"}
#r = requests.get("http://127.0.0.1", headers=headers, timeout=3)
#print(r.status_code)
#print(r.json())

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

@app.command()
def check(inventory_path: str = "./inventory.yaml",
          group: str = typer.Option(None)
):  
    try:
        with open(inventory_path) as f:
            w = yaml.safe_load(f)
            for i in w.get('hosts', []):
                for key, value in i.items():
                    if group and value != group:
                        continue
                    try:
                        t0 = time.perf_counter()
                        try:
                            with create_connection((i.get('address'), i.get('port')), timeout=2):
                                ms = (time.perf_counter() - t0) * 1000
                                print(i.get('name'), "OK", i.get('check'), f"{int(ms)}ms")
                        except TimeoutError:
                            print("KO : timeout")
                    except ConnectionRefusedError:
                            print("KO : refusé")
                    except OSError as e:
                            print("KO :", e)
                    ms = (time.perf_counter() - t0) * 1000
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

