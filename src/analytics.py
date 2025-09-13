def chunk(values: list[int], k: int) -> list[list[int]]:
    if k <= 0:
        raise ValueError("k must be > 0")
    result = []
    for i in range(0, len(values), k):
        result.append(values[i:i+k])
    return result


def running_total(start: int, changes: list[int]) -> list[int]:
    result = []
    total = start
    for c in changes:
        total += c
        result.append(total)
    return result


def index_of_first_at_least(values: list[int], target: int) -> int | None:
    for i, v in enumerate(values):
        if v >= target:
            return i
    return None
