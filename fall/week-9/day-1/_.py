import csv
import matplotlib.pyplot as plt

countries = []
populations = []

with open('countries.csv', encoding='utf=8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        countries.append(row["name"])
        populations.append(int(row["population"]))

# Combine the data 
country_data = list(zip(countries, populations))
# Sort the data by the population
country_data.sort(key=lambda x: x[1], reverse=True)

# Get first 10 elements
top_10 = country_data[:10]

# Separate back into two lists
top_countries = [x[0] for x in top_10]
top_populations = [x[1] for x in top_10]

# Create horizontal bar graph
plt.barh(top_countries, top_populations)

# Add labels and title
plt.xlabel("Population")
plt.ylabel("Country")
plt.title("Top 10 Largest Countries")

# Make the layout fit nicer and display it
plt.tight_layout()
plt.show()
