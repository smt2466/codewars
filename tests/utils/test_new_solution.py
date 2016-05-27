# pylint: disable=missing-docstring, invalid-name

from unittest import mock, TestCase

import pytest

from utils.new_solution import get_kata_data


class GetKataDataTest(TestCase):

    def setUp(self):
        self.mock_get = mock.patch('utils.new_solution.requests.get').start()
        self.response = mock.Mock()
        self.response.status_code = 200
        self.mock_get.return_value = self.response
        self.addCleanup(mock.patch.stopall)

    def test_returns_json_from_request(self):
        assert get_kata_data('slug', 'access_key') == self.response.json()

    def test_called_with_correct_url_and_api_key(self):
        url = 'https://www.codewars.com/api/v1/code-challenges/%s'
        slug = 'kata_slug'
        api_key = 'api_key'
        get_kata_data(slug, api_key)
        self.mock_get.assert_called_once_with(
            url % slug, {'access_key': api_key})

    def test_raise_error_if_response_status_code_is_not_200(self):
        self.response.status_code = 404
        with pytest.raises(ValueError):
            get_kata_data('slug', 'access_key')
