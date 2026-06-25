# Analytics Directory

This directory contains Jupyter notebooks and documentation for analyzing historical weather data from German weather stations.

## Table of Contents
- [1. Notebooks](#1-notebooks)
- [2. Documentation](#2-documentation)

## 1. Notebooks

- `station_history.ipynb`: Queries the local Parquet data lake to find the earliest recorded data and the total history length for each weather station.
- `station_hot_days.ipynb`: Calculates the number of extremely hot days (maximum temperature exceeding 32 degrees Celsius) per year for all weather stations with at least 100 years of data. The results are visualized as bar charts to show the evolution of extreme heat frequency.
- `station_map.ipynb`: Identifies weather stations with at least 100 years of data and plots them on an interactive map using their latitude and longitude coordinates.
- `station_timeseries.ipynb`: Generates temperature timeseries charts for weather stations with a history of at least 100 years. The charts display the yearly average of minimum, maximum, and mean temperatures.
- `station_anomalies.ipynb`: Calculates the overall average maximum temperature for stations with at least 100 years of data, computes the average maximum temperature for each year, and visualizes the difference as a bar diagram. Positive anomalies indicate warmer years and negative anomalies indicate cooler years.
- `station_anomalies_50_70.ipynb`: Applies the same logic as `station_anomalies.ipynb`, but filters for stations with a history length between 50 and 70 years that are present until the end of the dataset.
- `kirschbluete_timeseries.ipynb`: Analyzes and plots the time series of the Julian day when the sour cherry bloom started, showing both the individual station data and average overall trends.
- `kirschbluete_weather_correlation.ipynb`: Selects random phenology stations and long-running weather stations to calculate and plot a correlation matrix between spring mean temperatures and the bloom day (Jultag).

## 2. Documentation

- `experiment_design_changes.md`: A report detailing data homogenization, parallel measurements, and structural biases introduced by changes in experimental design over time. This includes information on calculation methodologies, sensor hardware updates, and reporting systems for historical raw datasets compared to modern homogenized datasets. It also contains a tabular record of station metadata changes.
