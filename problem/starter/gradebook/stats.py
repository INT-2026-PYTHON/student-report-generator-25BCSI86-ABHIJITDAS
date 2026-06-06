"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass
def average_per_student(records):
    students = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        students.setdefault(name, []).append(score)

    averages = {}

    for name, scores in students.items():
        averages[name] = round(sum(scores) / len(scores), 2)

    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass
def subjects_offered(records):
    subjects = set()

    for record in records:
        subjects.add(record["subject"])

    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass
def top_scorer(records):
    averages = average_per_student(records)

    name = max(averages, key=averages.get)

    return (name, averages[name])

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass
def passing_students(records, threshold=60.0):
    averages = average_per_student(records)

    passed = []

    for name, avg in averages.items():
        if avg >= threshold:
            passed.append(name)

    return sorted(passed)