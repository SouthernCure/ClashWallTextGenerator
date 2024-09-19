import dearpygui.dearpygui as dpg

GRID_SIZE = 10  # Define the grid size
checkbox_states = {}  # Dictionary to store the state of each checkbox

def on_checkbox_change(sender, app_data, user_data):
    """Callback function when a checkbox is clicked."""
    # Update the checkbox state in the dictionary
    checkbox_states[sender] = app_data

def save_checkbox_states():
    """Saves the states of all checkboxes into a string."""
    result = []
    hash_count = 0
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            checkbox_name = f"Checkbox_{i}_{j}"
            # Retrieve the state of each checkbox (default to 0 if not found)
            state = checkbox_states.get(checkbox_name, False)
            if state:
                row.append('#')
                hash_count += 1
            else:
                row.append('.')
        # Join each row into a single string and add to the result
        result.append(''.join(row))
    
    # Join all rows with a newline character to form the final string
    final_string = '\n'.join(result)
    print(final_string)  # Print the final string (or handle it as needed)
    print(f"Total number of filled checkboxes (#): {hash_count}")

def create_checkbox_grid():
    """Creates a grid of checkboxes."""
    with dpg.window(label="42x42 Checkbox Grid", width=1920, height=1080):
        # Create the grid of checkboxes
        for i in range(GRID_SIZE):
            with dpg.group(horizontal=True):  # Create a horizontal group for each row
                for j in range(GRID_SIZE):
                    # Unique name for each checkbox based on its position
                    checkbox_name = f"Checkbox_{i}_{j}"
                    dpg.add_checkbox(label="", callback=on_checkbox_change, user_data=(i, j), tag=checkbox_name)

        # Add the save button below the grid
        dpg.add_button(label="Save", callback=save_checkbox_states)

# Initialize DearPyGui and create the checkbox grid
dpg.create_context()
create_checkbox_grid()
dpg.create_viewport(title='Checkbox Grid', width=800, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
