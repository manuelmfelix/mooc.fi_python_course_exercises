# Write your solution here
import math

def get_station_data(filename: str):

    stations = {}

    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]),float(parts[1]))

    return stations

def distance(stations: dict, station1: str, station2: str):
    x_km = (float(stations[station1][0]) - float(stations[station2][0])) * 55.26
    y_km = (float(stations[station1][1]) - float(stations[station2][1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    great = 0
    st1 = ""
    st2 = ""
    a = list(stations.keys())
    for b in range(len(a)-1):
        for d in range(1,len(a)):
            c = distance(stations,a[b],a[d])
            if c > great:
                great = c
                st1 = a[b]
                st2 = a[d]
    return st1, st2, great

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
