# Life Expectancy Classification using KNN

## Overview
This project analyzes global health indicators to classify countries as having **high or low life expectancy** using a K-Nearest Neighbors (KNN) model. The goal was to explore relationships between health metrics and evaluate how well machine learning models can predict life expectancy categories.

The analysis combines **visual exploration, classification modeling, and model evaluation** to identify which health indicators are most influential.

---

## Dataset
The dataset contains country-level health statistics including:

- BMI
- Infant Deaths
- Alcohol Consumption
- Adult Mortality
- Life Expectancy label (high vs low)

These features represent health, lifestyle, and mortality indicators that may influence national life expectancy outcomes.

---

## Visual Analysis

Pairplot analysis revealed several important relationships between the variables.

### Key Findings

**Adult Mortality**
- Strongly separates high and low life expectancy countries
- Countries with **high life expectancy cluster at very low adult mortality rates**

**Infant Deaths**
- Also strongly correlated with life expectancy
- High life expectancy countries tend to have **very low infant mortality**

**BMI and Alcohol Consumption**
- Show weaker relationships
- High and low expectancy countries appear mixed across these features

**Infant Deaths vs Adult Mortality**
- Shows a **positive correlation**
- Countries with higher adult mortality also tend to have higher infant mortality
- Strong clustering exists at low mortality levels.

---

## Policy Implications

If advising a government based on this analysis, the priority areas would be:

- Improving **healthcare access**
- Reducing **infant mortality**
- Addressing **adult mortality causes**
- Improving **sanitation and public health systems**

However, this analysis has limitations:

- Data is **aggregated at the country level**
- It does not capture **urban vs rural differences**
- Reporting standards vary across countries.

---

## Model Development

Two KNN classifiers were trained:

- **KNN (k = 3)** — Small neighborhood
- **KNN (k = 10)** — Larger neighborhood

Baseline models were also used for comparison:

- Always predict high life expectancy
- Always predict low life expectancy

---

## Model Performance

### Training Results

| Model | k | Accuracy | Precision | Recall | F1 |
|------|---|---|---|---|---|
| KNN (Small) | 3 | 0.991 | 0.984 | 0.982 | 0.983 |
| KNN (Large) | 10 | 0.962 | 0.955 | 0.903 | 0.928 |
| Always True | - | 0.267 | 0.268 | 1.0 | 0.423 |
| Always False | - | 0.732 | 0 | 0 | 0 |

### Testing Results

| Model | k | Accuracy | Precision | Recall | F1 |
|------|---|---|---|---|---|
| KNN (Small) | 3 | 0.970 | 0.960 | 0.939 | 0.949 |
| KNN (Large) | 10 | 0.951 | 0.953 | 0.878 | 0.914 |
| Always True | - | 0.294 | 0.294 | 1 | 0.454 |
| Always False | - | 0.706 | 0 | 0 | 0 |

### Observations

- **KNN with k=3 performed best overall**
- Smaller k values capture **local patterns more effectively**
- Larger k models generalize more but may reduce recall.

The baseline models highlight that **accuracy alone can be misleading**, especially with imbalanced datasets.

---

## Deployment Example

A hypothetical country was tested with:

- BMI = 27
- Infant Deaths = 11
- Alcohol Consumption = 1.3
- Adult Mortality = 50

The model predicted **high life expectancy**.

This prediction aligns with the earlier visual analysis because both **infant deaths and adult mortality are relatively low**, which strongly correlates with higher life expectancy.

---

## Technologies Used

- Python
- Scikit-Learn
- Pandas
- Seaborn
- Matplotlib
- Google Colab

---

## Key Takeaways

- Adult mortality and infant mortality are strong indicators of life expectancy.
- KNN can effectively classify life expectancy categories using health metrics.
- Evaluation metrics beyond accuracy (precision, recall, F1) are essential for understanding model performance.