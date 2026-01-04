# Risk Prediction

AI-powered predictions for Control Activity failure probability.

## Purpose

Risk Prediction uses machine learning to predict which controls are likely to fail their next test, allowing compliance teams to take preventive action.

## Key Fields

| Field | Description |
|-------|-------------|
| **Control Activity** | The control this prediction is for |
| **Control Name** | Human-readable name (e.g., "Journal Entry Approval Workflow") |
| **Prediction Date** | When this prediction was generated |
| **Failure Probability** | Chance the control will fail testing (0.0 - 1.0, where 0.15 = 15%) |
| **Risk Level** | Low/Medium/High/Critical based on probability thresholds |
| **Is Current** | Whether this is the most recent prediction for this control |

## Risk Level Thresholds

| Level | Probability Range |
|-------|------------------|
| Low | 0% - 20% |
| Medium | 20% - 40% |
| High | 40% - 60% |
| Critical | 60%+ |

## Contributing Factors

The model considers these factors when making predictions:

- **Days since last test** - Controls not tested recently have higher risk
- **Historical pass rate** - Controls that failed before are more likely to fail again
- **Deficiency count** - Controls with past deficiencies are higher risk
- **Is key control** - Key controls may have different risk profiles
- **Automation level** - Manual controls typically have higher failure rates
- **Has backup performer** - Controls without backup are riskier

## Recommended Actions

Based on the prediction, the system suggests actions like:

- Schedule testing within X days
- Review control design for effectiveness
- Assign backup performer
- Increase monitoring frequency
- Update control documentation

## How Predictions Are Generated

1. The AI model runs on a schedule (configurable in AI Provider Settings)
2. For each active Control Activity, it calculates failure probability
3. New Risk Prediction records are created with `is_current = 1`
4. Previous predictions for the same control have `is_current = 0`

## Viewing Predictions

- **Risk Prediction List**: See all predictions sorted by date
- **Control Activity Form**: See current prediction in the AI section (if enabled)
- **Dashboard**: High-risk controls highlighted for attention

## Configuration

Configure prediction behavior in **AI Provider Settings**:

- `enable_risk_prediction` - Enable/disable the feature
- `prediction_frequency` - How often to run predictions (Daily/Weekly)
- `high_risk_threshold` - Probability threshold for "High" classification
- `critical_risk_threshold` - Probability threshold for "Critical" classification
