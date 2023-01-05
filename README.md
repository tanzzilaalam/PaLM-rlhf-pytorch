# Trial Version (exlploring)

## create virtual environment:

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
```

## Custom / random text dataset:

original repo trained with: data/enwik8.gz

original training code: train.py

<br>

<br>

custom trial: downloaded and processed from:

1. https://www.kaggle.com/datasets/yasserh/amazon-product-reviews-dataset

2. https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews

3. https://www.kaggle.com/datasets/grikomsn/amazon-cell-phones-reviews

4. https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products


custom training code (dummy) with cpu: amazon_train.py

### now run the following:

```bash
python amazon_prepare_txtfile.py

amazon_create_tensors.py


```

```bash
python amazon_train.py
```