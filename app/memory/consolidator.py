from collections import defaultdict

class MemoryConsolidator:

    def consolidate(self, knowledge: list[dict]) -> list[dict]:
        merged = defaultdict(
            lambda: {
                "root_cause": "",
                "resolution": "",
                "confidence": 0,
                "occurrences": 0,
            }
        )
        for item in knowledge:
            key = (
                item["root_cause"],
                item["resolution"],
            )
            merged[key]["root_cause"] = item["root_cause"]
            merged[key]["resolution"] = item["resolution"]
            merged[key]["occurrences"] += 1
        results = []
        for value in merged.values():
            value["confidence"] = min(
                1.0,
                value["occurrences"] / 10,
            )
            results.append(value)

        return results