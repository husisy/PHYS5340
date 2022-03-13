import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# TODO replace lec10-page5
fig,ax = plt.subplots()
tmp0 = (r'$\hat{a}_1\hat{a}_2^\dagger\hat{a}_3^\dagger\hat{a}_4\hat{a}_5\hat{a}_6^\dagger$')
ax.text(0, 0, tmp0, horizontalalignment='center', verticalalignment='center')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
fig.savefig('tbd00.svg')
fig.savefig('tbd00.pdf')
