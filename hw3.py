
from data import CountyDemographics

#Part 1:
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population["2014 Population"]
    return total

# Purpose: Calculate the combined 2014 population of supplied counties.
# Input: counties is a list of CountyDemographics objects.
# Output: Returns the total of each county's "2014 Population" value

#Part 2:
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    matching = []

    for county in counties:
        if county.state == state:
            matching.append(county)
            
    return matching

# Purpose: Return counties whose state matches the requested state abbreviation.
# Input: counties is a list of CountyDemographics objects; state is a two-letter state abbreviation.
# Output: Returns a list of CountyDemographics objects from counties with a matching state.

#Part 3: 
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0.0
    for county in counties:
        if key in county.education:
            percentage = county.education[key]
            population = county.population["2014 Population"]
            total += population * percentage / 100
    return total
# Purpose: Estimate the 2014 population with a specified education category.
# Input: counties is a list of CountyDemographics objects; key is an education dictionary key.
# Output: Returns the total estimated population for the specified education category.

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0.0
    for county in counties:
        if key in county.ethnicities:
            percentage = county.ethnicities[key]
            population = county.population["2014 Population"]
            total += population * percentage / 100
    return total
# Purpose: Estimate the 2014 population with a specified ethnicity category.
# Input: counties is a list of CountyDemographics objects; key is an ethnicities dictionary key.
# Output: Returns the total estimated population for the specified ethnicity category.

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        percentage = county.income["Persons Below Poverty Level"]
        population = county.population["2014 Population"]
        total += population * percentage / 100
    return total
# Purpose: Estimate the 2014 population below the poverty level.
# Input: counties is a list of CountyDemographics objects.
# Output: Returns the total estimated population below the poverty level.

#Part 4:
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0.0:
        return 0.0
    education_population = population_by_education(counties, key)
    return 100 * (education_population / total_population)
# Purpose: Calculate the overall percentage for a specified education category.
# Input: counties is a list of CountyDemographics objects; key is an education dictionary key.
# Output: Returns the population-weighted percentage for the specified education category.

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0.0:
        return 0.0
    ethnicity_population = population_by_ethnicity(counties, key)
    return 100 * (ethnicity_population / total_population)
# Purpose: Calculate the overall percentage for a specified ethnicity category.
# Input: counties is a list of CountyDemographics objects; key is an ethnicities dictionary key.
# Output: Returns the population-weighted percentage for the specified ethnicity category.

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0.0:
        return 0.0
    below_poverty_population = population_below_poverty_level(counties)
    return 100 * (below_poverty_population / total_population)
# Purpose: Calculate the overall percentage of people below the poverty level.
# Input: counties is a list of CountyDemographics objects.
# Output: Returns the population-weighted percentage below the poverty level.

#Part 5:
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.education[key] > threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose education percentage is greater than a threshold.
# Input: counties is a list of CountyDemographics objects; key is an education key; threshold is a percentage.
# Output: Returns counties whose specified education percentage is strictly greater than threshold.

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.education[key] < threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose education percentage is less than a threshold.
# Input: counties is a list of CountyDemographics objects; key is an education key; threshold is a percentage.
# Output: Returns counties whose specified education percentage is strictly less than threshold.

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose ethnicity percentage is greater than a threshold.
# Input: counties is a list of CountyDemographics objects; key is an ethnicities key; threshold is a percentage.
# Output: Returns counties whose specified ethnicity percentage is strictly greater than threshold.

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.ethnicities[key] < threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose ethnicity percentage is less than a threshold.
# Input: counties is a list of CountyDemographics objects; key is an ethnicities key; threshold is a percentage.
# Output: Returns counties whose specified ethnicity percentage is strictly less than threshold.

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose poverty-level percentage is greater than a threshold.
# Input: counties is a list of CountyDemographics objects; threshold is a percentage.
# Output: Returns counties whose poverty-level percentage is strictly greater than threshold.

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matching = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            matching.append(county)
    return matching
# Purpose: Find counties whose poverty-level percentage is less than a threshold.
# Input: counties is a list of CountyDemographics objects; threshold is a percentage.
# Output: Returns counties whose poverty-level percentage is strictly less than threshold.
