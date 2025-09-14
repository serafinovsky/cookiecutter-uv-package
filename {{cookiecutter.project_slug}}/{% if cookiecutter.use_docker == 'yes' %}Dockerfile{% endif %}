FROM python:{{ cookiecutter.python_versions.split()[0].strip() }}-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --dev --frozen --no-install-project
COPY . .
