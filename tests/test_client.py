import json
import time
from pathlib import Path

PIPE_DIR = Path("pipe")
REQ = PIPE_DIR / "storage_request.txt"
RES = PIPE_DIR / "storage_response.txt"

POLL_SECONDS = 0.1


def send(req: dict) -> None:
    REQ.write_text(json.dumps(req))


def wait_for_response(timeout: float = 5.0) -> dict:
    start = time.time()

    while time.time() - start < timeout:
        raw = RES.read_text().strip()
        if raw:
            return json.loads(raw)
        time.sleep(POLL_SECONDS)

    raise TimeoutError("Timed out waiting for response")


def clear_response() -> None:
    RES.write_text("")


def main() -> None:
    PIPE_DIR.mkdir(parents=True, exist_ok=True)
    REQ.touch(exist_ok=True)
    RES.touch(exist_ok=True)
    clear_response()

    send({
        "action": "write",
        "id": "workout_001",
        "data": {"exercise": "Run", "minutes": 30}
    })
    print("WRITE ->", wait_for_response())
    clear_response()

    send({
        "action": "get",
        "id": "workout_001"
    })
    print("GET ->", wait_for_response())
    clear_response()

    send({
        "action": "get",
        "id": "missing_id"
    })
    print("GET missing ->", wait_for_response())
    clear_response()


if __name__ == "__main__":
    main()
