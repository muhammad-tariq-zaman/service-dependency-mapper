"""Order services by dependency (topological sort) and detect cycles.

Usage: python3 main.py services.json
JSON format: {"services": {"web": ["db"], "db": []}}
"""
import argparse
import json
import sys


def order(services):
    visited, visiting, result = set(), set(), []

    def visit(node):
        if node in visited:
            return
        if node in visiting:
            raise ValueError(f"dependency cycle involving {node}")
        visiting.add(node)
        for dep in services.get(node, []):
            visit(dep)
        visiting.remove(node)
        visited.add(node)
        result.append(node)

    for node in services:
        visit(node)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="JSON service-dependency file")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        services = json.load(f)["services"]
    try:
        ordered = order(services)
    except ValueError as e:
        print(f"ERROR: {e}")
        return 1
    print("Start order (dependencies first):")
    for i, name in enumerate(ordered, 1):
        print(f"{i}. {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
