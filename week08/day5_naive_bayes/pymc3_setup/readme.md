<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Python Environment Setup


Check for existing python environments with

```
conda env list
```

If you already created an environment callec `pymc3_env`, run the following, otherwise
continue with the next step:

```
conda remove -n pymc3_env
```

I stored the environment's package information in an yml-file in this folder with

```
conda env export > pymc3_env.yml
```

Now you can create the same environment using

```
conda env create -f pymc3_env.yml
```

Afterwards, run the following to make the environment known to your
notebook kernels and to install python-graphviz:

```
conda activate pymc3_env
conda install -c conda-forge python-graphviz
python -m ipykernel install --user --name pymc3_env --display-name "pymc3_env"
conda deactivate
```
