# Instagram User Analytics with Machine Learning

This project analyzes Instagram user engagement using machine learning techniques. It applies K-Means clustering to categorize users based on metrics like followers, likes, and comments.

## Features

Loads Instagram user data from a CSV file

Preprocesses data (scaling and feature selection)

Performs K-Means clustering to categorize users

Visualizes clusters using a scatter plot

Saves clustered results to a CSV file

## Installation

Clone the repository:

git clone https://github.com/yourusername/instagram-analytics.git
cd instagram-analytics

Install dependencies:

pip install pandas numpy matplotlib scikit-learn

## Usage

Prepare your dataset: Ensure instagram_data.csv contains columns:

followers

following

posts

likes

comments

## Run the script:

python instagram_analytics.py

View the results in instagram_user_clusters.csv.

## Visualization

The script generates a scatter plot showing user clusters (followers vs. likes), providing insights into different engagement groups.
