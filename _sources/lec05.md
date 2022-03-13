# lec05

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

202200218

Topics

1. Spectral function
2. (Thought) experiment on spectroscopy
3. The zoo of Green's functions
4. Impurity-phonon coupling

Goals

1. developing intuition about Green's and spectral functions
2. Appreciating how they relate to physical problems
3. Applying the techniques to a less trivial and physically relevant problem

## Spectral function

Last time, we were considering a "one-particle" Green's function in a general quantum many-body problem

$$
\begin{align*}
    G_{\alpha \alpha}\left( t \right) &=\left( -i \right) \langle \Omega |\hat{c}_{\alpha}\left( t \right) \hat{c}_{\alpha}^{\dagger}\left( 0 \right) |\Omega \rangle _H\\
    &=\left( -i \right) \sum_n{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2e^{-i\left( E_n-E_{\Omega} \right) t}}
\end{align*}
$$

$$ \Delta E_n=\left( E_n-E_{\Omega} \right) \ge 0$$

where $n$ labels the complete (but unknown) eigenstates of the Hamiltonian. We will continue analyzing how much information we can gain from considering such expressions. We would want to understand the excitation energies. However, in general it is hopeless to try to resolve each of the frequencies. Instead, we should think of a distribution of frequencies, and prominent features will be "peaks" with some widths. This can be done systematically by Fourier transform with respect to time $t$

$$
\begin{align*}
    G_{\alpha \alpha}\left( \omega \right) &\stackrel{?}{=} \int_{-\infty}^{\infty}{dtG_{\alpha \alpha}\left( t \right) e^{i\omega t}}\\
    &=-i\sum_n{\int_{-\infty}^{\infty}{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2e^{i\left( \omega -\Delta E_n \right) t}}}
\end{align*}
$$

But there's a serious issue: the integrand is oscillating as we attempt to Fourier transform with $t\to \pm\infty$. Clearly this is an artifact of our mathematical treatment: we don't know if our universe existed or will exist all the way to $t=\pm\infty$!

Here, let us do two things to circumvent the problem

1. In our thought experiment, we always let the system evolve forward in time when we evaluate the auto-correlation. In other words, we restrict ourselves to $t\geq 0$
2. we won't be able to access $t\to +\infty$ anyway. Let's "damp" the contribution by adding a convergence factor $e^{-\eta t}$ to the integrand, taking $\eta\to 0^+$

$$
\begin{align*}
    G_{\alpha \alpha}\left( \omega \right) &=\lim_{\eta \rightarrow 0^+} \left( -i \right) \int_0^{\infty}{dtG_{\alpha \alpha}\left( t \right) e^{i\omega t}e^{-\eta t}}\\
    &=\lim_{\eta \rightarrow 0^+} \left( -i \right) \sum_n{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2\int_0^{\infty}{e^{i\left( \omega -\Delta E_n+i\eta \right) t}}}\\
    &=\lim_{\eta \rightarrow 0^+} \sum_n{\frac{\left( -i \right) \left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2}{i\left( \omega -\Delta E_n+i\eta \right)}\left( e^{-\eta \left( +\infty \right)}-1 \right)}\\
    &=\lim_{\eta \rightarrow 0^+} \sum_n{\frac{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2}{\omega -\Delta E_n+i\eta}}
\end{align*}
$$

Notes:

1. this explains the convention of attaching $(-i)$ to the definition of $G_{\alpha\alpha}(t)$
2. $G_{\alpha\alpha}(\omega)$ as a function over $\omega$ has a (dense) series of poles at $\omega=\Delta E_n-i\eta$

![lec05-fig00](data/fig/lec05-fig00.png)

But this is still not something we can measure directly! The matrix element $\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2$ is physical: it corresponds to the transition probability of the ground state to some excited state when we add an electron to it. But energy information is hidden in the location of the poles which we displaced below the real line by a sleight of hand. We now claim that, in fact one can identify a "spectral function", closely related to actual experiments, from the frequency-space Green's function:

$$ A_{\alpha \alpha}\left( \omega \right) =\frac{-1}{\pi}\mathrm{Im}\left[ G_{\alpha \alpha}\left( \omega \right) \right] =\sum_n{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2\delta \left( \omega -\Delta E_n \right)}$$

where $\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2$ is the matrix element and $\delta \left( \omega -\Delta E_n \right)$ is the density of states. We will give a "lousy" derivation here first; will revisit later. Noticing

