import csv

print("=== DATA ANALYZER LITE v1.0 ===")

try:
    with open('billionaire_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    print(f"Loaded {len(data)} rows")
    print("\nFirst 3 rows:")
    for row in data[:3]:
        print(row)
    
    # Sort by net_worth
    sorted_data = sorted(data, key=lambda x: float(x.get('net_worth', 0)), reverse=True)
    print("\nTop 5 Richest:")
    for i, person in enumerate(sorted_data[:5]):
        print(f"{i+1}. {person.get('name')} - ${int(person.get('net_worth_billion'))}B")
        
except FileNotFoundError:
    print("Put billionaire_data.csv in this folder first")
