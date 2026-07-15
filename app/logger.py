# 1. הגדרת לוגר JSON - זה מה שהראש צוות רוצה לראות!
import json
import logging
import sys

from app.config import config


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "app": "football-analytics"
        }
        # אם יש אובייקט של שגיאה, נוסיף אותו
        if hasattr(record, 'match_id'):
            log_obj['match_id'] = record.match_id
        return json.dumps(log_obj)


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(config.log_level)