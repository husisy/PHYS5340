# lec18

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

20220407

Topics

1. Frequency space Feynman diagrams
2. Self-energy
3. Jellium Hamiltonian

Goals

1. Getting familiarized with how to translate Feynman diagrams to expressions / integrals in the frequency-momentum space
2. Appreciating how the interaction correction to the propagator can be grouped into one single quantity, the self-energy

## Going to frequency space

So far, we have used a "hybrid" discussion with momentum and real time. We have seen that momentum is conserved at each vertex, e.g.,

![lec18-fig00](data/fig/lec18-fig00.png)

which is a consequence of the translation invariance of the full interacting Hamiltonian.

It will be natural to ask if a similar conservation holds for frequency (energy). We expect the answer to be yes, since we are considering a time-independent Hamiltonian. Let us just go through an example in some details to see how that comes about, which hopefully also helps us build up our technical muscle in translating diagrams into expressions.

Recall, the Fourier transform for the (bare) propagator is

$$ G^F\left( k,\omega \right) =\int_{-\infty}^{\infty}{dtG^F\left( k,t \right) e^{i\omega t}e^{-\eta \left| t \right|}}$$

Consider a slightly more complicated diagram in $G^F(k,\omega)$

![lec18-fig01](data/fig/lec18-fig01.png)

The contraction imposes delta-functions in the momenta, and it will be convenient to first consider the effects of that

$$ \begin{cases}
   p_1=k\\
   p_2=p_1+q_1\\
   p_2+q_2=k\\
   p_{2}^{'}-q_2=p_{1}^{'}\\
   p_{1}^{'}-q_1=p_{2}^{'}\\
\end{cases}\quad \Rightarrow \quad \begin{cases}
   p_1=k\\
   p_2=k+q_1\\
   q_2=-q_1\\
   p_{2}^{'}=p_{1}^{'}-q_1\\
\end{cases}$$

