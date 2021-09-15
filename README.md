# RAIZEN | Code Challenge

## Goal

Build a small REST API that answers questions about sensor data collected in a single month.

## Background

Below we share a dataset in CSV format that provides metrics recorded by a sensor over a full month (2015-08). 

These are the parameters we care for this challenge:

- `time`: The datetime when the metric was recorded
- `temp`: The temperature recorded by the sensor
- `CO2`: The CO2 concentration recorded by the sensor
- `humidity`: The humidity recorded by the sensor

Based on that, we want to answer some questions by querying an API instead of doing manual exploration of the data.

You are free to design the endpoints the way you feel they should be.

## Questions the API should be able to answer

- What was the highest CO2 level detected in the whole dataset and when did that happen?
- What was the day with the hottest temperature recorded in that month?
- What was the day and hour with the highest humidity recorded?

## Rules

- You must use Python 3.8+
- The API specification must be defined using OpenAPI v3 and implemented in Falcon https://falcon.readthedocs.io/en/stable/
- Make a good developer experience. We would like to be able to install and run this API in less than 5min total


## Bonus (optional)

- Use Docker Compose
- Use a Time Series Database for storing/querying the data (timescale, influxdb, etc)

## Notes

We are aware that some of the requirements are a bit open. That helps us understand the way you approach problems with incomplete requirements and how proactive (or careful) you are in these situations. 

You can send the public repository link to `eduardo@raizenlabs.com`

# Thank you for your time.