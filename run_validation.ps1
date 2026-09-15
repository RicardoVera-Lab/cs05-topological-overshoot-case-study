$ErrorActionPreference = 'Stop'
python -m pip install -r requirements.txt
python tests\validate_synthetic.py
