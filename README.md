# Simple-centroid-based-classification

This project implements a simple prototype-based classification algorithm using the Iris dataset. Instead of training a complex model, it classifies new points by comparing them to the average (centroid) of each class using Euclidean distance.

It also visualizes both the original dataset and newly classified points using a scatter plot.

# Concepts Used
Centroid-based classification
Euclidean distance
Data aggregation with pandas
Interactive user input
Data visualization with seaborn

# Project Structure
.
├── iris.csv
├── main.py
└── README.md

# Requirements
Install the required dependencies:
pip install pandas seaborn matplotlib

# Usage

Run the script: python main.py

You will be prompted to enter points:

Proporciona el número de puntos a evaluar:
Proporciona X0:
Proporciona Y0:

Each point represents:

X → Petal Width
Y → Petal Length

# How It Works
1. Load Dataset
The Iris dataset is loaded and unnecessary columns are removed.
2. Compute Class Centroids
For each species:Mean petal length, Mean petal width
These become the reference points.
3. Input New Points
The user enters custom points to classify.
4. Distance Calculation
Each point is compared to all centroids using Euclidean distance.
5. Classification
The point is assigned to the nearest centroid.
6. Visualization
A scatter plot is generated showing: Original dataset, Classified new points

# Visualization
🔵 Original Iris data
🔴 Newly classified points
Colors represent species

# Limitations
Very simple classification method
Sensitive to data distribution
Not suitable for complex datasets
No learning phase (non-ML model in strict sense)

# Possible Improvements
Replace centroid method with KNN
Normalize data before distance calculation
Add decision boundaries
Use interactive plotting (Plotly)
Build a GUI for input

# Author
Juan Carlos Garcia Jimenez
