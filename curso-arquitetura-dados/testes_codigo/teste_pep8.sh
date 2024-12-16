# Instale o flake8 antes
pip install flake8

# Salve este comando em um script chamado `check_style.sh`
#!/bin/bash
echo "Running PEP8 style checks with flake8..."
flake8 your_project_directory --max-line-length=88 --exclude=venv,.git,__pycache__
