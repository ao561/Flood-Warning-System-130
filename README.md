# Flood Warning System

A Python-based computational backend for a real-time flood monitoring and warning system. This project processes real-time river level data to perform geographical analysis, assess flood risk, and generate alerts for rivers and stations across England.

## 🛠️ Features

* **Real-time Data Retrieval:** Fetches live river level data from the Department for Environment Food and Rural Affairs (DEFRA) API.

* **Geographical Analysis:** Analyzes the location of monitoring stations, including finding the closest stations to a given point and identifying stations within a certain radius.

* **Data Analysis & Manipulation:** Implements a variety of functions to process, analyze, and manipulate time-series river level data.

* **Flood Risk Assessment:** Determines the current flood risk at various stations by comparing current levels to typical high and low levels.

* **Data Visualization:** Generates plots and charts to visualize river level trends over time.

## 📁 Project Structure

This project is structured as a series of tasks, building upon each other to create a functional flood warning system backend. The tasks are designed to be completed sequentially and cover various aspects of the system's functionality.

* `Task1A.py` - `Task1F.py`: Focus on initial data structures and geographical calculations.

* `Task2A.py` - `Task2G.py`: Focus on data analysis, including flood risk assessment and time-series data processing.

## ✅ Tests

The project includes a suite of unit tests to ensure the reliability of the system's components. These tests cover core functionalities like data analysis, geographical calculations, and station data handling.

* `test_analysis.py`: Tests the functions for data analysis and flood risk assessment.

* `test_geo.py`: Tests the geographical calculation functions, such as finding the distance between stations.

* `test_station.py`: Tests the data structures and methods related to monitoring stations.

To run the tests, you will need to have `pytest` installed:
```
pip install pytest
```
Then, from the root directory of the repository, you can run the tests with:
```
pytest
```
## 🏁 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### 📋 Prerequisites

You will need Python 3.x installed on your system.

### ⬇️ Installation

1. Clone the repository:
```
git clone https://github.com/ao561/Flood-Warning-System.git
cd Flood-Warning-System
```
2. (Optional) It is recommended to create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```
3. Install the required dependencies:
```
pip install haversine numpy matplotlib
```
## ▶️ Usage

You can run the various Python scripts located in the root directory of the repository to test the functionality of each task. For example, to run one of the initial tasks, you would execute:
```
python Task1A.py
```
