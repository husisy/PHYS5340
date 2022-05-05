# lec23

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

20220429

Topics

1. Matsubara Green' functions in frequency space
2. Electron-phonon problem
3. Electron self-energy

Goals

1. Understand the new features of the finite-T problem in frequency space
2. Demonstrate the formalism in the electron-phonon problem

## Matsubara Green's functions in frequency space

As usual, let us now Fourier transform to the frequency space. Since all data is contained within the interval $\tau \in \left[ 0,\beta \right]$, we have

$$ \mathcal{G} _{AB}\left( i\omega _n \right) =\int_0^{\beta}{d\tau \mathcal{G} _{AB}\left( \tau \right) e^{i\omega _n\tau}}$$

where the Matsubara frequencies for $n\in\mathbb{Z}$ are

$$ \omega _n=\begin{cases}
   2\pi n/\beta ,\quad \mathrm{bosonic}, \mathrm{periodic}\\
   \left( 2n+1 \right) \pi /\beta ,\quad \mathrm{fermionic},\text{anti-periodic}\\
\end{cases}$$

verify that, for the fermionic one, the phase factor satisfies

$$ e^{i\omega _n\left( \tau +\beta \right)}=e^{i\omega _n\beta}e^{i\omega _{\tau}}=e^{i\left( 2n+1 \right) \pi}e^{i\omega _{\tau}}=-e^{i\omega _{\tau}}$$

as desired.

The inverse transform is now given by

$$ \mathcal{G} _{AB}\left( \tau \right) =\frac{1}{\beta}\sum_n{\mathcal{G} _{AB}\left( i\omega _n \right) e^{-i\omega _n\tau}}$$

As a quick demonstration, let us now apply the general discussions above to the bare Matsubara Green's functions.

Free fermions:

$$ \mathcal{G} \left( k,\tau \right) =-e^{-i\varepsilon _k\tau}\left[ \Theta \left( \tau \right) \left( 1-f\left( \varepsilon _k \right) \right) +\Theta \left( -\tau \right) f\left( \varepsilon _k \right) \right] $$

$$
\begin{align*}
    \mathcal{G} \left( k,i\omega _n \right) &=\int_0^{\beta}{d\tau \mathcal{G} \left( k,\tau \right) e^{i\omega _n\tau}}\\
    &=-\int_0^{\beta}{d\tau e^{-i\varepsilon _k\tau}e^{i\omega _n\tau}\left( 1-f\left( \varepsilon _k \right) \right)}\\
    &=-\left( 1-\frac{1}{e^{\beta \varepsilon _k}+1} \right) \frac{e^{i\left( \omega _n-\varepsilon _k \right) \beta}-1}{i\omega _n-\varepsilon _k}\\
    &\Downarrow \quad e^{i\omega _n\beta}=-1\\
    &=\frac{-1}{e^{-\beta \varepsilon _k}+1}\frac{-\left( e^{-\beta \varepsilon _k}+1 \right)}{i\omega _n-\varepsilon _k}\\
    &=\frac{1}{i\omega _n-\varepsilon _k}
\end{align*}
$$

Free bosons

$$ \mathscr{D} \left( k,\tau \right) =\frac{-1}{2m\omega _k}\left[ \Theta \left( \tau \right) \left( e^{-\omega _k\tau}\left( 1+n\left( \omega _k \right) \right) +e^{\omega _k\tau}n\left( \omega _k \right) \right) +\left( \tau \leftrightarrow -\tau \right) \right] $$

$$
\begin{align*}
    \mathscr{D} \left( k,i\nu _n \right) &=\frac{-1}{2m\omega _k}\int_0^{\beta}{d\tau e^{i\nu _n\tau}\left( e^{-\omega _k\tau}\left( 1+n\left( \omega _k \right) \right) +e^{\omega _k\tau}n\left( \omega _k \right) \right)}\\
    &=\frac{-1}{2m\omega _k}\left[ \left( 1+n\left( \omega _k \right) \right) \frac{e^{\left( i\nu _n-\omega _k \right) \beta}-1}{i\nu _n-\omega _k}+n\left( \omega _k \right) \frac{e^{\left( i\nu _n+\omega _k \right) \beta}-1}{i\nu _n+\omega _k} \right] \\
    &\Downarrow e^{i\nu _n\beta}=1\\
    &=\frac{-1}{2m\omega _k}\left[ \frac{e^{-\beta \omega _k}}{e^{\beta \omega _k}-1}\frac{e^{-\beta \omega _k}-1}{i\nu _n-\omega _k}+\frac{1}{e^{\beta \omega _k}-1}\frac{e^{\beta \omega _k}-1}{i\nu _n+\omega _k} \right] \\
    &=\frac{1}{2m\omega _k}\left[ \frac{1}{i\nu _n-\omega _k}-\frac{1}{i\nu _n+\omega _k} \right]
