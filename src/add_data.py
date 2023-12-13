from abc import abstractmethod

from .custom_graph import CustomGraph


class AddData:

    @abstractmethod
    def add_stadium(g: CustomGraph,
                    country_name: object,
                    city_name: object,
                    stadium_name: object):
        try:
            g.add_cls_instance(country_name, "Countries")
            g.add_cls_instance(city_name, "Cities")
            g.add_obj_prop_instance(city_name, "isPlacedIn", country_name)
            g.add_cls_instance(stadium_name, "Stadiums")
            g.add_obj_prop_instance(stadium_name, "isPlacedIn", city_name)

            print("Success")
        except(Exception) as e:
            print(e)

