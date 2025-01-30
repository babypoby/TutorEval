#!/usr/bin/bash

curl -fsSL https://ollama.com/install.sh | sh

python3 -m venv venv

source venv/bin/activate

pip install supabase

