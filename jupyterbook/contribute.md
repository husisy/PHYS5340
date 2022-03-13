# how to contribute

:::{note}
This is **NOT** the official course PHYS5340 website yet!

* If you are student in this course, **always** take the lecture notes as the correct one if you find any differences between lecture notes and website contents
* If you are just passerby, use the materials below at your own risk. Since the website is still the first version (even alpha version), there could be some typos, incorrect/inaccurate/improper statements.
:::

:::{note}
**All** materials in this website are based on the course offered at HKUST
:::

:::{note}
As a "casual course", we provide only general references but not specific ones to the materials introduced
:::

:::{note}
**All** materials' copyright in this website are reserved for the course lecturer

* If you want to use the material somewhere, you might need to contact the lecturer first
:::

:::{note}
Contribution is always **welcome**. if you find any typo, incorrect/inaccurate/improper statements or necessary references, do not hesitate to

* raise an issue on github repo
* make an pull request on github repo
* contact me directly
:::

contact first, I have to add you to the contributor list first (write permission)

*TODO*: add guide of pull request feature of GitHub

website-version

1. clone the repository locally
   * `git clone xxx`
   * please replace `xxx` with the REAL git-repository link (see it on GitHub website)
2. setup local environment
   * mainly install `jupyterbook` package, please
   * one option: run the code snippet below to setup a separate `conda` environment (should be okay on `win/linux/mac` OS)
   * `pip install ghp-import`
3. make any modification
4. build the website locally
   * at the directory `jupyterbook`, run `jupyter-book build .`
5. view the website locally
   * double click `jupyterbook/_build/html/intro.html` (open this file using the default web-browser)
6. push the modification to GitHub page: `ghp-import -n -p -f _build/html`
7. push the modification to GitHub
   * `git add . -m "Short Summary"`
   * `git push`
8. view the website on GitHub pages

```bash
# setup environment
conda create -y -n jupyterbook
conda install -y -n jupyterbook -c pytorch pytorch torchvision torchaudio cpuonly
conda install -y -n jupyterbook -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum jupyter-book
```

```bash
# build and commit to GitHub
cd jupyterbook
jupyter-book build .
pip install ghp-import
ghp-import -n -p -f _build/html
git add . -m "Short Summary"
git push
```

pdf-version

1. clone the repository locally
   * `git clone xxx`
   * please replace `xxx` with the REAL git-repository link (see it on GitHub website)
2. install texlive environment, following the instruction on the official website [link](https://tug.org/texlive/acquire-netinstall.html)
   * available for both `windows/linux`, I haven't check that on Mac (no device available)
3. make any modification
4. build the pdf file locally
   * at the root directory (where there is a file `main.tex`): `latexmk -pdf main.tex`
   * (optional) clean the build auxiliary files `latexmk -c`
   * (recommend) `vscode` extension `LaTeX-workshop` and `spell check`
5. push the modification to GitHub
   * `git add . "Short Summary"`
   * `git push`

```bash
# build and commit to GitHub
latexmk -pdf main.tex
# latexmk -c
git add . -m "Short Summary"
git push
```
