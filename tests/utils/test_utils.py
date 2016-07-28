# pylint: disable=missing-docstring, invalid-name

try:
    from unittest import mock
except ImportError:
    import mock

import pytest

from utils.utils import Kata, get_kata_data, process_kata_data


class TestGetKataData:

    def create_answer(self, status_code):
        answer = mock.Mock()
        answer.status_code = status_code
        return answer

    @pytest.fixture
    def mock_get(self, monkeypatch):
        def inner_mock_get(answer):
            mock_get = mock.Mock(return_value=answer)
            monkeypatch.setattr('utils.utils.requests.get', mock_get)
            return mock_get
        return inner_mock_get

    @pytest.fixture
    def answer_ok(self):
        return self.create_answer(200)

    @pytest.fixture
    def answer_fail(self):
        return self.create_answer(404)

    @pytest.fixture
    def get_ok(self, answer_ok, mock_get):
        return mock_get(answer_ok)

    @pytest.fixture
    def get_fail(self, answer_fail, mock_get):
        return mock_get(answer_fail)

    def test_returns_json_from_request(self, get_ok):
        assert get_kata_data('slug', 'access_key') == get_ok().json()

    def test_called_with_correct_url_and_api_key(self, get_ok):
        slug = 'kata_slug'
        url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
        api_key = 'api_key'

        get_kata_data(slug, api_key)

        assert get_ok.call_count == 1
        assert get_ok.call_args == mock.call(url, {'access_key': api_key})

    def test_raise_error_if_response_status_code_is_not_200(self, get_fail):
        with pytest.raises(ValueError):
            get_kata_data('slug', 'access_key')


class TestProcessKataData:

    def test_returns_correct_namedtuple(self):
        data = {
            'name': 'kata_name',
            'url': 'kata_url',
            'slug': 'kata_slug',
            'rank': {'id': -6},
            'description': 'kata_description'
        }
        expected = Kata(
            'kata_name',
            'kata_url',
            'kata_slug',
            '6',
            'kata_description'
        )
        assert process_kata_data(data) == expected
