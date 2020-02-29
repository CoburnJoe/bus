import json

from typing import List


class Bus:
    def __init__(self):
        pass

    @staticmethod
    def nest(parent: str, child: str, keys: List[tuple]) -> str:
        _parent = json.loads(parent)
        _child = json.loads(child)

        for object in _parent:
            for pair in keys:
                child_key = pair[0]  # student uuid
                parent_key = pair[1]  # meals

                for child_ in _child:
                    if object[child_key] == child_[child_key]:
                        object[parent_key] = child_
                        # del object[parent_key][child_key]

        print(_parent)

        return "yes"
