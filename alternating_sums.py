from typing import List
ListOfInts = List[int]


class AlternatingSums:
    @classmethod
    def alternating_sums(cls, data: ListOfInts):
        team1, team2 = cls._divide_into_teams(data)
        return [sum(team1), sum(team2)]

    @classmethod
    def _divide_into_teams(cls, data: ListOfInts):
        odd, even = list(), list()
        for i, num in enumerate(data):
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even, odd
