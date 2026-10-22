"""Update the local Jekyll citation cache; retain the old data on fetch failure."""
import json
import os
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

SCHOLAR_ID = "XpCihyQAAAAJ"
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
OUTPUT = Path(__file__).resolve().parents[1] / "_data" / "scholar.json"


class CitationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_cell = False
        self.cells = []
        self.buffer = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and attrs.get("id") == "gsc_rsb_st":
            self.in_table = True
        if self.in_table and tag == "td" and "gsc_rsb_std" in attrs.get("class", "").split():
            self.in_cell = True
            self.buffer = ""

    def handle_data(self, data):
        if self.in_cell:
            self.buffer += data

    def handle_endtag(self, tag):
        if tag == "td" and self.in_cell:
            self.cells.append(self.buffer.strip())
            self.in_cell = False
        if tag == "table":
            self.in_table = False


def parse_citations(html):
    parser = CitationParser()
    parser.feed(html)
    if len(parser.cells) < 6:
        raise ValueError("Scholar 未返回完整统计表（可能限流或要求验证码）")
    value = parser.cells[0].replace(",", "").replace("\u00a0", "")
    if not re.fullmatch(r"\d+", value):
        raise ValueError("无法识别 Scholar 引用数")
    return int(value)


def main():
    request = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
    data = {
        "scholar_id": SCHOLAR_ID,
        "citedby": parse_citations(html),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": URL,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, OUTPUT)
    print(f"Scholar 引用量已更新：{data['citedby']}；{data['updated_at']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"更新失败，保留原引用量缓存：{error}", file=sys.stderr)
        sys.exit(1)
