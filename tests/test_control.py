from src.control import Job_list

jobs = Job_list()


def test_job_list():
    assert type(jobs) == Job_list


def test_add():
    jobs.clear()
    jobs.add("a")
    assert "a" in jobs.jobs


def test_remove_job():
    jobs.clear()
    jobs.add("a")
    jobs.remove("a")
    assert "a" not in jobs.jobs


def test_get_first_job():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    assert jobs.get_first_job() == "a"


def test_bulk_add():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    assert len(jobs) == 3


def test_bulk_remove():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    jobs.bulk_remove(["a", "b", "c"])
    assert len(jobs) == 0


def test_clear():
    jobs.clear()
    assert len(jobs) == 0


def test_len():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    assert jobs.__len__() == 3


def test_str():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    assert jobs.__str__() == "['a', 'b', 'c']"


def test_repr():
    jobs.clear()
    jobs.bulk_add(["a", "b", "c"])
    assert jobs.__repr__() == "['a', 'b', 'c']"
