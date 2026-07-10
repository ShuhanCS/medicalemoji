"""Does resubmitting a declined emoji work, and which date starts the four-year bar?

Reads Unicode's public proposal-status sheet and answers three questions:

  1. Were our resubmissions filed while barred?
  2. Do first-time proposals fare better than resubmissions?
  3. Can the public data distinguish a bar counted from the SUBMISSION date from one
     counted from the DECLINE date?

Answer to 3 is no. See docs/plans, and do not overstate it.

    python evidence/resubmission_analysis.py sources/unicode_emoji_proposals_status_20260513.csv

Caveats baked into the code:
  * The sheet's date column is the SUBMISSION date, not the decline date.
  * Every 2025 row is stamped 2025-04-02, a batch placeholder. Those rows are dropped
    from gap analysis because the date is not real.
  * Names like "Blood Bag (B)" are distinct proposals by different authors. Only exact
    name matches are treated as resubmissions.
"""
import collections
import csv
import datetime
import sys

PLACEHOLDER = datetime.date(2025, 4, 2)
RULE_CHANGED = 2024  # the bar went from two years to four
OURS = {"liver", "stomach", "spine", "intestines", "ecg", "kidney", "kidneys"}


def load(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for r in csv.reader(f):
            if len(r) < 3 or r[0].strip().lower() == "emoji":
                continue
            try:
                d = datetime.datetime.strptime(r[2].strip(), "%m/%d/%Y").date()
            except ValueError:
                continue
            rows.append((r[0].strip().strip('"').lower(), r[1].strip().lower(), d))
    return rows


def advanced(status):
    return any(k in status for k in ("released", "recommend", "consideration"))


def bar_years(resubmission_date):
    return 4.0 if resubmission_date.year >= RULE_CHANGED else 2.0


def decline_date(submission):
    """Declines are announced at cycle end: submitters notified 'no later than November 30'."""
    return datetime.date(submission.year, 11, 30)


def main(path):
    rows = load(path)
    by_name = collections.defaultdict(list)
    for name, status, date in rows:
        by_name[name].append((date, status))

    # 1 and 2: first-time versus resubmission
    first_adv = first_n = re_adv = re_n = 0
    for versions in by_name.values():
        versions.sort()
        first_n += 1
        first_adv += advanced(versions[0][1])
        for _, status in versions[1:]:
            re_n += 1
            re_adv += advanced(status)
    print(f"first-time proposals  advanced {first_adv:>4}/{first_n:<5} {100*first_adv/first_n:.0f}%")
    print(f"resubmissions         advanced {re_adv:>4}/{re_n:<5} {100*re_adv/re_n:.0f}%\n")

    # 3: do the two clocks disagree, and does the outcome tell us which one governs?
    buckets = collections.defaultdict(lambda: [0, 0])
    for name, versions in by_name.items():
        versions = sorted(v for v in versions if v[0] != PLACEHOLDER)
        for (d1, s1), (d2, s2) in zip(versions, versions[1:]):
            if "declin" not in s1:
                continue
            bar = bar_years(d2)
            sub_ok = (d2 - d1).days / 365.25 >= bar
            dec_ok = (d2 - decline_date(d1)).days / 365.25 >= bar
            key = f"{'sub_ok' if sub_ok else 'sub_barred'} / {'dec_ok' if dec_ok else 'dec_barred'}"
            buckets[key][0] += advanced(s2)
            buckets[key][1] += 1
            if name in OURS:
                verdict = "inside the bar" if not sub_ok else "eligible"
                print(f"  ours: {name:11} {d1} -> {d2}  bar {bar:.0f}y  {verdict:15} {s2}")

    print()
    for key in ("sub_ok / dec_ok", "sub_ok / dec_barred", "sub_barred / dec_barred"):
        adv, total = buckets[key]
        rate = 100 * adv / total if total else 0
        print(f"  {key:26} advanced {adv}/{total} = {rate:.0f}%")
    print(
        "\nThe middle bucket is where the clocks disagree. Its rate sits between the other\n"
        "two on a handful of cases, so the public data does not identify which clock governs."
    )


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sources/unicode_emoji_proposals_status_20260513.csv")
