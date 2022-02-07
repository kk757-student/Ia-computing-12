from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    N = 9
    stations = build_station_list()
    s = rivers_by_station_number(stations, N)
    print(s)

if __name__ == "__main__":
    print("*** Task 1E: rivers by number of stations ***")
run()

