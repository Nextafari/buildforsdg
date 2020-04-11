from my_funcs import *


#multiplier for the currently infected people
multiplier = 10

#multiplier effect for severe impact
multiplier_factor = 50

#multiplier for severe positive cases 
multiplier_1 = 0.15

#multiplier for hospital beds availability
multiplier_2 = 0.35

#multiplier for ICU
multiplier_3 = 0.05

#multiplier for ventilator
multiplier_4 = 0.02


def estimator(**data):

	data= {}
	impact = {}
	severeImpact = {}

	avg_daily_income = data["region"]["avgDailyIncomeInUSD"]
	majority_population  = data["region"]["avgDailyIncomePopulation"]

	days = daily_impact(data["periodType"], data["timeToElapse"])
	
	#Output == currentlyInfected to be asigned to a dict = func(retrieving data from a dict containing the reported cases data)
	impact["currentlyInfected"] = currently_infected_cases(data["reportedCases"], multiplier)

	impact["infectionsByRequestedTime"] = infections_by_requested_time(data["currentlyInfected"], days)

	severeImpact["currentlyInfected"] = severe_infected_cases(data["currentlyInfected"], multiplier_factor)

	severeImpact["infectionsByRequestedTime"] = infections_by_requested_time(data["currentlyInfected"], days)

	impact["severeCasesByRequestedTime"] = severe_cases_by_requested_time(impact["infectionsByRequestedTime"], 																										multiplier_1)

	severeImpact["severeCasesByRequestedTime"] = severe_cases_by_requested_time(																							severeImpact["infectionsByRequestedTime"], multiplier_1)

	impact["hospitalBedsByRequestedTime"] = hopsital_beds_by_requested_time(data["hospitalBedsByRequestedTime"], 																multiplier_2, impact["severeCasesByRequestedTime"])

	severeImpact["hospitalBedsByRequestedTime"] = hopsital_beds_by_requested_time(data["hospitalBedsByRequestedTime"], 														multiplier_2, severeImpact["severeCasesByRequestedTime"])

	impact["casesForICUByRequestedTime"] = cases_for_icu_by_requested_time(impact["infectionsByRequestedTime"], 																									multiplier_3)
	
	severeImpact["casesForICUByRequestedTime"] = cases_for_icu_by_requested_time(severeImpact["infectionsByRequestedTime"]																								, multiplier_3)
	
	impact["casesForVentilatorsByRequestedTime"] = cases_for_ventilators_by_requested_time(																							impact["infectionsByRequestedTime"], multiplier_4)
	
	severeImpact["casesForVentilatorsByRequestedTime"] = cases_for_ventilators_by_requested_time(																			severeImpact["infectionsByRequestedTime"], multiplier_4)

	impact["dollarsInFlight"] = dollars_in_flight(avg_daily_income, impact["infectionsByRequestedTime"], 																									majority_population, days)

	severeImpact["dollarsImpact"] = dollars_in_flight(avg_daily_income, severeImpact["infectionsByRequestedTime"], 																							majority_population, days)





	response =  { 
		data: data,          
		impact: impact,         
		severeImpact: severeImpact   
		}


	return response
