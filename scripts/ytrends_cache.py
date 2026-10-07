#!/usr/bin/env python3
"""Cache số liệu YTrends theo từ khóa để không tra lại trong cùng một kỳ dữ liệu.

YTrends làm mới dữ liệu mỗi ngày một lần (~14:00-15:00 UTC). Một mục cache chỉ
được dùng khi nó được lưu SAU lần làm mới gần nhất (mốc 15:00 UTC), nên số liệu
lấy từ cache giống hệt số liệu tra lại ngay lúc này.

Cách dùng:
  python3 ytrends_cache.py get --ltype physical "gingham applique" "varsity applique"
      -> {"hits": {keyword: entry}, "misses": [keyword, ...]}
  python3 ytrends_cache.py put < entries.json
      entries.json là list các object, mỗi object có các khóa trong REQUIRED
      (giá trị có thể là null), tùy chọn thêm "related": [tag, ...].
  python3 ytrends_cache.py clear

Thêm --as-of YYYY-MM-DD vào lệnh get để coi các mục có snapshot.as_of_date khác
là miss (dùng khi một lần tra mới trả về as_of_date khác với cache).
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

CACHE_FILE = Path(os.environ.get("ETSY_TITLE_TAG_CACHE",
                                 Path.home() / ".cache" / "etsy-title-tag" / "ytrends.json"))
REFRESH_HOUR_UTC = 15
REQUIRED = ["keyword", "ltype", "total_listings", "total_sellers", "avg_conversion_rate",
            "opportunity_score", "pct_sold_in_window", "competition_level",
            "as_of_date", "median_data_age_days", "link"]


def norm(keyword):
    return " ".join(keyword.lower().split())


def key(keyword, ltype):
    return f"{ltype or 'any'}|{norm(keyword)}"


def last_refresh(now):
    boundary = now.replace(hour=REFRESH_HOUR_UTC, minute=0, second=0, microsecond=0)
    return boundary if now >= boundary else boundary - timedelta(days=1)


def load():
    try:
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = CACHE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(CACHE_FILE)


def cmd_get(args):
    cache = load()
    cutoff = last_refresh(datetime.now(timezone.utc))
    hits, misses = {}, []
    for kw in args.keywords:
        entry = cache.get(key(kw, args.ltype))
        fresh = entry and datetime.fromisoformat(entry["fetched_at"]) >= cutoff
        if fresh and args.as_of and entry["as_of_date"] != args.as_of:
            fresh = False
        if fresh:
            hits[norm(kw)] = entry
        else:
            misses.append(kw)
    print(json.dumps({"hits": hits, "misses": misses}, ensure_ascii=False, indent=1))


def cmd_put(_args):
    entries = json.load(sys.stdin)
    if isinstance(entries, dict):
        entries = [entries]
    cache = load()
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for entry in entries:
        missing = [k for k in REQUIRED if k not in entry]
        if missing:
            sys.exit(f"Thiếu khóa {missing} ở mục {entry.get('keyword')!r}")
        entry = dict(entry, keyword=norm(entry["keyword"]), fetched_at=now)
        cache[key(entry["keyword"], entry["ltype"])] = entry
    # Bỏ các mục cũ hơn 7 ngày để file không phình ra.
    week_ago = datetime.now(timezone.utc) - timedelta(days=7)
    cache = {k: v for k, v in cache.items()
             if datetime.fromisoformat(v["fetched_at"]) >= week_ago}
    save(cache)
    print(f"Đã lưu {len(entries)} mục vào {CACHE_FILE}")


def cmd_clear(_args):
    CACHE_FILE.unlink(missing_ok=True)
    print("Đã xóa cache")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    get = sub.add_parser("get")
    get.add_argument("keywords", nargs="+")
    get.add_argument("--ltype", choices=["physical", "download"])
    get.add_argument("--as-of")
    get.set_defaults(func=cmd_get)
    sub.add_parser("put").set_defaults(func=cmd_put)
    sub.add_parser("clear").set_defaults(func=cmd_clear)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