\end{align*}
$$

Notice how the expressions resemble the zero-temperature results we have derived! In fact, the zero-temperature limit can be recovered by simply "Wick rotation" back to real frequencies (and real time):

$$ i\omega _n\rightarrow \omega $$

$$ i\nu _n\rightarrow \omega $$

In this sense, when defined on the complex plane there is only "one" propagator, although to differentiate, e.g., the retarded vs Feynman propagator, one needs to specify the frequency integral contour (typically through Feynman's $i\varepsilon$ prescription, i.e., for retarded Green's function we Wick rotate by $i\omega_n\to \omega+i\delta$ etc.)

But where is the temperature? In the Matsubara formalism, it is encoded in the spacing between the allowed frequencies. In other words, it is encoded in the sum over frequencies.

Having developed the basic formalism, let's put it to use in a physical problem.

## Electron-phonon problem

Recall the impurity-phonon problem we studied a couple of months ago, which served as our first nontrivial, but still exactly solved problem. After half a semester, let us "promote" our problem to a general quantum many-body problem, and see how we could attack it perturbative.

Consider electrons and phonons described respectively by (here, we roughly follow the notations in Coleman)

$$ \hat{H}_e=\sum_{k\sigma}{\varepsilon _k\hat{c}_{k\sigma}^{\dagger}\hat{c}_{k\sigma}};\quad \varepsilon _k\sim \frac{k^2}{2m}-\mu $$

$$ \hat{H}_{\mathrm{ph}}=\sum_q{\omega _q\hat{a}_{q}^{\dagger}\hat{a}_q};\quad \omega _q\sim c\left| q \right|$$

