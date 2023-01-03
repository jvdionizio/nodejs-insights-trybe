from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    translated_list = read_brazilian_file(path)
    for report in translated_list:
        assert "title" in report
        assert "salary" in report
        assert "type" in report
        assert "titulo" not in report
        assert "salario" not in report
        assert "tipo" not in report
