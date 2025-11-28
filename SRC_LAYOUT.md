Project `src/` layout

This repository follows the recommended `src` layout for Python projects.

Structure

- `src/` - top-level directory for importable packages
  - `datagenerator/` - main datagenerator package
  - `rockphysics/` - rockphysics package
  - `synthoseis/` - top-level convenience package that aggregates subpackages
- Other project files remain at repository root (docs, scripts, config, notebooks, etc.)

Why `src/`?

Using `src/` keeps importable packages separate from non-package project files and helps avoid accidental imports of the local project during development.

Installation

Install in editable/development mode so changes in the repo are reflected immediately:

```bash
python -m pip install -e .
```

(Use the virtualenv Python if you're using one: `/path/to/venv/bin/python -m pip install -e .`)

Importing

- The project exposes a top-level `synthoseis` package which aggregates the main subpackages. Use:

```python
import synthoseis
# access subpackages
synthoseis.datagenerator
synthoseis.rockphysics
```

- You can also import subpackages directly:

```python
import datagenerator
import rockphysics
```

Packaging notes

- `pyproject.toml` uses `setuptools` to discover packages under `src/` with:

```toml
[tool.setuptools.packages.find]
where = ["src"]
exclude = ["config*", "notebooks*", "img*"]
```

- Keep non-package resources (docs, images, notebooks) at the repo root.

