#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="agent_experiments"
PYTHON_VERSION="3.12"

# require conda
if ! command -v conda >/dev/null 2>&1; then
    echo "conda not found in PATH. Install Miniconda/Anaconda and try again." >&2
    exit 1
fi

# make conda's activate available so we can create the env non-interactively
CONDA_BASE="$(conda info --base)"
# shellcheck source=/dev/null
source "${CONDA_BASE}/etc/profile.d/conda.sh"

# create env if it doesn't exist
if ! conda env list | grep -qE "(^|[[:space:]])${ENV_NAME}([[:space:]]|$)"; then
    echo "Creating conda environment '${ENV_NAME}' with Python ${PYTHON_VERSION}..."
    conda create -y -n "${ENV_NAME}" "python=${PYTHON_VERSION}"
fi

# activate and install packages
conda activate "${ENV_NAME}"

python -m pip install --upgrade pip
python -m pip install --upgrade google-adk  google-genai ipython jupyter_server