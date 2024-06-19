# Lesson 3: Assignments | Sets

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Task 1:
def shared_destination(): #Destinations that both airlines fly to
    mutual_dest = our_routes.intersection(competitor_routes)
    return mutual_dest
print(shared_destination())

def unique_desination(): #Destination unique to our airline
    exclusive_dest = our_routes.difference(competitor_routes)
    return exclusive_dest
print(unique_desination())

def neither_destination(): #Destinations that neither airline share
    other_destination = our_routes.symmetric_difference(competitor_routes)
    return other_destination
print(neither_destination())


# 2. Set Operations in Data Analysis
# Task 1:
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def existing_customer_ids():
    set_ids = set(customer_ids)
    unique_customer_ids = list(set_ids)
    return unique_customer_ids
print(existing_customer_ids())