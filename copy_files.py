import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("destination", default="dist", nargs="?")
args = parser.parse_args()
source = Path(args.source)
destination = Path(args.destination)

def copy_files(source, destination):
    for item in source.iterdir():
        try:
            if item.is_dir():
                copy_files(item, destination)
            elif item.is_file():
                ext = item.suffix
                ext_dir = destination / ext[1:]
                ext_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(item, ext_dir)
        except Exception as e:
            print(f"Помилка: {e}")

copy_files(source, destination)
