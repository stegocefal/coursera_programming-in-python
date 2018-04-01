import pytest
import os
from .context import source
from source.file_with_magic_methods import File
import tempfile


def setup_tempfile(text):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write(text)
        tempfile_path = temp.name
    return tempfile_path


@pytest.fixture()
def file_obj(request):
    filepath = setup_tempfile('')
    obj = File(filepath)

    def fin():
        os.remove(filepath)

    request.addfinalizer(fin)
    return obj


file_obj2 = file_obj


def test_init(file_obj):
    assert os.path.isfile(file_obj.path)


def test_write(file_obj):
    writeline = 'line\n'
    file_obj.write(writeline)
    with open(file_obj.path, 'r') as f:
        readline = f.read()
    assert readline == writeline


def test_sum(file_obj, file_obj2):
    obj = file_obj + file_obj2
    assert os.path.isfile(obj.path)
    assert isinstance(obj, File)
    assert os.path.dirname(obj.path) == tempfile.gettempdir()
    with open(file_obj.path, 'r') as f:
        content1 = f.read()
    with open(file_obj2.path, 'r') as f:
        content2 = f.read()
    with open(obj.path, 'r') as f:
        content3 = f.read()
    os.remove(obj.path)  # This does not look good. Cleanup should be made inside fixture.
    assert content3 == content1 + content2


def test_iter(file_obj):
    lines = ['line1\n', 'line2\n', 'line3\n']
    # for line in lines:
    #     file_obj.write(line)
    file_obj.write(''.join(lines))
    i = 0
    for line in file_obj:
        assert line == lines[i]
        i += 1


def test_print(file_obj):
    assert file_obj.__str__() == file_obj.path
