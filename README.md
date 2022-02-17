# PHYS5340

There are many LaTeX-based books on this topic (quantum many-body physics), but still no website-based (with MathJax support) book is available.

1. better suitable for mooc course: easily to combined with other mooc materials (quiz, code, animation, etc.)
2. could still build a pdf file, although not as good as LaTeX-based
3. an example course on topological insulator [topocondmat.org](https://topocondmat.org/)

An open source book is useful for this research community

1. contribution from the whole community (I guess, mostly those new-learner)
2. students can interact with code (parameters) to see the result

TODO

1. [ ] the derivation step on the course

```bash
conda create -y -n jupyterbook
conda install -y -n jupyterbook -c pytorch pytorch torchvision torchaudio cpuonly
conda install -y -n jupyterbook -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum jupyter-book
```

some abbriation

1. "i.e.": (id est) means “that is” or “in other words”. (It is used to paraphrase a statement that was just made, not to mean“for example”, and is always followed by a comma.)
2. s.t.: such that, so that
3. P.S. stands for postscript. It comes from the Latin postscriptum, which literally means “written after.”

```bash
cd jupyterbook
jupyter-book build . #--all
pip install ghp-import
ghp-import -n -p -f _build/html
```
