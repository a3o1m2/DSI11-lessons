<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Python Environment Setup


I stored the environment's package information in an yml-file.

```
conda env export > pymc3_env.yml
```

Now you can create the same environment using

```
conda env create -f pymc3_env.yml
```

Afterwards, run the following to make the environment known to your
notebook kernels:

```
conda activate pymc3_env
python -m ipykernel install --user --name pymc3_env --display-name "pymc3_env"
conda deactivate
```
