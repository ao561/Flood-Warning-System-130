from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    '''Build list of stations'''
    stations = build_station_list()

    stations_n = rivers_by_station_number(stations, 9)

    
    print(stations_n)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
