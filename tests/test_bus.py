import json

from busses.bus import Bus


class TestBus:
    bus = None

    def setup_method(self):
        self.bus = Bus()

    def teardown_method(self):
        pass

    def test_shuttle(self):
        # def nest(self, parent: str, child: str, keys: dict) -> str:
        parent_payload = json.dumps(
            [
                {
                    "student_uuid": "123",
                    "upn": "upn string",
                    "former_upn": "former upn string",
                    "gender_code": "gender code",
                    "forename": "string",
                    "middle_names": "string",
                    "surname": "string",
                    "former_surname": "string",
                    "preferred_forename": "string",
                    "preferred_surname": "string",
                    "admission_status": "string",
                    "enrolment_status": "string",
                    "g_and_t_indicator": True,
                    "mode_of_travel_code": "string",
                    "mode_of_travel": "string",
                    "house_code": "string",
                    "house": "string",
                    "eal": True,
                    "first_language": "string",
                },
                {
                    "student_uuid": "789",
                    "upn": "upn string",
                    "former_upn": "former upn string",
                    "gender_code": "gender code",
                    "forename": "string",
                    "middle_names": "string",
                    "surname": "string",
                    "former_surname": "string",
                    "preferred_forename": "string",
                    "preferred_surname": "string",
                    "admission_status": "string",
                    "enrolment_status": "string",
                    "g_and_t_indicator": True,
                    "mode_of_travel_code": "string",
                    "mode_of_travel": "string",
                    "house_code": "string",
                    "house": "string",
                    "eal": True,
                    "first_language": "string",
                },
            ]
        )
        child_payload = json.dumps(
            [
                {
                    "student_uuid": "123",
                    "meal_uuid": "string",
                    "meal_name": "string",
                    "provided_by_school": True,
                    "date_of_meal": "string",
                    "meal_price": "string",
                    "cost_to_student": "string",
                },
                {
                    "student_uuid": "456",
                    "meal_uuid": "string",
                    "meal_name": "string",
                    "provided_by_school": True,
                    "date_of_meal": "string",
                    "meal_price": "string",
                    "cost_to_student": "string",
                },
            ]
        )
        # [{}]
        expected_output = None
        result = self.bus.nest(
            parent=parent_payload, child=child_payload, keys=[("student_uuid", "meals")]
        )
        assert 1 == 1
