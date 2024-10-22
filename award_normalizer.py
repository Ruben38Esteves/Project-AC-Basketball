import csv

# Step 1: Read the CSV file
input_file = 'data/awards_players.csv'
output_file = 'data/normalized_awards_players.csv'

with open(input_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Step 2: Define normalization rules
normalization_rules = {
    "All-Star Game Most Valuable Player": "All-Star MVP",
    "Coach of the Year": "Coach of the Year",
    "Defensive Player of the Year": "Defensive Player of the Year",
    "Kim Perrot Sportsmanship": "Kim Perrot Sportsmanship Award",
    "Kim Perrot Sportsmanship Award": "Kim Perrot Sportsmanship Award"
}

# Step 3: Normalize award names
for row in data:
    if row['award'] in normalization_rules:
        row['award'] = normalization_rules[row['award']]

# Step 4: Write the normalized data to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)