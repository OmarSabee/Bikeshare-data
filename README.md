# Bikeshare Data Analysis

This Python script allows users to analyze bikeshare data for different cities in the US. Users can interactively specify a city, month, and day of the week to explore various statistics related to bikeshare usage.

## Requirements

- Python 3.x
- pandas library
- numpy library

## Usage

1. Ensure that Python 3.x is installed on your system.
2. Install the required libraries by running the following command:
```
pip install pandas numpy
```
3. Download the source code files.
4. Place the bikeshare data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as the script.
5. Open a terminal or command prompt and navigate to the directory containing the script and data files.
6. Run the script by executing the following command:
```
python bikeshare_analysis.py
```
7. Follow the prompts to specify the city, month, and day of the week for analysis.
8. The script will display various statistics related to the selected filters, such as the most common month, day of the week, start hour, popular stations, trip duration, user types, and, if available, gender and birth year information.
9. You can choose to see the raw data by answering "yes" when prompted.

## Notes

- The script assumes that the bikeshare data files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) are in CSV format and contain the necessary columns (`Start Time`, `End Time`, `Start Station`, `End Station`, `User Type`, `Gender`, `Birth Year`).
- If any data files are missing or the data format is incorrect, the script will not run properly.
- The script uses the pandas and numpy libraries to handle and analyze the data.
- User input is validated to ensure that valid city, month, and day selections are made.
- The script provides an interactive experience, allowing users to explore different aspects of the bikeshare data based on their selections.
