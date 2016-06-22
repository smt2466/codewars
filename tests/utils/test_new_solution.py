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


class TestGetKataData:

    @pytest.fixture
    def answer_ok(self):
        answer = mock.Mock()
        answer.status_code = 200
        return answer

    @pytest.fixture
    def answer_fail(self):
        answer = mock.Mock()
        answer.status_code = 404
        return answer

    def test_returns_json_from_request(self, monkeypatch, answer_ok):
        mock_get = mock.Mock(return_value=answer_ok)
        monkeypatch.setattr('utils.new_solution.requests.get', mock_get)

        assert get_kata_data('slug', 'access_key') == answer_ok.json()

    def test_called_with_correct_url_and_api_key(self, monkeypatch, answer_ok):
        mock_get = mock.Mock(return_value=answer_ok)
        monkeypatch.setattr('utils.new_solution.requests.get', mock_get)

        slug = 'kata_slug'
        url = 'https://www.codewars.com/api/v1/code-challenges/%s' % slug
        api_key = 'api_key'

        get_kata_data(slug, api_key)

        assert mock_get.call_count == 1
        assert mock_get.call_args == mock.call(url, {'access_key': api_key})

    def test_raise_error_if_response_status_code_is_not_200(self, monkeypatch, answer_fail):
        mock_get = mock.Mock(return_value=answer_fail)
        monkeypatch.setattr('utils.new_solution.requests.get', mock_get)

        with pytest.raises(ValueError):
            get_kata_data('slug', 'access_key')


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
