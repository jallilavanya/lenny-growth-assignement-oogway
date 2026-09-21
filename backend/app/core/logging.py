import logging, json
class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({'timestamp': self.formatTime(record), 'level': record.levelname, 'event': record.getMessage()})
def configure_logging():
    h=logging.StreamHandler(); h.setFormatter(JsonFormatter()); root=logging.getLogger(); root.handlers.clear(); root.addHandler(h); root.setLevel(logging.INFO)
