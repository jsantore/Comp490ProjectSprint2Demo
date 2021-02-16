import demo


def test_get_data():
    data = demo.get_data()
    assert len(data) > 3000

