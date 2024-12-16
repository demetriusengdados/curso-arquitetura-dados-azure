# Instale pytest e pytest-cov antes
pip install pytest pytest-cov

# Salve este comando em um script chamado `check_coverage.sh`
#!/bin/bash
echo "Running unit tests and coverage analysis..."
pytest --cov=your_project_directory --cov-report=html
