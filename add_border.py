from typing import List
ListOfStrings = List[str]


class AddBorder:
    @classmethod
    def add_border(cls, picture: ListOfStrings):
        width = len(picture[0])
        picture.insert(0, ('*' * width))
        picture.append('*' * width)
        result = []
        for l in picture:
            result.append('*' + l + '*')
        return result
