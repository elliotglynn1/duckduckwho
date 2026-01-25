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

### 3. Install Java 17 or later (required for PySpark)

This project uses PySpark, which requires Java 17 or later.

**Check your current Java version:**
```bash
java -version
```

**On Mac/Linux:**
```bash
# Using Homebrew (Mac)
brew install openjdk@17

# Or install from Adoptium
# Then set JAVA_HOME in your shell profile (~/.bashrc, ~/.zshrc, etc.)
export JAVA_HOME=/path/to/java17
```

**Verify installation:**
```bash
java -version  # Should show version 17 or higher
echo $JAVA_HOME  # Should show the Java installation path (Linux/Mac)
echo %JAVA_HOME%  # Should show the Java installation path (Windows cmd)
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

Or, since dependencies are in `pyproject.toml`:

```bash
uv pip install -e .
```

### 5. Set your eBird API token

Export your API token to the environment variable `EBIRD_API_TOKEN`.

**On Mac/Linux:**
```bash
export EBIRD_API_TOKEN="your_ebird_api_token"
```

**On Windows (cmd):**
```cmd
set EBIRD_API_TOKEN=your_ebird_api_token
```

### 6. Run the main script

```bash
python main.py
```

## Development

Pre-commit hooks for linting can be enabled by running
```bash
pre-commit --install
```