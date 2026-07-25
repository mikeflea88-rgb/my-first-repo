import pandas as pd
import matplotlib.pyplot as plt

print("=== DATA ANALYZER v1.0 ===")

try:
    df = pd.read_csv('billionaire_data.csv')
    print("Data loaded!")
    print(df.head())
    
    print("\nTop 5 Richest:")
    print(df[['name', 'net_worth']].sort_values('net_worth', ascending=False).head())
    
    # Make a graph
    df['net_worth'].hist()
    plt.title('Net Worth Distribution')
    plt.savefig('graph.png')
    print("\nGraph saved as graph.png")
    
except FileNotFoundError:
    print("Put billionaire_data.csv in this folder first")
