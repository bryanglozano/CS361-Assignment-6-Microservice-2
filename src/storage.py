
import json
from pathlib import Path
from typing import Any, Dict, List

store_file = Path("pipe") / "data_store.json"

def load_store() -> Dict [str, Any]:
  if not store_file.exists():
    return {}
  raw = store_file.read_text().strip()
  if not raw:
    return {}
  try:
    return json.loads(raw)
  except json.JSONDecodeError:
    return {}
def save_store(store: Dict[str, Any]) -> None:
  store_file.parent.mkdir(parents=True, exist_ok=True)
  store_file.write_text(json.dumps(store, indent=2))
def process_request(req: Dict[str, Any]) -> Dict[str, Any]:
  errors: List[str] = []
  action = req.get("action")
  id = req.get("id")
  if action not in ("write", "get"):
    errors.append("action must be 'write' or 'get'")
  if not isinstance(id, str) or not id.strip():
    errors.append("id must be a non-empty string")
  if errors:
    return {"ok": False, "error": "invalid_request", "details": errors}
  store = load_store()
  if action == "write":
    data = req.get("data")
    if not isinstance(data, dict):
      return {
                "ok": False,
                "action": "write",
                "id": id,
                "error": "data must be an object"
        }
    store[id] = data
    save_store(store)
    return {
            "ok": True,
            "action": "write",
            "id": id,
            "message": "stored"
        }
  if _id not in store:
        return {
            "ok": False,
            "action": "get",
            "id": id,
            "error": "not_found"
        }
  return {
        "ok": True,
        "action": "get",
        "id": id,
        "data": store[id]
    }
