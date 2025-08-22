#!/usr/bin/env python3

import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def ensure_output_dir(directory: Path) -> None:
	"""Create plots output directory if it does not exist."""
	directory.mkdir(parents=True, exist_ok=True)


def load_dataset(csv_path: Path) -> pd.DataFrame:
	"""Load the students CSV into a DataFrame."""
	if not csv_path.exists():
		raise FileNotFoundError(f"CSV file not found at: {csv_path}")
	return pd.read_csv(csv_path)


def add_average_column(df: pd.DataFrame) -> pd.DataFrame:
	"""Compute per-student average across Math, Science, and English."""
	required_cols = ["Math", "Science", "English"]
	missing = [c for c in required_cols if c not in df.columns]
	if missing:
		raise ValueError(f"Missing required columns: {missing}")
	result = df.copy()
	result["Average"] = result[required_cols].mean(axis=1)
	return result


def find_top_student(df_with_avg: pd.DataFrame) -> pd.Series:
	"""Return the row corresponding to the student with the highest Average."""
	if "Average" not in df_with_avg.columns:
		raise ValueError("DataFrame must contain an 'Average' column")
	return df_with_avg.loc[df_with_avg["Average"].idxmax()]


def plot_average_bar_chart(df_with_avg: pd.DataFrame, out_dir: Path) -> Path:
	"""Generate and save a bar chart of average marks per student."""
	ensure_output_dir(out_dir)
	plt.figure(figsize=(8, 5))
	plt.bar(df_with_avg["Name"], df_with_avg["Average"], color="skyblue")
	plt.title("Average Marks of Students")
	plt.xlabel("Student Name")
	plt.ylabel("Average Marks")
	plt.ylim(0, 100)
	plt.tight_layout()
	out_path = out_dir / "average_marks.png"
	plt.savefig(out_path)
	plt.close()
	return out_path


def plot_subject_line_chart(df: pd.DataFrame, out_dir: Path) -> Path:
	"""Generate and save a line chart showing each student's marks by subject."""
	ensure_output_dir(out_dir)
	subjects = ["Math", "Science", "English"]
	plt.figure(figsize=(8, 5))
	for i in range(len(df)):
		plt.plot(subjects, df.iloc[i][subjects], marker="o", label=str(df.iloc[i]["Name"]))
	plt.title("Marks by Subject")
	plt.ylabel("Marks")
	plt.ylim(0, 100)
	plt.legend()
	plt.tight_layout()
	out_path = out_dir / "marks_by_subject.png"
	plt.savefig(out_path)
	plt.close()
	return out_path


def plot_marks_histogram(df: pd.DataFrame, out_dir: Path) -> Path:
	"""Generate and save a histogram of all marks across subjects."""
	ensure_output_dir(out_dir)
	all_marks = df[["Math", "Science", "English"]].values.flatten()
	plt.figure(figsize=(8, 5))
	plt.hist(all_marks, bins=5, edgecolor="black")
	plt.title("Distribution of All Marks")
	plt.xlabel("Marks")
	plt.ylabel("Frequency")
	plt.xlim(0, 100)
	plt.tight_layout()
	out_path = out_dir / "marks_distribution.png"
	plt.savefig(out_path)
	plt.close()
	return out_path


def main() -> None:
	project_root = Path(__file__).parent
	csv_path = project_root / "students.csv"
	plots_dir = project_root / "plots"

	# Step 2: Load Dataset
	df = load_dataset(csv_path)
	print("Data (head):")
	print(df.head())

	# Step 3: Calculate Average Marks
	df_with_avg = add_average_column(df)
	print("\nData with Average:")
	print(df_with_avg)

	# Step 4: Find Top Student
	top_student = find_top_student(df_with_avg)
	print("\nTop Student:")
	print(top_student)

	# Step 5/6: Visualize Results
	avg_chart = plot_average_bar_chart(df_with_avg, plots_dir)
	subject_chart = plot_subject_line_chart(df, plots_dir)
	hist_chart = plot_marks_histogram(df, plots_dir)
	print("\nSaved plots:")
	print(f"- {avg_chart}")
	print(f"- {subject_chart}")
	print(f"- {hist_chart}")


if __name__ == "__main__":
	main()
