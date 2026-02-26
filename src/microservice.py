import json
import time
from pathlib import Path

from storage import process_request

PIPE_DIR = Path("pipe")
REQ = PIPE_DIR / "storage_request.txt"
RES = PIPE_DIR / "storage_response.txt"

POLL_SECONDS = 0.1

def write_response(resp: dict) -> None:
    RES.write_text(json.dumps(resp, indent=2))


def main() -> None:
    PIPE_DIR.mkdir(parents=True, exist_ok=True)
    REQ.touch(exist_ok=True)
    RES.touch(exist_ok=True)

    print("Data Storage Microservice running...")
    print(f"Request file: {REQ}")
    print(f"Response file: {RES}")

    while True:
        raw = REQ.read_text().strip()

        if not raw:
            time.sleep(POLL_SECONDS)
            continue

        try:
            req = json.loads(raw)
        except json.JSONDecodeError:
            write_response({
                "ok": False,
                "error": "request must be valid JSON"
            })
            REQ.write_text("")
            continue

        if not isinstance(req, dict):
            write_response({
                "ok": False,
                "error": "request must be a JSON object"
            })
            REQ.write_text("")
            continue

        response = process_request(req)

        RES.write_text("")
        write_response(response)

        REQ.write_text("")

if __name__ == "__main__":
    main()
