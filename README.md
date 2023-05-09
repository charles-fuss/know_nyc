# know_nyc

main.py provides an in-depth analysis of various aspects of a neighborhood in New York City, including rat reports, air pollution, demographics, nearby subway stations, parks, and crime statistics. The user inputs their address and receives relevant data about their neighborhood. This script also works collaboratively with the Google Places API, which takes user geolocation and compares against the data retrived from the Socrata API. 

getschools.py finds schools near a given address in New York City. The program provides a list of schools in the user's zip code and borough. Users can filter the results to show only public schools if desired.


## Dependencies

- msilib
- plotly
- getschools_
- geopy
- requests
- pandas
- math
- json
- Socrata

## Functions

### toGeoJSON(inputFile, outputFile)

Converts a JSON file to a GeoJSON file for mapbox compatibility.

### rat_results(zip)

Compiles recent rat reports from the user's neighborhood. Takes the zip code as a string input.

### pollution_results(address, neighborhood)

Gathers air pollution data for the user's neighborhood, including hospitalizations, deaths, and pollutant emissions.

### demographics(zip)

Provides demographic information for the user's zip code.

### subways(address)

Finds nearby subway stations and returns their distances from the user's address.

### parks(address)

Finds nearby parks and returns their distances from the user's address.

### park_events(parks, user_data)

Finds events happening at nearby parks.

### crime(address)

Gathers crime statistics for the user's neighborhood.

## Usage

1. Import the necessary libraries.
2. Set up the Socrata client.
3. Call the desired functions with the appropriate input parameters.

Example:

```python
address = "123 Main St, New York, NY"
zip_code = "10001"
neighborhood = "Chelsea"

rat_results(zip_code)
pollution_results(address, neighborhood)
demographics(zip_code)
subways(address)
parks(address)
