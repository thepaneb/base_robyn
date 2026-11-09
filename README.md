# base_robyn

**A ready-to-use Robyn workspace on VS Code Dev Containers.** Python 3.14 + uv, a modular application skeleton, OpenAPI/ReDoc, and Docker/Compose ready.

<p>
  <a href="https://github.com/new?template_name=base_robyn&template_owner=thepaneb"><img alt="Use this template" src="https://img.shields.io/badge/Use%20this%20template-2ea44f?logo=github&logoColor=white"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white">
  <img alt="Robyn" src="https://img.shields.io/badge/Robyn-0.x-6C47FF">
  <img alt="uv" src="https://img.shields.io/badge/uv-managed-DE5FE9?logo=uv&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white">
</p>

## Why use this template

- **uv for everything** — `uv sync` creates the virtualenv and installs from the committed `uv.lock`.
- **Modular by design** — every folder in `app/modules` is discovered at startup; each module owns its router, routes, models and services.
- **OpenAPI + ReDoc** — routes are registered with OpenAPI metadata, and ReDoc is served by the app.
- **Docker image included** — a slim, locked, `--no-dev` build.
- **Ruff and pytest configured** in `pyproject.toml`.

## Quick start

1. Click **Use this template** → **Create a new repository**.
2. Clone your new repository and open the folder in VS Code.
3. Accept **Reopen in Container** when prompted.
4. Press **F5** → **Debug - DEV** and open http://127.0.0.1:40001.

Requirements: Docker running, VS Code, and the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

## What's inside

```text
.
├── .devcontainer/devcontainer.json   # Python 3.14 + uv, extensions, port 40001
├── .vscode/launch.json               # "Debug - DEV" and "Debug - FAST"
├── app/
│   ├── api/__init__.py               # Robyn app + OpenAPI metadata
│   ├── extensions/
│   │   ├── log/                      # shared logger
│   │   └── routes_loader/            # loads each module's routes/ folder
│   ├── modules/
│   │   ├── hello_world/              # POST /app/hello_world
│   │   ├── redoc/                    # GET /redoc
│   │   └── status/                   # GET /app/status
│   ├── static/redoc.html
│   ├── constants.py                  # BASE_PATH
│   └── run.py                        # module discovery + entry point
├── dev/dependencies.sh               # uv sync
├── Dockerfile
├── dockercompose.yml
├── pyproject.toml
└── uv.lock
```

## How the app is wired

### Startup

`app/run.py` scans `app/modules/*/__init__.py`. Every module that defines `init_module(app)` is imported and called; a module that fails to load is logged and skipped instead of taking the application down.

### Routes

Each module declares a `SubRouter` with a prefix and calls `init_routes(__file__)`, which loads every file in the module's `routes/` folder.

| Method | Path | What it does |
| --- | --- | --- |
| GET | `/app/status` | Health payload (`{"status": "healthy", ...}`) |
| POST | `/app/hello_world` | Returns `Hello, world!` |
| GET | `/redoc` | Serves the ReDoc page |

`BASE_PATH` in `app/constants.py` controls the `/app` prefix.

### Adding a module

1. Create `app/modules/<name>/__init__.py` with an `init_module(app)` function.
2. Create `router.py` with a `SubRouter` and its prefix.
3. Add route files under `routes/`; they are loaded automatically.

## Run and debug

| Action | How | URL |
| --- | --- | --- |
| Dev container | `F5` → **Debug - DEV** or **Debug - FAST** | http://127.0.0.1:40001 |
| Terminal (inside the container) | `ROBYN_PORT=40001 uv run python app/run.py` | http://127.0.0.1:40001 |
| Docker Compose | `docker compose -f dockercompose.yml up --build` | http://localhost:50001 |

Compose maps host `50001` → container `8080`. The app reads `ROBYN_HOST`, `ROBYN_PORT`, `ROBYN_LOG_LEVEL`, `ROBYN_PROCESSES` and `ROBYN_WORKERS` from the environment.

## Customize

- **Dependencies:** edit `pyproject.toml`, run `uv lock` and commit the updated `uv.lock`.
- **Prefix:** change `BASE_PATH` in `app/constants.py`.
- **Ports:** `.devcontainer/devcontainer.json` (`40001`) and `dockercompose.yml` (`50001`).
- **Docker:** the image runs `python run.py --fast`; adjust `CMD` for your deployment.

## License

This template does not ship a license file. Add one if you plan to distribute derived work.
