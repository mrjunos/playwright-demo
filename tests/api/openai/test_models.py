from assertpy import assert_that


def test_get_models(api):
    response = api.get_models()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(type(response.json())).is_equal_to(list)