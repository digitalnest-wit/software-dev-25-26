# Temperature Converter
# Run here:

# Formula: 32°F − 32) × 5/9 = 0°C

temp_fahrenheit = float(input('What\'s the temperature outside? (ºF) '))
temp_celsius = (temp_fahrenheit - 32) * (5 / 9)

print(f' => {temp_celsius}ºC')
