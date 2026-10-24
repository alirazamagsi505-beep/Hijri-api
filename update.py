from hijri_converter import Gregorian
from datetime import datetime, timedelta
import json, os
today = datetime.utcnow() + timedelta(hours=5)
h = Gregorian(today.year, today.month, today.day).to_hijri()
path = "hijri/calendar/jafria/1448.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)
date_str = today.strftime("%Y-%m-%d")
data["last_updated"] = today.isoformat()
data["today"] = {"gregorian": date_str, "hijri_day": h.day, "hijri_month": h.month, "hijri_year": h.year}
data["days"][date_str] = {"d": h.day, "m": h.month, "y": h.year}
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
