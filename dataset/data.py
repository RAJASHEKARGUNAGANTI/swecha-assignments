import json
import csv
# import urllib.request

# read the JSON data from the URL
# url = 'https://data.viz.newsclick.in/covid/covidSummary.json'
# response = urllib.request.urlopen(url)
response = {
    "firstDoseAdministered": 77.08,
    "indiaNewConfirmed": 444,
    "indiaNewDeaths": 1,
    "indiaNewRecovery": 252,
    "indiaNewTests": 44846,
    "indiaNewVaccinated": 372,
    "indiaTotalActive": 3809,
    "indiaTotalConfirmed": 44690936,
    "indiaTotalDeaths": 530782,
    "indiaTotalRecovery": 44156345,
    "indiaTotalTests": 919716776,
    "indiaTotalVaccinated": 1979288349,
    "secondDoseAdministered": 71.42,
    "timestamp": "2023-03-13",
    "worldNewConfirmed": 422847,
    "worldNewDeaths": 1396,
    "worldNewRecovery": 0,
    "worldTotalActive": 632367530,
    "worldTotalConfirmed": 638991129,
    "worldTotalDeaths": 6623604,
    "worldTotalRecovery": 0
}
data = json.loads(response.read())

# open a CSV file for writing
with open('covidSummary.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # write the header row
    writer.writerow(['State', 'Confirmed', 'Active', 'Recovered', 'Deceased'])

    # write the data rows
    for state_data in data['stateData']:
        writer.writerow([
            state_data['state'],
            state_data['confirmed'],
            state_data['active'],
            state_data['recovered'],
            state_data['deceased']
        ])
