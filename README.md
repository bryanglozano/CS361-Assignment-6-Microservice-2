Data Storage Microservice Description: This microservice stores and retrieves data a text-file.

It supports:
- writing data
- getting data
it ensures:
- data is stored in a JSON file
- requests are valid JSON
- invalid requests are handled

This microservice communicates using text files, not direct function calls. The test file simulates a main program using the microservice.

communication contract:  This is a text-file based communication, meaning:
- request file: pipe/storage_request.txt
- response file: pipe/storage_response.txt
- Both are json formatted text

Clear instructions for how to programmatically REQUEST data from the microservice:

1. Open pipe/storage_request.txt
2. write json object
3. save & close the file

Request formats:

Write request:
{
  "action": "write",
  "id": "unique_id",
  "data": {...}
}

Get request:
{
  "action": "get",
  "id": "unique_id"
}

Example call:

{
  "action": "write",
  "id": "workout_001",
  "data": {
    "exercise": "Run",
    "minutes": 30
  }
}

Clear instructions for how to programmatically RECEIVE data from the microservice:

The microservice writes a JSON response to: pipe/storage_response.txt

Example call(valid WRITE): 
{
  "ok": true,
  "action": "write",
  "id": "workout_1",
  "message": "stored"
}

Example call(valid GET):
{
  "ok": true,
  "action": "get",
  "id": "workout_1",
  "data": {...}
}

Example call (invalid): 
{
  "ok": false,
  "error": "invalid_request",
  "details": ["error message"]
}

How to run:
1. Clone the repository
2. Make sure you're in the repository root folder (do not run inside /src, /tests, or /pipe)
3. Open a command prompt/terminal and enter:

- python3 src/microservice.py (Linux/Mac)
- python src\microservice.py (Windows)

4. Output should look like this:
Data Storage Microservice running...
Request file: pipe/storage_request.txt
Response file: pipe/storage_response.txt

5. Open a second command prompt/terminal and run the test client:
- python3 tests/test_client.py (Linux/Mac)
- python tests\test_client.py

6. Output should be something similar to this: {'ok': False, 'action': 'get', 'id': 'missing_id', 'error': 'not_found'}

UML sequence diagram:

Note to run from repo root:
py src/microservice.py
py tests/test_client.py