$$ \Rightarrow \sum_{p_1p_{1}^{'}q_1p_2p_{2}^{'}q_2}{}=\sum_{p_{1}^{'}q_1}{}$$

i.e., there are only two independent internal momenta. In fact, it will be convenient (and more conventional) to label the diagram using these two momenta

![lec18-fig02](data/fig/lec18-fig02.png)

This corresponds to the expression (suppressing spin)

$$
\begin{align*}
    &\#\int{dtdt_1dt_2e^{i\omega t}\sum_{pq}{V\left( q \right) V\left( -q \right)}}\\
    &\quad\times \left< \hat{c}_{k}^{\cdot}\left( t \right) \hat{c}_{k}^{\dagger \cdot \cdot}\left( 0 \right) \,\,{\color[RGB]{0, 0, 240} \hat{c}_{k+q}^{\dagger \therefore}\hat{c}_{p-q}^{\dagger \therefore \cdot}\hat{c}_{p}^{\therefore \cdot \cdot}\hat{c}_{k}^{\cdot \cdot}}\,\,{\color{red} \hat{c}_{k}^{\dagger \cdot}\hat{c}_{p}^{\dagger \therefore \cdot \cdot}\hat{c}_{p-q}^{\therefore \cdot}\hat{c}_{k+q}^{\therefore}} \right> _{\mathcal{T}}\\
    =&\#\int{dtdt_1dt_2e^{i\omega t}\sum_{pq}{V\left( q \right) V\left( -q \right)}}\\
    &\quad\times \left< \hat{c}_k\left( t \right) {\color{red} \hat{c}_{k}^{\dagger}} \right> _{\mathcal{T}}\left< \hat{c}_{k}^{\dagger}\left( 0 \right) {\color[RGB]{0, 0, 240} \hat{c}_k} \right> _{\mathcal{T}}\left< {\color[RGB]{0, 0, 240} \hat{c}_{k+q}^{\dagger}}{\color{red} \hat{c}_{k+q}} \right> _{\mathcal{T}}\left< {\color[RGB]{0, 0, 240} \hat{c}_{p-q}^{\dagger}}{\color{red} \hat{c}_{p-q}} \right> _{\mathcal{T}}\left< {\color[RGB]{0, 0, 240} \hat{c}_{p}^{\dagger}}{\color{red} \hat{c}_p} \right> _{\mathcal{T}}\\
    \sim& \#\int{dtdt_1dt_2e^{i\omega t}\sum_{pq}{V\left( q \right) V\left( -q \right)}}\\
    &\times G_{0}^{F}\left( k,t-t_2 \right) \left( -G_{0}^{F}\left( k,t_1 \right) \right) \left( -G_{0}^{F}\left( k+q,t_2-t_1 \right) \right) \left( -G_{0}^{F}\left( p-q,t_2-t_1 \right) \right) G_{0}^{F}\left( p,t_1-t_2 \right) \\
    &\quad\Downarrow G_{0}^{F}\left( k,t \right) =\int{\frac{d\omega}{2\pi}G_{0}^{F}\left( k,\omega \right) e^{-i\omega t}}\\
    =&\#\int{dtdt_1dt_2\sum_{pq}{e^{i\omega t}e^{-i\omega _1\left( t-t_2 \right)}e^{-i\omega _2t_1}e^{-i\omega _3\left( t_2-t_1 \right)}e^{-i\omega _4\left( t_2-t_1 \right)}e^{-i\omega _5\left( t_1-t_2 \right)}}}\\
    &\quad \times V\left( q \right) V\left( -q \right) G_0^F\left( k,\omega _1 \right) G_0^F\left( k,\omega _2 \right) G_0^F\left( k+q,\omega _3 \right) G_0^F\left( p-q,\omega _4 \right) G_0^F\left( p,\omega _5 \right)
\end{align*}
$$

Let's focus on the phases

$$ \int{dtdt_1dt_2e^{i\left( \omega -\omega _1 \right) t}e^{i\left( -\omega _2+\omega _3+\omega _4-\omega _5 \right) t_1}e^{i\left( \omega _1-\omega _3-\omega _4+\omega _5 \right) t_2}}$$

$$ \Rightarrow \begin{cases}
   \omega _1=\omega\\
   \omega _2=\omega _3+\omega _4-\omega _5\\
   \omega _5=\omega _3+\omega _4-\omega _1\\
\end{cases}\quad \Rightarrow \begin{cases}
   \omega _1=\omega\\
   \omega _2=\omega\\
   \omega _3=\omega +\omega _5-\omega _4\\
\end{cases}$$

i.e., there are only two independent internal frequencies, which we may choose to parameterize as

$$
\begin{align*}
    &\#\int{\frac{d\tilde{\omega}d\tilde{\omega}}'{\left( 2\pi \right) ^2}\sum_{pq}{V\left( q \right) V\left( -q \right)}}\\
    &\quad V\left( q \right) V\left( -q \right) G_{0}^{F}\left( k,\omega \right) G_{0}^{F}\left( k,\omega \right) G_{0}^{F}\left( k+q,\omega +\tilde{\omega} \right) G_{0}^{F}\left( p-q,\tilde{\omega}' \right) G_{0}^{F}\left( p,\tilde{\omega}+\tilde{\omega}' \right)
\end{align*}
$$

Of course, it would have been much easier to label the frequency in the original diagram, simply by imposing a "frequency (i.e., energy) conservation at every vertex":

![lec18-fig03](data/fig/lec18-fig03.png)

(Note: the wavy lines do not actually depend on the frequency we attached to them, since we considered instantaneous interactions)

Now it should be clearer how to translate the diagram into an expression: we first label all the lines with momentum and frequencies (i.e., 4-momentum in the relativistic case), with the understanding that any internal variables are integrated / summed over. Then each fermion line corresponds to a bare fermion propagator $G_0^F(k,\omega)$, whereas each wavy line corresponds to an interaction term $V(q)$.

The remaining question, important for actual calculations, concerns the prefactor which we did not keep track of (deliberately). It is affected by

1. factors of $-i$: this can be absorbed into the "dictionary"
2. fermionic sign and spin degeneracy: each fermion loop contributes a factor of $-(2S+1)$
3. "symmetry factor": generally speaking, different contraction patterns can lead to the same diagram up to relabeling, and this cancels (partly) the combinatorial factors appearing in the expansion of the exponential. However, high-symmetry diagrams generally appear a fewer number of times than a "generic" diagram, since some "relabelings" collide. This gives a symmetry factor for the diagram.

At this stage, almost every field-theory textbook contains a box (or two) called "the Feynman rules". Let us not repeat them here beyond the sketch above. Instead, see, e.g., Coleman 7.2.

## Dyson's equation and self-energy

Clearly, it was very tedious to keep track of all these factors. It makes sense for us to abstract the expression a bit by writing / drawing

![lec18-fig04](data/fig/lec18-fig04.png)

Furthermore, we have only considered one particular term in the perturbative expansion among the many. One can imagine having arbitrarily complicated diagrams. It will be natural to group all these possibilities into some general blob. That brings us to the notion of Dyson's equation and self-energy.

Our general goal will, again, be ensuring that redundant pieces in the perturbative analysis can be simplified as much as possible. To appreciate how, let us consider expanding the full propagator in terms of the connected diagrams:

![lec18-fig05](data/fig/lec18-fig05.png)

We see that the higher-order terms are basically built around the basic first-order terms taking the form

![lec18-fig06](data/fig/lec18-fig06.png)

Of course, "built" is a vague word to use here. To be more precise, we see that the last two terms are special, in that they are the only ones (among the ones drawn) for which three out of the five bare propagators are at momentum $k$. Indeed, let us translate one of them into explicit expressions

![lec18-fig07](data/fig/lec18-fig07.png)

$$
\begin{align*}
    &G_{0}^{F}\left( k,\omega \right) \left( V\left( q=0 \right) \int{\frac{d\nu dp}{\left( 2\pi \right) ^{d+1}}\mathrm{Tr}\left( G_{0}^{F}\left( p,0^- \right) \right)} \right) \\
    &\times G_{0}^{F}\left( k,\omega \right) \times \left( V\left( q'=0 \right) \int{\frac{d\nu 'dp'}{\left( 2\pi \right) ^{d+1}}\mathrm{Tr}\left( G_{0}^{F}\left( p',0^- \right) \right)} \right) \times G_{0}^{F}\left( k,\omega \right) \\
    =&G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right)
