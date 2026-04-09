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
