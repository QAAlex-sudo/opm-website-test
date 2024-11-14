import pytest

from util.ApiClient import ApiClient


@pytest.fixture
def api_client():
    """Получаем экземпляр класса с заданным атрибутом URL"""
    return ApiClient()


@pytest.mark.parametrize("search_query", [
    "Lenovo s2"
])
def test_service_response(api_client, search_query):
    response = api_client.get_search_results(search_query)

    assert len(response.root) == 1
    assert response.root[0].data.id == "5599"
    assert response.root[0].data.type == "watch"
    assert (response.root[0]
            .data
            .relativePath == "constructor?type=3&manufacturer=34&serial=545&model=5599")
    assert response.root[0].data.text == "S2 Часы Lenovo S2"
    assert response.root[0].data.sorting == "0"
    assert response.root[0].score == 47.893784