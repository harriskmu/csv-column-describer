# CSV Column Describer

A Python tool that reads a CSV file and automatically generates a data dictionary — 
column names, data types, and a plain English description of what each column likely means.

Wrote this because documenting datasets manually is tedious and nobody ever does it properly.
This makes it automatic.

---

## What it does

- Reads any CSV file you point it at
- Detects column names and data types automatically
- Uses the OpenAI API to generate a plain English description for each column
- Outputs a clean markdown data dictionary you can save or share

---

## Setup

1. Clone the repo
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key to a `.env` file
OPENAI_API_KEY=your_key_here

4. Run it

```bash
python main.py your_file.csv
```

---

## Example output
ColumnTypeDescriptioncustomer_idintegerUnique identifier for each customersignup_dateobjectThe date the customer created their accounttotal_spendfloatCumulative amount spent by the customer in USDis_activebooleanWhether the customer has activity in last 90 days

---

## File structure
csv-column-describer/
├── main.py
├── describer.py
├── sample_data.csv
├── requirements.txt
├── .env.example
└── README.md

---

## Notes

- Works with any standard CSV file
- Larger CSVs only send column names and sample rows to the API — not the full file
- Built for internal data teams who need quick documentation turnaround

---

## Requirements

- Python 3.9+
- OpenAI API key