\end{align*}
$$

These kind of terms exist at all orders. E.g., keeping the same form of $G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right)$ but at order $V^3$:

![lec18-fig08](data/fig/lec18-fig08.png)

Notice how the blue parts correspond to the "non-simple" terms in our $O(V^2)$ discussion. And, Also at order $V^3$, we can have terms of the form $G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right) \blacksquare G_{0}^{F}\left( k,\omega \right) $

![lec18-fig09](data/fig/lec18-fig09.png)

Hopefully we have grasped the pattern emerging: the expansion of the full propagator in terms of the connected diagrams can be rewritten schematically as

![lec18-fig10](data/fig/lec18-fig10.png)

From this, we see that we can further restrict our attention to some special classes of diagrams: instead of considering all connected diagrams, it suffices to consider those diagrams which have the following property: it stays connected even if we cut one "internal" fermion line open. We call them "one-particle irreducible", abbreviated as 1PI.

As promised, we arrive at yet another great simplification of the (formal) analysis by introducing $\Sigma$. Translating the diagrams back to equations (suppressing the frequency-momentum dependence)

![lec18-fig11](data/fig/lec18-fig11.png)

$$ G^F=G_{0}^{F}+G_{0}^{F}\Sigma G_{0}^{F}+G_{0}^{F}\left( \Sigma G_{0}^{F} \right) ^2+G_{0}^{F}\left( \Sigma G_{0}^{F} \right) ^3+\cdots $$

As written, it is suggestive that we are simply summing over a geometric series. Indeed, using essentially the same old trick, we see that the expansion above can be drawn / written succinctly as

![lec18-fig12](data/fig/lec18-fig12.png)

$$ G^F=G_{0}^{F}+G_{0}^{F}\Sigma G^F$$

$$ \Rightarrow \quad \left( 1-G_{0}^{F}\Sigma \right) G^F=G_{0}^{F}$$

$$ \Rightarrow \quad G^F\left( k,\omega \right) =\frac{1}{1-G_{0}^{F}\left( k,\omega \right) \Sigma \left( k,\omega \right)}G_{0}^{F}\left( k,\omega \right) $$

where in the last line, we reinstate the $(k,\omega)$ dependence.

To summarize, although we claimed it would be a hard task to compute the "full propagator" in an interacting problem, we can actually condense the entire calculation to that of computing the self-energy $\Sigma(k,\omega)$. Contrast this with the naive approach, in which we expand the numerator and denominator separately, order-by-order!

## Jellium, or, homogeneous electron gas

Having built the machinery needed to tackle interacting quantum many-body problems (perturbatively), let us go back to our motivating example: electrons in free space interacting with each other through Coulomb interaction.

Instead of just having the electrons all by themselves at zero temperature, however, we know that, in practice, almost all "low temperature" systems are electrically neutral. Otherwise, the Coulomb energy diverges as we inter-particle spacing approaches zero. As such, let us instead imagine a homogenous system in which we have a uniform background charge distribution which cancels exactly the charge of the charge of the electron.

The modified interaction is now (passing to a continuum description)

$$ \hat{V}=\frac{e^2}{2}\int{d^3rd^3r'\frac{:\left( \hat{\rho}\left( r \right) -\rho \left( 0 \right) \right) \left( \hat{\rho}\left( r' \right) -\rho \left( 0 \right) \right) :}{\left| r-r' \right|}}$$

$$ \rho _0=\left< \hat{\rho}\left( r \right) \right> $$

where the electron density is

$$ \hat{\rho}\left( r \right) =\sum_{\sigma}{\hat{\Psi}_{r\sigma}^{\dagger}\hat{\Psi}_{r\sigma}}$$
