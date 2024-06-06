from src.pre_built.counter import count_ocurrences


def test_counter():
    count_path = count_ocurrences("data/jobs.csv", 'Python')
    assert count_path == 1639

    count_path = count_ocurrences("data/jobs.csv", 'C#')
    assert count_path == 57

    count_path = count_ocurrences("data/jobs.csv", 'Javascript')
    assert count_path == 122
