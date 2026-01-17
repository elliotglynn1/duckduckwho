# duckduckwho
Bird watching app, for keen ornithologists.

## How to use

### 1. Install `uv` (fast Python package manager)

```bash
pip install uv
```

### 2. Create and activate a virtual environment

```bash
uv venv .venv
source .venv/bin/activate
```
*On Windows, use:*
```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

Or, since dependencies are in `pyproject.toml`:

```bash
uv pip install -e .
```

### 4. Set your eBird API token

Export your API token to the environment variable `EBIRD_API_TOKEN`.

**On Mac/Linux:**
```bash
export EBIRD_API_TOKEN="your_ebird_api_token"
```

**On Windows (cmd):**
```cmd
set EBIRD_API_TOKEN=your_ebird_api_token
```

### 5. Run the main script

```bash
python main.py
```

