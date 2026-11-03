# Lab 7 — Written answers (using uploaded 1M-row dataset)

**Dataset and evaluation:** Reproducible 20,000-row sample; 19,928 known delivery labels; 75% training and 25% testing. Metrics below are from the actual executed scripts, not the previous 600-row dataset.

## Activity A — One Lab 6 step that matters
If we skipped categorical encoding, the Random Forest could not use string fields such as `transport_mode` or `priority_level` directly. The Lab 6 preparation converts them to numerical indicators and handles missing values. We also exclude `days_late` to avoid leaking the answer.

## Activity B — Why keep the test set hidden?
The test set estimates how well the model performs on shipments it has never seen. Training on those records would let the model memorize details and make its reported performance unreliable. Stratifying preserves the approximate proportion of on-time and delayed shipments. The majority-class baseline is **77.12%**.

## Activity C — Why use 100 trees rather than one?
Each tree learns from a different bootstrap sample and considers different feature subsets. Combining their votes reduces the influence of one tree's accidental patterns or mistakes. A forest is often more stable on unseen records than a single deep tree, although more trees require extra computation.

## Activity D — Evaluation and confusion matrix
- Training accuracy: **100.00%**.
- Test accuracy: **80.33%**.
- Majority-class baseline: **77.12%**.
- Confusion matrix (rows = actual; columns = predicted; order = Delayed, On_Time):

| | Predicted Delayed | Predicted On_Time |
|---|---:|---:|
| Actual Delayed | 341 | 799 |
| Actual On_Time | 181 | 3,661 |

**Explain accuracy to a manager:** On previously unseen shipment records, the model correctly identified the delivery outcome about 80 out of every 100 times. This is only modestly better than predicting that every shipment will arrive on time, so it should be used cautiously.

**Training versus test gap:** Perfect training accuracy but lower test accuracy suggests overfitting. The test score, not the training score, is the better estimate of performance on new shipments.

**More costly mistake:** Missing a genuinely delayed shipment (predicting on time when it will be delayed) can prevent the team from arranging support early. There are **799** such errors in this test set. False alarms also cost resources, so the team should evaluate both kinds of error based on actual operational costs.

## Activity E — Feature importance
The top feature is `customs_clearance_days` (importance approximately **0.1149**), followed by `distance_km` (**0.1016**) and `fuel_price_index` (**0.0995**). Customs clearance plausibly affects delivery timing because longer clearance can delay shipments. However, this feature is usable before dispatch only if it is an estimate known at prediction time; an observed final clearance duration would also cause leakage. The importances show which variables the trained forest used, **not** which variables cause delays. Changing a correlated variable does not guarantee the delivery outcome will change.

## Activity F — Number of trees
| Trees | Test accuracy |
|---:|---:|
| 1 | 69.65% |
| 5 | 75.87% |
| 10 | 76.01% |
| 50 | 80.05% |
| 100 | 80.33% |
| 200 | 80.31% |

Accuracy generally rises at first and then levels off. In this run, 200 trees do **not** improve test accuracy over 100, so 100 trees is a reasonable choice when considering computation time.

## Activity G — New shipments
The three new examples are illustrative records built to match the **uploaded dataset's columns**, not copied source rows. Their results are:

| Shipment | Prediction | Trees voting on time |
|---|---|---:|
| A | On_Time | 96% |
| B | On_Time | 56% |
| C | On_Time | 75% |

**Which shipment to flag?** Shipment B: its 56% on-time vote is the weakest of the three, so it has the greatest estimated risk of delay. Tree vote shares are not necessarily well-calibrated real-world probabilities. The team should review its longer distance and clearance time.

**Shipment C's missing customs value:** Lab 6's median-imputation decision supplies the training-set median clearance value before prediction. This allows the model to produce an answer rather than failing on the missing field, but the analyst should verify the missing value when possible.

## Activity H — Validation checklist
- [x] Model features are numerical and contain no missing values.
- [x] The model was fitted on training records only.
- [x] Test accuracy, baseline, and confusion matrix were computed.
- [x] Feature importances and tree-count comparison were plotted.
- [x] New examples were processed with the training-fitted imputers and encoder.

### Reflection (120–150 words)
I would not allow this model to decide which humanitarian shipments receive extra support without human oversight. Its test accuracy is **80.33%**, only a little higher than the **77.12%** majority-class baseline. More importantly, it incorrectly predicts that **799** delayed shipments will arrive on time, which could cause the team to miss opportunities to intervene. The model is useful for highlighting shipments that deserve attention, but staff should combine its predictions with route conditions, urgent needs, and local knowledge. One Lab 6 decision that should remain under review is replacing missing customs clearance values with the median. This makes the model run consistently, yet the typical clearance time may differ between regions or transport modes. Analysts should also confirm that any clearance-day estimate is available before dispatch. These checks help prevent misleading confidence and support fairer, more reliable decisions.
