# CSCI218 Labs 6 & 7 — corrected dataset version

**Source:** Your uploaded `humanitarian_shipments_1M.csv.gz` (1,000,000 rows, 23 columns). **No simulated records are generated.** The file stays compressed; pandas reads it directly.

## VS Code

1. Extract the ZIP and open this folder in VS Code.
2. Install Python and run `python -m pip install -r requirements.txt` in the terminal.
3. Run `python run_all.py`, or run any individual `Lab_6_Activities/activity_A.py` etc. from the root folder.
4. Read the written answers in each lab's `WRITTEN_ANSWERS.md`. Graphs are saved to `plots/`.

## Data size and reproducibility

By default scripts use a **reproducible random 20,000-row sample of your uploaded million-row dataset** so all activities run on a typical student laptop. The complete original 1M-row file is included unchanged. To process all million rows, set `CSCI218_SAMPLE_ROWS=0` before running; training 100/200-tree forests will be substantially slower and require much more memory. Each script loads the same seeded sample.

The actual dataset has different columns from the original instructor-generated 600-row example. The scripts correctly use `delivery_status` (On_Time vs Delayed) instead of `delivered_on_time`, `cargo_category` instead of `cargo_type`, and `priority_level` rather than `security_level`. The original `days_late` field is deliberately excluded from features because it is only known after delivery and would leak the target. Rows without a target are excluded. Numeric missing values use median imputation, categorical missing values use most-frequent imputation. Lab 7 fits preprocessors on training data only.

Lab 7 Activity G uses three **illustrative new shipments** adapted to the uploaded CSV schema; they are not rows from the source data. All other records used for fitting/evaluation are from the uploaded file.
