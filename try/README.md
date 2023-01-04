## Trial Version (exlploring)

### create virtual environment:

```
mkdir .venv
conda create -n venv python=3.9
conda activate venv
python3.9 -m venv ./.venv
source ./.venv/bin/activate
conda deactivate
python3 -m pip install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
```

or, run:

```
source ./.venv/bin/activate