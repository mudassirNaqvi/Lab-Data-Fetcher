
# 🧪 Marham Lab Data Fetcher

This Python script fetches test data from the [Marham](https://www.marham.pk) labs API and saves details of the top 10 labs with valid responses into a JSON file.

## 🔧 Features

- Fetches test data for a list of lab IDs using the Marham public API.
- Collects data from up to 10 labs that return valid JSON responses.
- Saves the final output to a `data_more` file in JSON format.

## 🚀 How to Use

1. **Clone or copy the script to your local machine**

2. **Install required libraries (if not already installed)**
   ```bash
   pip install requests
   ```

3. **Run the script**
   ```bash
   python script.py
   ```

4. **Output**
   - The script will save a file named `data_more` in the same directory.
   - This file contains a list of up to 10 labs with their respective data.

## 📄 Code Overview

### `get_lab_data(lab_id)`
Fetches data for a specific lab using its ID. Returns JSON if valid, otherwise prints an error.

### `get_top_labs(lab_ids)`
Loops through given lab IDs and collects up to 10 valid lab datasets.

### `lab_ids_to_try = range(1, 21)`
Defines a list of lab IDs to try from 1 to 20.

## 💾 Output File Format

The output `data_more` file contains JSON like:
```json
[
    {
        "lab_id": 3,
        "data": {
            "tests": [...]
        }
    },
    ...
]
```

## 🧠 Author

**Syed Muhammad Mudassir Naqvi**  
Bachelor of Science in Computer Science - University of Karachi
