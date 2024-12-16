# Instale pylint antes
pip install pylint

# Salve este comando em um script chamado `check_quality.sh`
#!/bin/bash
echo "Running code quality checks with pylint..."
pylint your_project_directory
