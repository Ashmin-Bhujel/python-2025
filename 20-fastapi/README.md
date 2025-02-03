# FastAPI

- [x] Install uv (fast project and package manager for python) [ For Linux or Mac ]

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- [x] Create virtual environment

  ```bash
  uv venv
  ```

- [x] Activate virtual environment

  ```bash
  source .venv/bin/activate
  ```

- [x] Install FastAPI

  ```bash
  uv pip install "fastapi[standard]"
  ```

- [x] Run the server

  ```bash
  fastapi dev main.py
  ```

  Open the browser and go to `http://localhost:8000`

- [x] Access the API docs from `http://localhost:8000/docs`
