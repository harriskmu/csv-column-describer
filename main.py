import sys
from describer import describe_columns

if len(sys.argv) < 2:
    print("Usage: python main.py your_file.csv")
    sys.exit(1)

csv_path = sys.argv[1]

print(f"\nReading: {csv_path}\n")
describe_columns(csv_path)
