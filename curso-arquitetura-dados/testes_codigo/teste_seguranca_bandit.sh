# Instale o bandit antes
pip install bandit

# Salve este comando em um script chamado `check_security.sh`
#!/bin/bash
echo "Running security checks with bandit..."
bandit -r your_project_directory
