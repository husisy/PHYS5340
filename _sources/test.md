---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# test

test kinds of jupyterbook feature

## animation

```{code-cell} ipython3
import numpy as np
import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt
from IPython.display import HTML
fig, ax = plt.subplots()
xdata = np.linspace(0, 2*np.pi, 100)
omega = np.linspace(1, 4, 20)
ydata = np.sin(omega[:,np.newaxis]*xdata)
hline0, = ax.plot(xdata, ydata[0], label=f'omega={omega[0]:.3f}')
hlegend = ax.legend(loc='upper right')
def hf_frame(ind0):
    hline0.set_data(xdata, ydata[ind0])
    label_i = f'{omega[ind0]:.3f}'
    # hline0.set_label(label_i) #doesn't help
    htext = hlegend.get_texts()[0]
    htext.set_text(label_i)
    return hline0,htext
ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(omega), interval=200)
plt.close(fig) #fig is not necessary anymore
HTML(ani.to_jshtml())
```