where for simplicity we have restricted our model to a single phonon mode, say the longitudinal acoustic mode. Let us now consider the possible form of the electron-phonon coupling. As fermion parity is conserved (or, one can say the Hamiltonian is always a bosonic operator) we have to start with a minimum of two fermion operators. In our problem, the electron number is conserved, so we consider some $\hat{c}_{k'\sigma '}^{\dagger}\hat{c}_{k\sigma}$ to start with. Spin rotation invariance requires spin to be a spectator, "dummy" index, and so we have $\sum_{\sigma}{\hat{c}_{k'\sigma}^{\dagger}\hat{c}_{k\sigma}}$. In contrast, the phonon operators can enter "alone" into the Hamiltonian, and so the minimal coupling takes the form

$$ g_{k'kq}\sum_{\sigma}{\hat{c}_{k'\sigma}^{\dagger}\hat{c}_{k\sigma}}\hat{a}_q+\mathrm{h}.\mathrm{c}.$$

Under (discrete) translation, the momentum-space operators pick up phases

$$ \begin{cases}
   \hat{t}_R\hat{c}_{k\sigma}^{\dagger}\hat{t}_{R}^{-1}=e^{-ik\cdot R}\hat{c}_{k\sigma}^{\dagger}\\
   \hat{t}_R\hat{a}_q\hat{t}_{R}^{-1}=e^{-iq\cdot R}\hat{a}_q\\
\end{cases}$$

$$ \Rightarrow \hat{t}_R\hat{c}_{k'\sigma}^{\dagger}\hat{c}_{k\sigma}\hat{a}_q\hat{t}_{R}^{-1}=e^{-i\left( k'-k-q \right) \cdot R}\hat{c}_{k'\sigma}^{\dagger}\hat{c}_{k\sigma}\hat{a}_q$$

and so translation invariance fixes $k'=k+q$

We also assume time-reversal symmetry,

$$\sum_{kq}{g_{kq}\hat{c}_{k+q}^{\dagger}\hat{c}_k\hat{a}_q}\xrightarrow{\mathrm{TR}}\sum_{kq}{g_{kq}^{*}\hat{c}_{\bar{k}+\bar{q}}^{\dagger}\hat{c}_{\bar{k}}\hat{a}_{\bar{q}}}$$

$$ \bar{q}=-q$$

$$ \Rightarrow g_{\bar{k}\bar{q}}=g_{kq}^{*}$$

Lastly, for simplicity let us assume $g_{kq}$ is independent of $k$. This cannot be easily justified based on the "symmetry principles" we are using here, but can be motivated from a more microscopic treatment (similar to our earlier discussion in the impurity-phonon model; see e.g. Coleman 8.7 for details).

These considerations / assumptions bring us down to

$$
\begin{align*}
    \hat{H}_{\text{e-ph}}&=\sum_{kq}{g_q\sum_{\sigma}{\hat{c}_{k+q,\sigma}^{\dagger}\hat{c}_{k\sigma}\hat{a}_q}}+\mathrm{h}.\mathrm{c}.\\
    &=\sum_{kq}{\left( g_q\sum_{\sigma}{\hat{c}_{k+q,\sigma}^{\dagger}\hat{c}_{k\sigma}\hat{a}_q}+g_{q}^{*}\sum_{\sigma}{\hat{c}_{k\sigma}^{\dagger}\hat{c}_{k+q,\sigma}\hat{a}_{q}^{\dagger}} \right)}\\
    &=\sum_{kq}{g_q\sum_{\sigma}{\hat{c}_{k+q,\sigma}^{\dagger}\hat{c}_{k\sigma}\hat{a}_q}}+\sum_{kq}{g_{\bar{q}}^{*}\sum_{\sigma}{\hat{c}_{k\sigma}^{\dagger}\hat{c}_{k+\bar{q},\sigma}\hat{a}_{\bar{q}}^{\dagger}}}\\
    &=\sum_{kq}{g_q\sum_{\sigma}{\hat{c}_{k+q,\sigma}^{\dagger}\hat{c}_{k\sigma}\left( \hat{a}_q+\hat{a}_{\bar{q}}^{\dagger} \right)}}
\end{align*}
$$

The full Hamiltonian $\hat{H}=\hat{H}_e+\hat{H}_{\mathrm{ph}}+\hat{H}_{\text{e-ph}}$ is slightly simplified version of what is known as the "Frohlich Hamiltonian". This can be viewed as the solid analog of QED, in which the role of the EM gauge field is played by the phonons. Note that we ignore e-e interactions here.

Unlike the impurity-phonon model, the current model is not (known to be) exactly solvable. To appreciate why, recall our solution to the impurity-phonon problem relied on the observation that the electron-number operators $\hat{n}_i$ for each orbital commute with the Hamiltonian, i.e., $\left[ \hat{n}_i,\hat{H} \right] =0$. Such conservation of the occupation numbers, however, are not "protected" by any physical principles, and so was instead a special feature of the model we wrote down. Such conservation is absent in the present problem, and as such we can only solve the physical properties perturbatively.

To be more concrete, we split the Hamiltonian into

$$ \hat{H}_0=\hat{H}_e+\hat{H}_{\mathrm{ph}}$$

$$\hat{V}=\hat{H}_{\text{e-ph}}$$

and the perturbation theory is obtained by going to the interaction picture with respect to $\hat{H}_0$. For instance, let us compute the Matsubara electron propagator. Suppressing the spin indices,

$$ \mathcal{G} \left( k,i\omega _n \right) =\int_0^{\beta}{d\tau e^{i\omega _n\tau}\mathcal{G} \left( k,\tau \right)}$$

$$
\begin{align*}
    \mathcal{G} \left( k,\tau \right) &=-\left< \mathcal{T} \left[ \hat{c}_k\left( \tau \right) \hat{c}_{k}^{\dagger}\left( 0 \right) \right] \right> \\
    &=\frac{-\left< \mathcal{T} \left[ \hat{c}_{I,k}\left( \tau \right) \hat{c}_{I,k}^{\dagger}\left( 0 \right) \hat{S}\left( \beta ,0 \right) \right] \right> _0}{\left< \hat{S}\left( \beta ,0 \right) \right> _0}
\end{align*}
$$

where

$$ \left< \cdots \right> _0=\frac{\mathrm{Tr}\left[ e^{-\beta \hat{H}_0}\cdots \right]}{\mathrm{Tr}\left[ e^{-\beta \hat{H}_0} \right]}$$

$$ \hat{S}\left( \beta ,0 \right) =\mathcal{T} \left[ e^{-\int_0^{\beta}{d\tau \hat{V}_I\left( \tau \right)}} \right] $$

as we have mentioned repeatedly, the expression above is essentially identical with the Gell-Mann-Low formula, except for the Euclidean time (and factors of $i$), and the definition of the expectation value (which is thermal).

We now claim without proof that the perturbation expansion is essentially identical to that we have discussed for the zero-temperature problem, in particular

1. Wick's theorem still applies, and so the expectation value $\langle\cdots\rangle_0$ can be evaluated through the combinatorial product and some of the basic contractions
2. The contractions can be organized through diagrams, i.e., we can still use Feynman diagrams
3. The linked cluster theorem holds, and so the presence of the denominator simply instructs us to focus on the connected diagrams
4. Dyson's equation holds, and so we can encode all the interaction correction to the self-energy.

Although we will not prove the validity of the treatment (neither did we really "prove" it for the zero-temperature case; we just tried to explain why it is plausible), it may be good to briefly discuss how one could establish that.

First, for the Wick's theorem, we note that the version needed is a "weaker" version concerning only the expectation values. In the modern treatment this is usually established through a path integral treatment with "sources" inserted, followed by taking functional derivatives. See, e.g., Coleman 8.4 for a discussion.

Alternatively, as a slightly less popular approach one can actually (formally) map the finite-temperature physics to the zero-temperature case by "purifying" the thermal density matrix into a pure state defined on a doubled system. This is called the thermal field dynamics / double. One can then imply that the thermal expectation value form of Wick's theorem through that of the TFD.

One might wonder about the operator version though, which is apparently stronger. Indeed, according to [hep-ph/9601268](https://arxiv.org/abs/hep-ph/9601268) this was a topic of confusion. The conclusion from that paper is that, the operation form still holds, but with a suitably generalized notion of path ordering (replacing time and normal ordering).

Given the Wick's theorem continues to hold, the rest of the discussion follows in essentially the same way. Long story short, we can simply treat the present perturbation theory in the same way as we did. THere are two main differences in practice:

1. The Feynman rules (i.e. transcribing diagrams into mathematical expressions) have some modifications on factors of $i$ versus $-i$ etc.
2. The frequency integrals now become sums over the discrete Matsubara frequencies

Modification (1) is mild; in this course we didn't pay too much attention to those factors anyway (in practice, of course, it is important to get all the factors right in any serious calculation). Modification (ii), in contrast, is more profound. We will see how that is achieved in the following.

## Electron self-energy

Compared to the jellium model, the present perturbation theory is modified in two ways:

1. We have another particle, the phonon, which comes with its own propagator
2. Instead of a (normal ordered) density-density interaction between the electrons, we have a coupling between electrons and phonons.

Diagrammatically, we can represent them by

(1) phonon propagator

![lec23-fig00](data/fig/lec23-fig00.png)

$$
\begin{align*}
    &=\mathscr{D} \left( q,i\nu _n \right) \\
    &=-\int_0^{\beta}{d\tau e^{i\nu _n\tau}\left< \mathcal{T} \left[ \hat{\phi}_q\left( \tau \right) \hat{\phi}_q\left( 0 \right) \right] \right>}\\
    &=\frac{1}{i\nu _n-\omega _q}-\frac{1}{i\nu _n+\omega _q}\\
    &=\frac{2\omega _q}{\left( i\nu _n \right) ^2-\omega _{q}^{2}}
\end{align*}
$$

(2) e-ph coupling vertex $ig_q$

![lec23-fig01](data/fig/lec23-fig01.png)

As one might anticipate from the notations, the phonons can be viewed as mediation interactions between the electrons. Indeed, the following diagram

![lec23-fig02](data/fig/lec23-fig02.png)

$$=\left( ig_q \right) ^2\mathscr{D} _0\left( q,i\nu _n \right) =-g_{q}^{2}\frac{2\omega _q}{\left( i\nu _n \right) ^2-\omega _{q}^{2}}$$

can be understood as an effective interaction. In particular, notice that while $i\nu_n$ corresponds to the energy difference $\sim\varepsilon_{k+q}-\varepsilon_k$, $\omega_q$ is at the phonon energy scale $\omega_D$. Curiously the effective interaction changes sign for $\delta\varepsilon \gtrsim \omega_D$ vs $\delta\varepsilon \lesssim \omega_D$: in particular, the interaction is attractive as $\delta \varepsilon\to 0$. THis corresponds to the celebrated phonon-mediated attraction!

There are of course many questions one could investigate within the electron-phonon model. In the interest of time let us focus on the electron self-energy. Similar to before, we can reconcile the self-energy with the 1PI diagrams:

![lec23-fig03](data/fig/lec23-fig03.png)

Let us focus on the lowest order diagram

![lec23-fig04](data/fig/lec23-fig04.png)

This is actually fairly well-justified as an approximation, but we will not discuss why here in the interest of time (see, e.g., Coleman 8.7.3). Translating our diagram into an expression

![lec23-fig05](data/fig/lec23-fig05.png)

$$
\begin{align*}
    &=\frac{1}{\beta}\sum_{q\nu _n}{-g_{q}^{2}\mathscr{D} \left( q,i\nu _n \right) \mathcal{G} _0\left( k-q,i\left( \omega _n-\nu _n \right) \right)}\\
    &=\frac{1}{\beta}\sum_{q\nu _n}{-g_{q}^{2}\frac{2\omega _q}{\left( i\nu _n \right) ^2-\omega _{q}^{2}}\frac{1}{i\left( \omega _n-\nu _n \right) -\varepsilon _{k-q}}}
\end{align*}
$$

Now we "only" need to evaluate the sum over the Matsubara frequencies -- but how do we do that?
