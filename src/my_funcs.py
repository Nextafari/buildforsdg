

def currently_infected_cases(reported_cases, multiplier):
	currently_infected = reported_cases * multiplier
	return currently_infected

def infections_by_requested_time(currently_infected, days):
	infections_per_time = currently_infected * (2 ** int(days//3))
	return infections_per_time

def severe_infected_cases(reported_cases, multiplier_factor):
	severe_case = reported_cases * multiplier_factor
	return severe_case


def daily_impact(period_type, time_to_elapse):
	Days = "Days"
	Weeks = "Weeks"
	Months = "Months"
	days = 0 
	if period_type == Days:
		days = time_to_elapse
	elif period_type == Weeks:
		days = 7 * time_to_elapse
	elif period_type == Months:
		days = 30 * time_to_elapse
	else:
		return days


def severe_cases_by_requested_time(infections_by_requested_time, multiplier_1):
	severe_positive_cases = infections_by_requested_time * multiplier_1
	return severe_positive_cases


def hopsital_beds_by_requested_time(hospital_beds, multiplier_2, severe_cases_by_requested_time):
	available_bedspace = (hospital_beds * multiplier_2) - severe_cases_by_requested_time
	return available_bedspace


def cases_for_icu_by_requested_time(multiplier_3, infections_by_requested_time):
	cases_for_icu = infections_by_requested_time * multiplier_3
	return cases_for_icu


def cases_for_ventilators_by_requested_time(multiplier_4, infections_by_requested_time):
	cases_for_ventilators = infections_by_requested_time * multiplier_4
	return cases_for_ventilators


def dollars_in_flight(avg_daily_income, infections_by_requested_time, majority_population, days):
	daily_income_loss = (infections_by_requested_time * avg_daily_income * majority_population) // days
	return daily_income_loss