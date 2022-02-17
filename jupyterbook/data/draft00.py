import os
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

hf_file = lambda *x: os.path.join('fig',*x)

fig,ax = plt.subplots(figsize=(6,3))
ax.plot([-0.35, 0.35], [-0.5,-0.5], color='k')
ax.plot([-0.35, 0.35], [0.5,0.5], color='k')
ax.plot([-1, -0.3], [0,0], color='k')
ax.plot([1, 0.3], [0,0], color='k')
text_kwargs = dict(fontsize=15, horizontalalignment='center', verticalalignment='center')
ax.text(0.5, -0.5, r'$-\varepsilon$', **text_kwargs)
ax.text(0.5, 0.5, r'$\varepsilon$', **text_kwargs)
ax.text(1.1, 0, r'$0$', **text_kwargs)
ax.text(0, 0.6, r'$\hat{c}_+^\dagger|0\rangle$', **text_kwargs)
ax.text(0, -0.4, r'$\hat{c}_-^\dagger|0\rangle$', **text_kwargs)
ax.text(-0.6, 0.1, r'$|0\rangle$', **text_kwargs)
ax.text(0.6, 0.1, r'$\hat{c}_\uparrow^\dagger\hat{c}_\downarrow^\dagger|0\rangle$', **text_kwargs)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1, 1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
fig.tight_layout()
fig.savefig(hf_file('lec04-fig01.png'))
