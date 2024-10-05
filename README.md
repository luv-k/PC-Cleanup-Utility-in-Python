# PC Cleanup Utility in Python

This Python project provides a utility to clean temporary files and browser cache from your PC. It can delete files in specified directories, clear temporary folders, and remove cache data for popular web browsers like Chrome, Firefox, Brave, and Edge.

## Features

- **Delete Temporary Files:** Cleans temporary files from system-defined temporary folders.
- **Clear Browser Cache:** Deletes cache data for Chrome, Firefox, Brave, and Edge browsers.
- **Terminate Browser Processes:** Automatically terminates browser processes before clearing cache to ensure data is not in use.

## Requirements

- Python 3.x
- `psutil` library

To install the required library, run:

```bash
pip install psutil
```

## How to Run

1. **Clone or Download the Repository:** Clone this repository or download the project files to your local machine.
2. **Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the directory where the code is located.
3. **Run the Script:**

   ```bash
   python cleanup_utility.py
   ```

## Customization

You can customize the cleanup paths by adding additional folders in the `custom_temp_folders` list within the `clear_temp_file()` function.

## Example Output

```
Starting PC cleaning---
Terminating Chrome process...
Chrome was running and has been terminated
cleared : C:\Users\YourUserName\AppData\Local\Temp
PC cleanup completed.
```
