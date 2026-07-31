from app.memory.storage import (
    read_json,
    write_json,
)


def test_storage_round_trip():

    write_json([])

    data = read_json()

    assert isinstance(
        data,
        list,
    )