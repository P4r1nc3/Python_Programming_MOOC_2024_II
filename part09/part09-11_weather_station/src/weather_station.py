# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name : str):
        self.__name = name
        self.__my_list = []

    def add_observation(self, observation: str):
        self.__my_list.append(observation)

    def number_of_observations(self):
        return len(self.__my_list)

    def latest_observation(self):
        if self.number_of_observations() == 0:
            return ''
        else:
            return self.__my_list[-1]

    def __str__(self):
        return f'{self.__name}, {len(self.__my_list)} observations'


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
