"""Census of Unicode emoji groups/subgroups, and where health emoji actually live.

Generates the tables in docs/plans/2026-07-09-utc-doc-health-category-spec.md.
Recompute before filing; print the retrieval date in the UTC document.

    curl -s https://unicode.org/Public/emoji/latest/emoji-test.txt -o emoji-test.txt
    python emoji_group_census.py emoji-test.txt
"""
import collections
import re
import sys

HEALTH_TERMS = [
    "anatomical heart", "lungs", "brain", "tooth", "bone", "microbe", "dna", "petri dish",
    "test tube", "ambulance", "hospital", "medical symbol", "health worker",
    "face with thermometer", "head-bandage", "nauseated", "vomiting", "sneezing",
    "medical mask", "woozy", "pill", "syringe", "stethoscope", "x-ray", "crutch",
    "adhesive bandage", "drop of blood", "wheelchair symbol", "ear with hearing aid",
    "mechanical arm", "mechanical leg", "white cane", "manual wheelchair",
    "motorized wheelchair", "guide dog", "service dog", "deaf person", "pregnant person",
]


def parse(path):
    """Yield (group, subgroup, char, name) for every fully-qualified emoji."""
    group = subgroup = None
    for line in open(path, encoding="utf-8"):
        if line.startswith("# group:"):
            group = line.split(":", 1)[1].strip()
        elif line.startswith("# subgroup:"):
            subgroup = line.split(":", 1)[1].strip()
        elif group and not line.startswith("#") and "; fully-qualified" in line:
            m = re.match(r"^(\S+)\s+E[\d.]+\s+(.*)$", line.split("#", 1)[1].strip())
            if m:
                yield group, subgroup, m.group(1), m.group(2)


def main(path):
    rows = list(parse(path))
    groups = collections.Counter(g for g, _, _, _ in rows)
    print("=== groups ===")
    for g, n in groups.items():
        print(f"  {g:20} {n:5}")
    print(f"  {'TOTAL':20} {sum(groups.values()):5}\n")

    print("=== subgroups of Objects ===")
    objects = collections.Counter(s for g, s, _, _ in rows if g == "Objects")
    for s, n in objects.most_common():
        print(f"  {s:22} {n:4}")

    print("\n=== health-related emoji, by where they live ===")
    seen, located = set(), collections.defaultdict(list)
    for g, s, ch, name in rows:
        low = name.lower()
        for term in HEALTH_TERMS:
            if term in low and term not in seen:
                seen.add(term)
                located[f"{g} > {s}"].append(f"{ch} {name}")
                break
    for loc in sorted(located):
        print(f"  {loc}  [{len(located[loc])}]")
        for e in located[loc]:
            print(f"      {e}")
    missing = [t for t in HEALTH_TERMS if t not in seen]
    if missing:
        print(f"\n  NOT FOUND (check for renames): {missing}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "emoji-test.txt")
