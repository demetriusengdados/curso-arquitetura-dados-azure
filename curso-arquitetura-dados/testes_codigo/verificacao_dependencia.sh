# Instale pip-audit antes
pip install pip-audit

# Salve este comando em um script chamado `check_dependencies.sh`
#!/bin/bash
echo "Checking for vulnerable dependencies..."
pip-audit
