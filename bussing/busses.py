import json

from typing import List


class Bus:
    @staticmethod
    def group(parent: str, child: str, keys: List[tuple]) -> [str, None]:
        try:
            _parent = json.loads(parent)
            _child = json.loads(child)
        except (TypeError, json.decoder.JSONDecodeError):
            return None

        parent_type: type = type(_parent)
        child_type: type = type(_child)

        if parent_type.__name__ == "list" and child_type.__name__ == "list":
            for parent_ in _parent:
                for pair in keys:
                    shared_key = pair[0]
                    new_name = pair[1]
                    for child_ in _child:
                        parent_match = parent_.get(shared_key)
                        child_match = child_.get(shared_key)
                        if parent_match == child_match:
                            new_child = child_
                            del new_child[shared_key]
                            parent_[new_name] = new_child

            return json.dumps(_parent)

        return None
