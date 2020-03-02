import json
import pytest

from busses.bus import Bus


class TestBus:
    bus = None

    def setup_method(self):
        self.bus = Bus()

    def teardown_method(self):
        pass

    def test_group_simple_positive(self):
        parent_payload = []
        child_payload = []

        for num in range(1, 5):
            _parent_payload = {"id": num, "A": "A", "B": "B"}
            parent_payload.append(_parent_payload)

            if num % 2 == 1:
                _child_payload = {"id": num, "C": "C", "D": "D"}
                child_payload.append(_child_payload)

        parent_payload = json.dumps(parent_payload)
        child_payload = json.dumps(child_payload)

        result = self.bus.group(
            parent=parent_payload, child=child_payload, keys=[("id", "child_data")]
        )

        assert (
            result
            == '[{"id": 1, "A": "A", "B": "B", "child_data": {"C": "C", "D": "D"}}, {"id": 2, "A": "A", "B": "B"}, '
            '{"id": 3, "A": "A", "B": "B", "child_data": {"C": "C", "D": "D"}}, {"id": 4, "A": "A", "B": "B"}]'
        )

    @pytest.mark.parametrize(
        "parent_payload, child_payload, expected_output",
        [
            ({}, None, None),
            (None, {}, None),
            ("", "", None),
            ("", None, None),
            (None, "", None),
        ],
    )
    def test_group_arg_error_handling(
        self, parent_payload, child_payload, expected_output
    ):
        result = self.bus.group(
            parent=parent_payload, child=child_payload, keys=[("id", "child_data")]
        )
        assert result == expected_output
