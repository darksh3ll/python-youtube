import time

import typer
from rich.progress import track


def main():
    total = 0
    for value in track(range(1000), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


main()
# if __name__ == "__main__":
#     typer.run(main)