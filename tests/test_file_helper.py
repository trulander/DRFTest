import pytest

from unittest import mock

from file_helper import FileHelper, Api
import os

@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "filename"
    f.write_text("CONTENT")
    return f

@pytest.fixture
def api():
    api = Api("api_key_secret")
    yield api
    api.close()

@pytest.fixture
def file_helper(api):
    fh = FileHelper(api=api)
    return fh

class TestFileHelper:
    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

    def test_remove_file(self, file_helper, temp_file):
        api = object()
        fh = FileHelper(api=api)
        fh.remove_file(filepath=temp_file)
        assert os.path.exists(temp_file) is False

    @mock.patch.object(FileHelper, "prepare_file", autospec=True)
    def test_upload_file(self, mocked_prepare_file):
        fake_api = mock.MagicMock()
        expected_data = object()
        mocked_prepare_file.return_value = expected_data
        fh = FileHelper(fake_api)
        fh.upload_file("Fake filepath")
        fake_api.request.assert_called()
        fake_api.request.assert_called_once()
        fake_api.request.assert_called_once_with("POST", expected_data)

    @mock.patch("file_helper.os")
    def test_uses_unlink_for_remove(self, mocked_fh_osm, file_helper):
        filepath = "11111"
        mocked_fh_osm.path.isfile.return_value = True
        file_helper.remove_file(filepath=filepath)
        mocked_fh_osm.unlink_assert_called_once_with(filepath)
