from abc import abstractmethod
from typing import Optional

from rdflib import Literal
from rdflib.namespace import XSD

from .custom_graph import CustomGraph


class AddData:
    @abstractmethod
    def add_stadium(
        g: CustomGraph, country_name: object, city_name: object, stadium_name: object
    ):
        try:
            g.add_cls_instance(country_name, "Countries")
            g.add_cls_instance(city_name, "Cities")
            g.add_obj_prop_instance(city_name, "isPlacedIn", country_name)
            g.add_cls_instance(stadium_name, "Stadiums")
            g.add_obj_prop_instance(stadium_name, "isPlacedIn", city_name)

            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_dates(instance_name: object, start_date: object, end_date: object):
        try:
            g.add_cls_instance(instance_name, "Dates")
            if start_date is not None:
                g.add_data_prop_instance(
                    instance_name + "_date",
                    "StartDate",
                    Literal(start_date, datatype=XSD.dateTime),
                )
            if end_date is not None:
                g.add_data_prop_instance(
                    instance_name + "_date",
                    "EndDate",
                    Literal(end_date, datatype=XSD.dateTime),
                )
            g.add_obj_prop_instance(instance_name, "onDate", instance_name + "_date")
            print("add dates success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_statistic(instance_name: object, statistic: Optional[object]):
        try:
            if statistic is not None:
                g.add_cls_instance(instance_name + "_statistic", "StatisticsCls")
                g.add_data_prop_instance(
                    instance_name + "_statistic", "StatisticsCls", Literal(statistic)
                )
                g.add_obj_prop_instance(
                    instance_name, "hasStatistic", instance_name + "_statistic"
                )
                print("add statistic success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_competition(
        g: CustomGraph,
        competition_type: object,
        competition_name: object,
        competition_start_date: Optional[object],
        compettiton_end_date: Optional[object],
        competition_statistic: Optional[object],
    ):
        """
        Competition type in ["local", "national"]
        competition_statistic: json?
        """

        assert competition_type in ["local", "national"]

        try:
            if competition_type == "local":
                g.add_cls_instance(competition_name, "LocalCompetitions")
            else:
                g.add_cls_instance(competition_name, "NationalCompetitions")
            AddData.add_dates(
                competition_name, competition_start_date, compettiton_end_date
            )
            AddData.add_statistic(competition_name, competition_statistic)
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_team(
        g: CustomGraph,
        team_type: object,
        team_name: object,
        team_found_date: Optional[object],
        team_close_date: Optional[object],
        team_statistic: Optional[object],
    ):
        """
        team_type in ["NationalTeams", "SockerClubs"]
        team_statistic: json?
        """

        assert team_type in ["NationalTeams", "SockerClubs"]

        try:
            if team_type == "NationalTeams":
                g.add_cls_instance(team_name, "NationalTeams")
            else:
                g.add_cls_instance(team_name, "SockerClubs")
            AddData.add_dates(team_name, team_found_date, team_close_date)
            AddData.add_statistic(team_name, team_statistic)
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_player_position(g: CustomGraph, position_name: Optional[object]):
        try:
            if position_name is not None:
                g.add_cls_instance(position_name, "Position")
                g.add_data_prop_instance(
                    position_name, "PositionName", Literal(position_name)
                )
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_player(
        g: CustomGraph,
        player_name: object,
        team_name: object,
        position_name: Optional[object],
        player_emploing_date: Optional[object],
        player_fire_date: Optional[object],
        player_statistic: Optional[object],
    ):
        try:
            g.add_cls_instance(player_name, "Players")
            g.add_obj_prop_instance(player_name, "onPosition", position_name)
            AddData.add_dates(player_name, player_emploing_date, player_fire_date)
            AddData.add_statistic(player_name, team_statistic)
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_coach(
        g: CustomGraph,
        coach_name: object,
        team_name: object,
        coach_emploing_date: Optional[object],
        coach_fire_date: Optional[object],
        coach_statistic: Optional[object],
    ):
        try:
            g.add_cls_instance(coach_name, "Coaches")
            AddData.add_dates(coach_name, coach_emploing_date, coach_fire_date)
            AddData.add_statistic(coach_name, team_statistic)
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_play(
        g: CustomGraph,
        play_name: object,
        competition_name: object,
        team1_name: object,
        team2_name: object,
        play_date: Optional[object],
        play_statistic: Optional[object],
    ):
        try:
            g.add_cls_instance(play_name, "Play")
            g.add_obj_prop_instance(play_name, "isPartOfCompetition", competition_name)
            g.add_obj_prop_instance(team1_name, "playAgainst", team2_name)
            AddData.add_dates(play_name, play_date, None)
            AddData.add_statistic(play_name, play_statistic)
            print("Success")
        except Exception as e:
            print(e)

    @abstractmethod
    def add_prizes(g: CustomGraph, prize_name: object):
        try:
            g.add_cls_instance(prize_name, "Prizes")
            print("Success")
        except Exception as e:
            print(e)
