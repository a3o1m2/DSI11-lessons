<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Tensorflow environment setup

```
conda create -n tensorflow_env python=3.7.4
conda activate tensorflow_env
conda install ipykernel
pip install tensorflow
conda install -c conda-forge matplotlib seaborn scikit-learn
conda install -c conda-forge python-graphviz
conda install -c conda-forge pydotplus
python -m ipykernel install --user --name tensorflow_env --display-name "tensorflow_env"
conda deactivate
```
