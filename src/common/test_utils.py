from common.utils import get_ordered_members, random_string


def test_get_ordered_members():
    class TestClass:
        field_test_3 = None
        field_test_1 = None
        field_test_2 = None

    members = get_ordered_members(TestClass)
    fields_name = []
    for name, member in members:
        if name.startswith('field_test_'):
            fields_name.append(name)

    assert fields_name == ['field_test_3', 'field_test_1', 'field_test_2']


def test_gen_random_string():
    assert len(random_string(10)) == 10
    assert len(random_string(16)) == 16
    assert random_string(32) != random_string(32)
