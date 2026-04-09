import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def describe_columns(csv_path: str):
    df = pd.read_csv(csv_path)

    column_info = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        sample_values = df[col].dropna().head(3).tolist()
        column_info.append({
            "column": col,
            "type": dtype,
            "samples": sample_values
        })

    prompt = f"""
You are a data analyst. Below is a list of columns from a CSV dataset.
For each column, write a short one-sentence plain English description of what it likely represents.

Return your response as a markdown table with these columns:
| Column | Type | Description |

Here are the columns:

{column_info}

Be concise. No extra commentary before or after the table.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
