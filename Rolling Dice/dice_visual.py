import pygal

from die import Die

die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in the list.
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of result."

hist.add("D5 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
