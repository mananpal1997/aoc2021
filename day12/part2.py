from collections import defaultdict
from typing import Dict, List, Tuple

from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        graph: Dict[str, List[str]] = defaultdict(list)
        for line in s.splitlines():
            src, dst = line.split("-")
            if src != "end" and dst != "start":
                graph[src].append(dst)
            if src != "start" and dst != "end":
                graph[dst].append(src)

        todo: List[Tuple[str, Dict[str, int], bool]] = [
            ("start", defaultdict(int), False)
        ]
        num_paths = 0
        while todo:
            node, visited, twice = todo.pop()
            for adj in graph[node]:
                if adj.islower() and visited[adj] < 2:
                    visited[adj] += 1
                    if not twice:
                        todo.append((adj, visited.copy(), visited[adj] == 2))
                    elif twice and visited[adj] == 1:
                        todo.append((adj, visited.copy(), twice))
                    visited[adj] -= 1
                elif not adj.islower():
                    todo.append((adj, visited.copy(), twice))
            else:
                num_paths += node == "end"
        return num_paths


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        ("start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end", 36),
        (
            (
                "dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\n"
                "LN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc"
            ),
            103,
        ),
        (
            (
                "fs-end\nhe-DX\nfs-he\nstart-DX\npj-DX\nend-zg\nzg-sl\n"
                "zg-pj\npj-he\nRW-he\nfs-DX\npj-RW\nzg-RW\nstart-pj\n"
                "he-WI\nzg-he\npj-fs\nstart-RW"
            ),
            3509,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
