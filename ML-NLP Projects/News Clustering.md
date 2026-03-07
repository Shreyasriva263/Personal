# Clickbait vs News Clustering using NLP

## Overview
This project explores whether **unsupervised learning** can distinguish between clickbait headlines and legitimate news headlines.

Using **TF-IDF vectorization and K-Means clustering**, the model attempts to uncover underlying linguistic patterns that differentiate the two types of headlines without using labeled data during clustering.

The project also explores **multi-cluster interpretation, validation, and dimensionality reduction using PCA.**

---

## Dataset

The dataset contains **20,000 headlines**, split roughly evenly between:

- Clickbait headlines
- News headlines

Each headline was converted into numerical features using **TF-IDF vectorization**.

### Preprocessing Steps

- Removed stopwords
- Applied stemming
- Limited vocabulary to the **top 5,000 features**
- Transformed headlines into TF-IDF vectors.

---

## Binary Clustering (K = 2)

K-Means clustering was first applied with **k = 2** to determine whether the algorithm could separate clickbait from news headlines without labels.

### Observations

The clustering performed **better than random chance**, indicating that linguistic patterns exist between the two headline types.

Clickbait headlines often contain:

- emotionally charged words
- curiosity-driven phrasing
- sensational language

News headlines typically contain:

- more formal wording
- informational structure.

These differences allowed the clustering algorithm to identify underlying patterns in the text.

---

## Multi-Cluster Analysis (K = 6)

To explore finer subtopics within the dataset, the model was run again using **k = 6 clusters**.

Word clouds were generated to interpret the clusters.

### Cluster Themes

| Cluster | Theme |
|------|------|
| 0 | Lifestyle content |
| 1 | Finance and sports reporting |
| 2 | Politics |
| 3 | Relatable content |
| 4 | Personality-based headlines |
| 5 | Curiosity-based clickbait |

The clusters demonstrate how unsupervised learning can uncover **topic-based structure within textual datasets.**

---

## Cluster Validation

To evaluate clustering quality, the proportion of clickbait headlines in each cluster was calculated.

| Cluster | % Clickbait |
|------|------|
| 3 | 84.01% |
| 4 | 95.96% |
| 5 | 99.30% |
| 1 | 7.80% |
| 2 | 2.68% |
| 0 | 46.95% |

### Observations

- Clusters **3, 4, and 5** were strongly clickbait dominated.
- Clusters **1 and 2** were mostly news headlines.
- Cluster **0** was mixed.

This demonstrates that K-Means successfully captured **meaningful structure in the dataset.**

However, some misclassifications occurred because the algorithm relies on **word frequency patterns rather than deep semantic meaning.**

Example failure cases:

- Headlines with sensational wording but legitimate news content.

---

## New Headline Testing

Four new headlines were created to test the clustering system.

- 2 news-style headlines
- 2 clickbait-style headlines

Each headline was:

1. Vectorized using the same TF-IDF transformation
2. Compared to cluster centroids using **cosine distance**

### Results

- 3 headlines were classified as expected
- 1 headline was misclassified

The misclassified headline had a **large cosine distance**, suggesting it did not strongly match any cluster.

---

## PCA Visualization

To visualize the high-dimensional TF-IDF space, **Principal Component Analysis (PCA)** was applied.

The data was projected into **3 dimensions** and visualized using a **Plotly 3D scatter plot**.

### Explained Variance

| Component | Variance |
|------|------|
| PC1 | 0.00424598 |
| PC2 | 0.00390374 |
| PC3 | 0.00303258 |

These three components capture **very little of the total variance**, which is expected for text datasets with thousands of features.

Using **Truncated SVD**, it was found that:

- **870 components were required to capture ~50% of the variance**

This demonstrates how **text data spreads information across many dimensions.**

---

## Outlier Analysis

Two geometric outliers were identified in the PCA visualization.

These headlines contained **rare or unusual vocabulary**, which caused them to appear far from the main clusters.

Because PCA maximizes variance, rare word usage can push certain points further away from the center of the dataset.

---

## Technologies Used

- Python
- Scikit-Learn
- TF-IDF Vectorization
- K-Means Clustering
- PCA
- Plotly
- Pandas
- Google Colab

---

## Key Takeaways

- Unsupervised learning can identify meaningful structure in text data.
- Clickbait headlines contain distinctive linguistic patterns.
- K-Means clustering can reveal both category separation and topical clusters.
- Dimensionality reduction helps visualization but loses significant information in high-dimensional text data.