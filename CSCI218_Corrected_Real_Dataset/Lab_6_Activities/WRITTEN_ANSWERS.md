# Lab 6 — Written answers (using uploaded 1M-row dataset)

**Dataset:** `humanitarian_shipments_1M.csv.gz`. Scripts use a fixed 20,000-row sample (19,928 rows with known targets). These answers are based on that sample, not on the instructor's 600-row example.

## Activity A — Why inspect before modelling?
Inspection reveals the dataset's structure, units, unusual values, and missing entries. For example, `cold_chain_temp_c` is missing in most records, `handler_notes` is free text, and some weights are non-positive. Without inspection, the model might treat bad values as genuine shipments or accidentally learn from information that would not be available before dispatch. Checking category labels and target completeness also helps prevent misleading results.

## Activity B — Target and why
The output is `delivery_status`: `On_Time` is encoded as 1 and `Delayed` as 0. It is the outcome the team wants to predict before delivery, so the other available shipment attributes become input features (`X`). Rows without a known status are excluded from supervised training and evaluation.

## Activity C — Columns removed and reasons
- `shipment_id`: unique identifier; not a generalizable delivery predictor.
- `dispatch_date`: omitted from this introductory model rather than treating a raw date as a numeric feature; a more advanced model could derive calendar variables.
- `country_office_code`: high-cardinality identifier, not needed for this baseline.
- `handler_notes`: unstructured text requiring separate natural-language processing.
- `cold_chain_temp_c`: approximately 90% missing and only meaningful for some shipments.
- `weight_lbs`: redundant conversion of `weight_kg`.
- `days_late`: **target leakage**. It is only known after delivery and effectively discloses the label.

## Activity D — Why not assign arbitrary numbers to categories?
A category such as Air, Sea, or Road has no natural numerical ordering. Encoding them as 0, 1, and 2 could falsely suggest that Road is larger than Air or twice Sea. One-hot encoding creates a separate 0/1 indicator for each category, avoiding that artificial ranking. The solution demonstrates this for seven categorical columns.

## Activity E — Missing-value decisions
Numerical features are imputed with the median, which is less sensitive to unusually large values than the mean. Categorical features are imputed with their most frequent observed category. Non-positive shipment weights are flagged as invalid and then imputed. Very sparse `cold_chain_temp_c` is dropped. Rows without the target are removed because imputing a label would invent the correct answer. For Lab 7, imputation values are learned on training data only.

## Activity F — Outliers and feature selection
The weight boxplot highlights extreme values; **six** sampled records have non-positive weight and are treated as invalid. Large positive weights are retained pending operational review because large humanitarian consignments can be legitimate. With non-negative encoded features, `SelectKBest(chi2, k=8)` selected `weight_kg`, `volume_m3`, `num_pallets`, `declared_value_usd`, `distance_km`, `beneficiaries_targeted`, `customs_clearance_days`, and `transport_mode_Air`. Chi-square rankings are sensitive to numerical feature scales, so they should not be interpreted as causal effects.

## Activity G — Validation checklist
- [x] All 40 model-input columns are numerical.
- [x] Missing values are handled.
- [x] Source categorical columns were replaced by one-hot indicators.
- [x] Feature and target arrays both contain 19,928 rows.
- [x] Decisions and potential leakage are documented.

### Reflection (120–150 words)
One preprocessing decision with a major effect is removing `days_late` from the input features. This field describes the delivery outcome after the shipment has arrived. If it were used to predict whether a shipment would be late, the model could appear extremely accurate without learning anything useful for planning ahead. Another important decision is how to handle missing customs clearance values. Replacing them with the median keeps more records available for training, but it can hide operational differences between routes or regions. A human analyst should review both decisions because the data may reflect unusual circumstances, incomplete reporting, or changes in how shipments are managed. The analyst should also check extreme weights rather than automatically deleting them: some very large shipments are legitimate. Keeping these choices documented makes predictions easier to explain, audit, and improve.
