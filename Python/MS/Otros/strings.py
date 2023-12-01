heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

print("Moon" in "This text will describe facts and challenges with space travel")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())

temperatures = "Mars Average Temperature: -60 C"

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print("-60".startswith('-'))

if "30 C".endswith("C"):
print("This temperature is in Celsius")

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))