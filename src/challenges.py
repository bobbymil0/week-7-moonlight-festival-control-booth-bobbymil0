import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    heap = []
    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []
    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    heap = []
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result = []
    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    if k <= 0:
        return []

    heap = []
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result = []
    for _ in range(min(k, len(heap))):
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    if not alerts:
        return None

    heap = []
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    return heap[0][2]