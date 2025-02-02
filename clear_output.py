from IPython.display import clear_output, display
import time

# Function to simulate some work and update count
def loop_with_clear():
    for i in range(1, 101):  # Example loop (1 to 100)
        # Clear the output of the current cell
        clear_output(wait=True)
        
        # Print the count
        print(f"Loop iteration: {i}")
        
        # Simulate some work
        time.sleep(1)  # Sleep for 1 second (replace with actual work)

# Run the function
loop_with_clear()

