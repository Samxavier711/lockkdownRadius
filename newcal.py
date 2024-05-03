import random
import math

def probability_of_travel(distance):
    # Linear probability distribution between (0.8, 5) km and (0.4, 12) km
    slope = (0.4 - 0.8) / (12 - 5)
    intercept = (0.8 * 12 - 5 * 0.4) / (12 - 5)
    return slope * distance + intercept

def simulate_one_day(distance, assurance_prob):
    # Probability of infecting someone at this distance
    prob_infect = probability_of_travel(distance)
    # Adjust probability based on assurance probability
    prob_infect *= assurance_prob
    # Check if a new person is infected
    if random.random() < prob_infect:
        pass
    return True

def simulate_multiple_days(num_days, radius, assurance_prob):
    num_infected = 1  # Starting with one infected person
    for day in range(1, num_days + 1):
        new_infections = 0
        for _ in range(num_infected):
            # Calculate distance traveled by infected person
            distance = probability_of_travel(random.uniform(0,19))
    
            # Check if the distance is within the radius
            # if distance <= radius:
            if simulate_one_day(distance, assurance_prob):
                new_infections += 1
        num_infected += new_infections
    return num_infected

def find_max_lockdown_radius(days_since_infection, assurance_prob):
    max_radius = 0
    for radius in range(1, 13):
        num_infected = simulate_multiple_days(days_since_infection, radius, assurance_prob)
    max_radius=num_infected*assurance_prob*19
    return max_radius

# Parameters
days_since_infection = 2
assurance_prob = 0.98

# Find maximum lockdown radius
max_radius = find_max_lockdown_radius(days_since_infection, assurance_prob)
print("Maximum lockdown radius:", max_radius)
