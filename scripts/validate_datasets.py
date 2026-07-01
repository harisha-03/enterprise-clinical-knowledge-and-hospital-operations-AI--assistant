import pandas as pd
from pathlib import Path

DATASET_DIR = Path("datasets")

files = sorted(DATASET_DIR.glob("*.csv"))

print("=" * 70)
print("DATASET VALIDATION REPORT")
print("=" * 70)

for file in files:
    try:
        df = pd.read_csv(file)

        print(f"\n📄 {file.name}")
        print(f"Rows    : {len(df):,}")
        print(f"Columns : {len(df.columns)}")
        print(f"Headers : {', '.join(df.columns)}")

    except Exception as e:
        print(f"\n❌ {file.name}")
        print(e)

print("\n" + "=" * 70)
print("Validation Complete")
print("=" * 70)