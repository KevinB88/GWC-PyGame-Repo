import time
import math

# Record the start time
start_time = time.time()

# Perform the input operation
user_input = input("Please enter something: ")

# Record the end time
end_time = time.time()

# Calculate the duration
duration = math.floor(end_time - start_time)

print(f"It took you {duration} seconds to respond.")
