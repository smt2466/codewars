# pylint: disable=missing-docstring, invalid-name

from unittest import mock

import pytest

from utils.new_solution import (
    Kata,
    format_description,
    get_kata_data,
    limit,
    process_kata_data,
)


# class TestMe:
#
#     @pytest.fixture
#     def abc(self, monkeypatch):
#         monkeypatch.setattr('utils.new_solution.requests.get', 'abc')
#
#
#     def test_function(self, abc):
#         assert function() == 'abc'


class TestGetKataData:

    @pytest.fixture
    def response(self, monkeypatch):
        answer = mock.Mock()
        answer.status_code = 200

        def get(*_):
            return answer

        monkeypatch.setattr('utils.new_solution.requests.get', get)
        return answer

    def test_returns_json_from_request(self, response):
        assert get_kata_data('slug', 'access_key') == response.json()

    def test_called_with_correct_url_and_api_key(self, response):
        url = 'https://www.codewars.com/api/v1/code-challenges/%s'
        slug = 'kata_slug'
        api_key = 'api_key'

        get_kata_data(slug, api_key)

        assert response

    def test_called_with_correct_url_and_api_key(self):
        url = 'https://www.codewars.com/api/v1/code-challenges/%s'
        slug = 'kata_slug'
        api_key = 'api_key'

        get_kata_data(slug, api_key)

        self.assertEqual(self.mock_get.call_count, 1)
        self.assertEqual(
            self.mock_get.call_args,
            mock.call(url % slug, {'access_key': api_key}))

    # def test_raise_error_if_response_status_code_is_not_200(self):
    #     self.response.status_code = 404
    #     with pytest.raises(ValueError):
    #         get_kata_data('slug', 'access_key')

#
# class ProcessKataDataTest:
#
#     def test_returns_correct_namedtuple(self):
#         data = {
#             'name': 'kata_name',
#             'url': 'kata_url',
#             'slug': 'kata_slug',
#             'rank': {'id': -6},
#             'description': 'kata_description'
#         }
#         expected = Kata(
#             'kata_name',
#             'kata_url',
#             'kata_slug',
#             '6',
#             'kata_description'
#         )
#         kata = process_kata_data(data)
#         self.assertEqual(kata, expected)
#
#
# class LimitTest:
#
#     def test_leave_short_line_as_is(self):
#         line = 'hello world'
#         self.assertEqual()
#
#
# class FormatDescriptionTest:
#
#     def test_all_lines_ok(self):
#         text = 'hello\nworld'
#         self.assertEqual(format_description(text), text)
#
#     def test_one_line_is_too_long(self):
#         text = 'a'*79 + 'world'
#         expected = 'a'*79 + '\nworld'
#         assert format_description(text) == expected
#
#     def test_multiple_long_lines(self):
#         text = 'a'*79 + ' hello\n' + 'b'*79 + ' world'
#         expected = 'a'*79 + '\nhello\n' + 'b'*79 + '\nworld'
#         self.assertEqual(format_description(text), expected)
#
#     def test_super_long_line(self):
#         text = 'a'*79 + ' ' + 'b'*79 + ' hello'
#         expected = 'a'*79 + '\n' + 'b'*79 + '\nhello'
#         self.assertEqual(text, expected)
