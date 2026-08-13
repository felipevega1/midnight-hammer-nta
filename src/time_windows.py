from datetime import date

# Window definitions: (label, start_date, end_date)
TIME_WINDOWS = [
    ("buildup_mar",    date(2025, 3,  1),  date(2025, 3, 31)),
    ("buildup_apr",    date(2025, 4,  1),  date(2025, 4, 30)),
    ("buildup_may",    date(2025, 5,  1),  date(2025, 5, 31)),
    ("buildup_jun1",   date(2025, 6,  1),  date(2025, 6, 12)),
    ("climax_w1",      date(2025, 6, 13),  date(2025, 6, 18)),
    ("climax_w2",      date(2025, 6, 19),  date(2025, 6, 24)),
    # Jun 25–30 (post-ceasefire days) fold into the July window so no dates are dropped.
    ("aftermath_jun-jul", date(2025, 6, 25),  date(2025, 7, 31)),
    ("aftermath_aug",  date(2025, 8,  1),  date(2025, 8, 31)),
]

def assign_window(article_date: date) -> str | None:
    for label, start, end in TIME_WINDOWS:
        if start <= article_date <= end:
            return label
    return None  # outside corpus window — should not occur after cleaning


# Chronological index per window, for output file naming.
WINDOW_INDEX = {label: i + 1 for i, (label, _, _) in enumerate(TIME_WINDOWS)}

def window_file_label(window: str) -> str:
    """'climax_w1' -> '05_climax_w1' — zero-padded chronological prefix so
    per-window output files sort chronologically in Finder / file browsers."""
    return f"{WINDOW_INDEX.get(window, 0):02d}_{window}"
