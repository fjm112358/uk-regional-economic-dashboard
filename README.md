# UK's Regional Economic Distribution Dashboard

An interactive dashboard developed in Python used to analyse data across regions in the UK.

## About the Project

This project analyses regional economic data and provides an interactive features

The dashboard allows users to select a region and dataset and view the corresponding distribution using histograms.

## Data

The dataset contains regional data on: 

* GDP
* Population
* GDP per head
* Accumulated GDP
* GDP growth

with the data being sourced from the **Office for National Statistics (ONS)**.

## Technologies Used

* **Python**
* **Pandas** – data cleaning
* **Plotly** – interactive data 
* **Dash** – interactive dashboard development
* **Excel** – data storage

## Features

* Interactive UK region selection
* Multiple economic datasets
* Interactive histograms
* Dynamic graph updates based on selection
* Data reshaping and processing using Pandas

## Project Structure

```text
uk-regional-economic-dashboard/
│
├── app.py
├── regional_gdp_cleaned.xlsx
└── README.md
```

## How to Run

Clone or download the repository and install the required Python libraries:

```bash
pip install dash pandas plotly openpyxl
```

Then run:

```bash
python app.py
```

The dashboard will open locally in your browser.

## Purpose

This project was developed as an independent Python project to develop practical skills in data analysis, statistical visualisation and interactive dashboard development.
