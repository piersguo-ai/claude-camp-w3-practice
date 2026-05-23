import json
from pathlib import Path

import pandas as pd


INPUT_FILE = Path("students.csv")
OUTPUT_FILE = Path("report.json")


def build_report(dataframe: pd.DataFrame) -> dict:
    total_students = int(len(dataframe))
    country_counts = dataframe["country"].value_counts().sort_index().to_dict()
    completed_count = int(dataframe["bet_status"].eq("completed").sum())
    completion_rate = completed_count / total_students if total_students else 0.0

    return {
        "total_students": total_students,
        "students_by_country": country_counts,
        "bet_completion_rate": round(completion_rate, 2),
    }


def main() -> None:
    dataframe = pd.read_csv(INPUT_FILE, parse_dates=["joined_date"])
    report = build_report(dataframe)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Report saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
