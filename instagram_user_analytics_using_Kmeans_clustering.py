import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load Instagram user data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess the data by selecting relevant features and scaling them."""
    features = ['followers', 'following', 'posts', 'likes', 'comments']
    df = df[features].fillna(0)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled, scaler

def perform_clustering(data, n_clusters=3):
    """Apply K-Means clustering to categorize users."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return clusters, kmeans

def visualize_clusters(df, clusters):
    """Visualize clusters using a scatter plot (followers vs likes)."""
    plt.scatter(df['followers'], df['likes'], c=clusters, cmap='viridis', alpha=0.6)
    plt.xlabel('Followers')
    plt.ylabel('Likes')
    plt.title('Instagram User Clustering')
    plt.colorbar(label='Cluster')
    plt.show()

def main():
    file_path = 'instagram_data.csv'  # Replace with your actual file path
    df = load_data(file_path)
    data_scaled, scaler = preprocess_data(df)
    clusters, model = perform_clustering(data_scaled)
    df['cluster'] = clusters
    visualize_clusters(df, clusters)
    df.to_csv('instagram_user_clusters.csv', index=False)
    print("Clustering completed. Results saved to instagram_user_clusters.csv")

if __name__ == "__main__":
    main()
