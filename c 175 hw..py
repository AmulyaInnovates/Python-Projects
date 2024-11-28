import matplotlib.pyplot as plt
import psutil

# Create an empty dictionary to store the application names and their CPU usage
app_name_dict = {}

# Set the count variable to 0
count = 0

# Iterate through the processes
for process in psutil.process_iter():
    # Increment the count variable
    count += 1
    
    # Check if the count is less than or equal to 6
    if count <= 6:
        # Get the name of the application
        name = process.name()
        
        # Get the CPU usage of the application
        cpu_usage = process.cpu_percent()
        
        # Print the application name and CPU usage
        print(f"{name} - {cpu_usage}%")
        
        # Update the dictionary with the application name and CPU usage
        app_name_dict.update({name: cpu_usage})

# Get the application name with maximum CPU usage
keymax = max(app_name_dict, key=app_name_dict.get)
print(f"Application with maximum CPU usage: {keymax}")

# Get the application name with minimum CPU usage
keymin = min(app_name_dict, key=app_name_dict.get)
print(f"Application with minimum CPU usage: {keymin}")

# Create a list of application names with maximum and minimum CPU usage
name_list = [keymax, keymin]
print(name_list)

# Get the maximum and minimum CPU usage values from the dictionary
app = app_name_dict.values()
max_app = max(app)
min_app = min(app)

# Create a list of maximum and minimum CPU usage values
max_min_list = [max_app, min_app]
print(max_min_list)

# Plot the bar chart
plt.figure(figsize=(6, 6))
plt.xlabel("Application")
plt.ylabel("CPU Usage")
plt.bar(name_list, max_min_list, width=0.5, color=['green', 'blue'])
plt.show()