$$ \frac{1}{x+i\eta}=\frac{x}{x^2+\eta ^2}-i\frac{\eta}{x^2+\eta ^2}$$
We will handle the real part later. The imaginary part looks like

![lec05-fig01](data/fig/lec05-fig01.png)

Normalization:

$$ \int_{-\infty}^{\infty}{dx\frac{\eta}{x^2+\eta ^2}}=\pi $$

$$ \Rightarrow \lim_{\eta \rightarrow 0^+} \mathrm{Im}\left[ \frac{1}{x+i\eta} \right] =-\pi \delta \left( 0 \right) $$

This gives

$$
\begin{align*}
    A_{\alpha \alpha}\left( \omega \right) &=\frac{-1}{\pi}\lim_{\eta \rightarrow 0^+} \mathrm{Im}\sum_n{\frac{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2}{\omega -\Delta E_n+i\eta}}\\
    &=\sum_n{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2\delta \left( \omega -\Delta E_n \right)}
\end{align*}
$$

where $\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2\delta(\omega-\Delta E_n)$ is the probability of finding the system in the $|n\rangle$ eigenstate when we add an electron $\hat{c}_{\alpha}^{\dagger}$ to the ground state $|\Omega\rangle$ with energy $\omega$ matching $\Delta E_n$. How can we measure a quantity like that?

STM: trying to add electrons to the sample (approx. in the ground state at low temperature)

![lec05-fig02](data/fig/lec05-fig02.png)

But STM doesn't only try to add electrons! The tip also tries to "pull" electrons out of the sample, i.e., remove electron from the ground state, Similarly for ARPES

![lec05-fig03](data/fig/lec05-fig03.png)

Clearly, there are many more things one can do. We are only starting to see the tip of the iceberg.

## Ground state deduction: a thought experiment

Now, let's imagine plotting this spectral function. First, let us revert to our simple "single-orbital" example


$$ \hat{H}=\varepsilon \left( \hat{c}_{\uparrow}^{\dagger}\hat{c}_{\downarrow}+\hat{c}_{\downarrow}^{\dagger}\hat{c}_{\uparrow} \right) $$

$$ G_{\uparrow \uparrow}\left( t \right) =-i\frac{1}{2}e^{-i\varepsilon t}$$

$$ A_{\uparrow \uparrow}\left( t \right) =\frac{1}{2}\delta \left( \omega -\varepsilon \right) $$

![lec05-fig04](data/fig/lec05-fig04.png)

If this was an experimental result, how would we interpret it? There is a sharp "resonance" when we try to add an up electron with energy $\varepsilon$ to the ground state. The overlap is $\frac{1}{2}$. Suppose we can do similar experiments and measure $A_{\downarrow\downarrow}(\omega)$, as well as those associated with electron electron removal

![lec05-fig05](data/fig/lec05-fig05.png)

we will conclude:

1. Adding $\hat{c}_{\uparrow}^{\dagger}$: sharp resonance with weight $\frac{1}{2}$
2. Adding $\hat{c}_{\downarrow}^{\dagger}$: sharp resonance with weight $\frac{1}{2}$
3. Removing $\hat{c}_{\uparrow}$: sharp resonance with weight $\frac{1}{2}$
4. Removing $\hat{c}_{\downarrow}$: sharp resonance with weight $\frac{1}{2}$

Further, IF we know the relevant Hilbert space is one orbital with spin-$\frac{1}{2}$ electrons, we can conclude

1. (conclusion-a) We can both add and remove electron from the ground state, it must have $1$ electron
2. (conclusion-b) The one electron is in some half-half state between spins up and down (equal weights above)

$$ |\Omega \rangle =\frac{1}{\sqrt{2}}\left( \hat{c}_{\uparrow}^{\dagger}+e^{i\phi}\hat{c}_{\downarrow}^{\dagger} \right) |0\rangle $$

i.e., we know the ground state up to an undetermined phase!

Notes:

1. We assumed above that we can choose to tunnel spin up versus down electrons independently. This is a kind of "resolution", giving "spin-resolved" spectral function (e.g., spin-polarized STM tips). If we don't have such spin resolution, we can only conclude (conclusion-a) but not (conclusion-b). More resolved means more knowledge
2. For such a "small" system, one can imagine cooking up fancier measurements to "better resolve" the system. That's in the spirit of quantum tomography. We don't usually have the luxury of such measurement capability in many-body quantum systems so we won't go further down there.

Let us next imagine plotting the spectral function for a general interacting many-body Hamiltonian

