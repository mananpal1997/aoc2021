from collections import defaultdict
from typing import Dict, List, Set, Tuple

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

        todo: List[Tuple[str, Set[str]]] = [("start", set())]
        num_paths = 0
        while todo:
            node, visited = todo.pop()
            for adj in graph[node]:
                if adj.islower() and adj not in visited:
                    visited.add(adj)
                    todo.append((adj, visited.copy()))
                    visited.remove(adj)
                elif not adj.islower():
                    todo.append((adj, visited.copy()))
            else:
                num_paths += node == "end"
        return num_paths


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        ("start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end", 10),
        (
            (
                "dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\n"
                "LN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc"
            ),
            19,
        ),
        (
            (
                "fs-end\nhe-DX\nfs-he\nstart-DX\npj-DX\nend-zg\nzg-sl\n"
                "zg-pj\npj-he\nRW-he\nfs-DX\npj-RW\nzg-RW\nstart-pj\n"
                "he-WI\nzg-he\npj-fs\nstart-RW"
            ),
            226,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
