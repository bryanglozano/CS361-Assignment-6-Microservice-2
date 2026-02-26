Data Storage Microservice Description: This microservice stores and retrieves data a text-file.

It supports:
- writing data
- getting data
it ensures:
- data is stored in a JSON file
- requests are valid JSON
- invalid requests are handled

This microservice communicates using text files, not direct function calls. The test file simulates a main program using the microservice.
communication contract:

microservice 2 description:

Clear instructions for how to programmatically REQUEST data from the microservice:

Example call:

Clear instructions for how to programmatically RECEIVE data from the microservice:

Example call:

UML sequence diagram:

Note to run from repo root:
py src/microservice.py
py tests/test_client.py