$$ A_{\alpha \alpha}\left( \omega \right) =\sum_n{\left| \langle n|\hat{c}_{\alpha}^{\dagger}|\Omega \rangle \right|^2\delta \left( \omega -\Delta E_n \right)}$$

![lec05-fig06](data/fig/lec05-fig06.png)

![lec05-fig07](data/fig/lec05-fig07.png)

![lec05-fig08](data/fig/lec05-fig08.png)

![lec05-fig09](data/fig/lec05-fig09.png)

Strange situations: featureless over the energy range. If such a spectrum is observed, it suggests either

1. the excitations cannot be understood as quasi-particles
2. quasi-particles exist, but they have poor overlap with the physical electrons

Either will be very interesting! But beyond our scope...

## A peek of the iceberg

In the above, we chose in an ad hoc manner to consider the real-time Green's function

$$ G_{\alpha \alpha}\left( t \right) =\left( -i \right) \langle \Omega |\hat{c}_{\alpha}\left( t \right) \hat{c}_{\alpha}^{\dagger}\left( 0 \right) |\Omega \rangle $$

Since our ground state will have a some finite density of electrons to start with, it will be equally natural to consider, e.g.,

$$ G_{\alpha \alpha}^{\prime}\left( t \right) =\left( -i \right) \langle \Omega |\hat{c}_{\alpha}^{\dagger}\left( t \right) \hat{c}_{\alpha}\left( 0 \right) |\Omega \rangle $$

which contains information about electron removal from $|\Omega\rangle$.

In addition, we don't necessarily have to commit to the "diagonal" form with matched indices. E.g., if $\alpha$ denotes spatial indices, it would be natural to consider

$$ G_{xy}\left( t,t' \right) =\left( -i \right) \langle \Omega |\hat{c}_x\left( t \right) \hat{c}_{y}^{\dagger}\left( t' \right) |\Omega \rangle $$

Our commitment above on $t>0$ is also a bit ad hoc anyway. We should be free ask what happens if we compute "negative time" correlation function, at least as a theoretical gadget. Also, why not do something more than single electron addition (removal)? E.g.,

$$ G_{\alpha \alpha \gamma \delta}^{\prime\prime}\left( t_1,t_2,t_3,t_4 \right) =\left( -i \right) \langle \Omega |\hat{c}_{\alpha}\left( t_1 \right) \hat{c}_{\beta}\left( t_2 \right) \hat{c}_{\gamma}^{\dagger}\left( t_3 \right) \hat{c}_{\delta}^{\dagger}\left( t_4 \right) |\Omega \rangle $$

These discussions suggest that there is a huge zoo of possible "Green's functionS" to consider, and we need a way to organize them, e.g., fix some ordering on the time of "insertions", etc.

Such generalized Green's functions appear under different considerations, and we may want to give them different names, Nevertheless, they are all variations on the same tune, much like Schubert's trout quintet! More later...

## Impurity phonon coupling

So far, we have discussed

1. QHO: coherent states, displacement operator,...
2. Free phonons: collection of decoupled QHOs
3. Localized electrons: a primer into "spectroscopy"

Let us now integrate all these into one single problem: how could we use electrons to probe phonons?

![lec05-fig10](data/fig/lec05-fig10.png)

Similar to before, let us consider a single-site electronic problem:

$$ \hat{H}_e=\sum_{i=1}^N{\varepsilon _i\hat{c}_{i}^{\dagger}\hat{c}_i}$$

let us interpret the index $i$ as labeling some relevant orbitals $s,p,d,\cdots$ and for concreteness we suppose there are $N$ relevant orbitals in our problem. We also consider the free phonon Hamiltonian

$$ \hat{H}_{ph}=\sum_q{\omega _q\hat{a}_{q}^{\dagger}\hat{a}_q}$$

where we have dropped the zero-point energy for simplicity, and take a single branch with uniform masses.

Let us suppose the electronic Hamiltonian describes the electronic states of an impurity located at the origin. The size and shape of the electron cloud surrounding our impurity depends in general on the orbital index $i$. This, in turn, affect the equilibrium position of the neighboring atoms, e.g., a "fatter" electron cloud will push the neighboring atoms further away. We claim this coupling can be modelled as

$$ \hat{H}_{e-ph}=\sum_{i,q}{\hat{c}_{i}^{\dagger}\hat{c}_iM_{iq}\left( \hat{a}_q+\hat{a}_{q}^{\dagger} \right)}$$

We will see why in the next class.
