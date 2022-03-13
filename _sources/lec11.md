# lec11

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

20220311

Topics

1. Wick's theorem and Gaussian states
2. Wicks' theorem, time-ordering and time-ordered exponential

Goals

1. Appreciating what is means to be "free", "Gaussian", "non-interacting" (mean-field)
2. Completing our explicit evaluation of the time-ordered exponential

## Gaussian states

In introducing the normal ordering, we tried to emphasize that its definition is implicitly dependent on a reference state, and so, correspondingly, the value of the contraction also depends on the reference state. We had already argued that the contraction simply equals to the "two-point" correlation function of the reference state. Let us show this more explicitly in a single QHO example.

To this end, let us introducing the notion of a "squeezed state" ( quantum optics terminology)

$$ |\zeta \rangle =\underset{\hat{S}\left( \zeta \right)}{\underbrace{e^{i\left( \zeta \hat{a}^{\dagger 2}+\zeta ^*\hat{a}^2 \right) /2}}}|0\rangle $$

We see that the squeezed state is "rotated" from the vacuum by a unitary, called the "squeezed operator"

$$ \hat{S}\left( \zeta \right) =e^{i\left( \zeta \hat{a}^{\dagger 2}+\zeta ^*\hat{a}^2 \right) /2}$$

Note: our notation here differs from the usual quantum optics discussion by a factor of $i$. This is done for our convenience in what follows.

We claim the squeezed state is "Gaussian", and that the Wick's theorem can be applied to facilitate the evaluation of expectation values. To that end, let us first consider how the squeeze operator transform the annihilation and creation operators:

$$ \hat{S}\left( \zeta \right) \hat{a}^{\dagger}\hat{S}^{\dagger}\left( \zeta \right) =\left. e^{i\left( \zeta \hat{a}^{\dagger 2}+\zeta ^*\hat{a}^2 \right) t/2}\hat{a}^{\dagger}e^{i\left( \zeta \hat{a}^{\dagger 2}+\zeta ^*\hat{a}^2 \right) t/2} \right|_{t=1}$$

where instead of computing it directly (with BCH type formulas), we use a trick that the transformation can be interpreted as a kind of Heisenberg picture evolution with a "squeezing Hamiltonian"

$$ i\partial _t\hat{a}^{\dagger}=\left[ \hat{a}^{\dagger},\frac{1}{2}\left( \zeta \hat{a}^{\dagger 2}+\zeta ^*\hat{a}^2 \right) \right] =-\zeta ^*\hat{a}$$

$$ \Rightarrow \quad \partial _t\left( \begin{array}{c}
  \hat{a}\\
  \hat{a}^{\dagger}\\
\end{array} \right) =i\left( \begin{matrix}
  0&    -\zeta\\
  \zeta ^*&    0\\
\end{matrix} \right) \left( \begin{array}{c}
  \hat{a}\\
  \hat{a}^{\dagger}\\
\end{array} \right)$$

$$ \Rightarrow \quad \left( \begin{array}{c}
  \hat{a}\left( t \right)\\
  \hat{a}^{\dagger}\left( t \right)\\
\end{array} \right) =\exp \left( i\left( \begin{matrix}
  0&    -\zeta\\
  \zeta ^*&    0\\
\end{matrix} \right) t \right) \left( \begin{array}{c}
  \hat{a}\left( 0 \right)\\
  \hat{a}^{\dagger}\left( 0 \right)\\
\end{array} \right)$$

For simplicity, let us further assume $\zeta=i\theta$ is purely imaginary. Then

$$
\begin{align*}
    \exp \left( it\left( \begin{matrix}
        0&    -i\theta\\
        -i\theta&    0\\
    \end{matrix} \right) \right) &=\exp \left( \theta t\sigma _x \right) \\
    &=\sum_{n:\mathrm{even}}{\frac{1}{n!}\left( \theta t \right) ^n}+\sigma _x\sum_{n:\mathrm{odd}}{\frac{1}{n!}\left( \theta t \right) ^n}\\
    &=\cosh \left( \theta t \right) +\sigma _x\sinh \left( \theta t \right)
\end{align*}
$$

$$ \Rightarrow \quad \left( \begin{array}{c}
  \hat{a}\left( t \right)\\
  \hat{a}^{\dagger}\left( t \right)\\
\end{array} \right) =\left( \begin{matrix}
  \cosh \left( \theta t \right)&    \sinh \left( \theta t \right)\\
  \sinh \left( \theta t \right)&    \cosh \left( \theta t \right)\\
\end{matrix} \right) \left( \begin{array}{c}
  \hat{a}\left( 0 \right)\\
  \hat{a}^{\dagger}\left( 0 \right)\\
\end{array} \right) $$

Setting $t=1$, we get

$$ \hat{S}\left( i\theta \right) \hat{a}\hat{S}^{\dagger}\left( i\theta \right) =\cosh \theta \hat{a}+\sinh \theta \hat{a}^{\dagger}$$

Note: you might recognize this as a "Bogoliubov transformation", usually discussed by asking what linear transformations of the bosonic operators will preserve the canonical commutation relations. We have, in fact, shown explicitly how the transformation can be achieved by the conjugate action of a unitary generated by a boson-bilinear.

With such preparation, let us verify that $|\zeta =i\theta \rangle$ is indeed a Gaussian state. For simplicity, we define

$$
\begin{align*}
    \hat{b}&=\hat{S}\left( i\theta \right) \hat{a}\hat{S}^{\dagger}\left( i\theta \right) \\
    &=\cosh \theta \hat{a}+\sinh \theta \hat{a}^{\dagger}
\end{align*}
$$

and the canonical commutation relation is preserved:

$$ \left[ \hat{b},\hat{b}^{\dagger} \right] =\hat{S}\left( i\theta \right) \left[ \hat{a},\hat{a}^{\dagger} \right] \hat{S}^{\dagger}\left( i\theta \right) =1$$

These are annihilation and creation operators, in that

$$ \hat{b}|i\theta \rangle =\hat{S}\left( i\theta \right) \hat{a}\hat{S}^{\dagger}\left( i\theta \right) \hat{S}\left( i\theta \right) |0\rangle =\hat{S}\left( i\theta \right) \hat{a}|0\rangle =0$$

With respect to $|i\theta \rangle$, therefore, it will be natural to define the normal order to be one in which $\hat{b}^\dagger$ is always brought to the left of $\hat{b}$.

The "new" normal order is then, for instance,

$$
\begin{align*}
    :\hat{a}^{\dagger}\hat{a}:&=:\left( -\sinh \theta \hat{b}+\cosh \theta \hat{b}^{\dagger} \right) \left( \cosh \theta \hat{b}-\sinh \theta \hat{b}^{\dagger} \right) :\\
    &=-\sinh \theta \cosh \theta \hat{b}^2+\cosh ^2\theta \hat{b}^{\dagger}\hat{b}+\sinh ^2\theta {\color{red} :\hat{b}\hat{b}^{\dagger}:}-\sinh \theta \cosh \theta \hat{b}^{\dagger 2}
\end{align*}
$$

correspondingly, the contraction becomes

$$ \hat{a}^{\dagger \bullet}\hat{a}^{\bullet}=\hat{a}^{\dagger}\hat{a}-:\hat{a}^{\dagger}\hat{a}:=\sinh ^2\theta \left[ \hat{b},\hat{b}^{\dagger} \right] =\sinh ^2\theta $$

Similarly,

$$ \hat{a}^{\bullet}\hat{a}^{\dagger \bullet}=\hat{a}\hat{a}^{\dagger}-:\hat{a}\hat{a}^{\dagger}:=\cosh ^2\theta $$

As argued, the contractions can be evaluated simply by looking at the "two-point" correlations. Explicitly, we have, e.g.,

$$
\begin{align*}
    \langle i\theta |\hat{a}^{\dagger}\hat{a}|i\theta \rangle &=\langle 0|\hat{S}^{\dagger}\left( i\theta \right) \hat{a}^{\dagger}\hat{a}\hat{S}\left( i\theta \right) |0\rangle \\
    &=\langle 0|\left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) \left( \cosh \theta \hat{a}-\sinh \theta \hat{a}^{\dagger} \right) |0\rangle \\
    &=\sinh ^2\theta \\
    &=\hat{a}^{\dagger \bullet}\hat{a}^{\bullet}
\end{align*}
$$

Similarly, we can evaluate

$$
\begin{align*}
    \hat{a}^{\dagger \bullet}\hat{a}^{\dagger \bullet}&=\langle i\theta |\hat{a}^{\dagger}a^{\dagger}|i\theta \rangle \\
    &=\langle 0|\left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) ^2|0\rangle \\
    &=-\sinh \theta \cosh \theta
\end{align*}
$$

The power of the Wick's theorem will be more apparent when we look at a longer string of operators. For instance, consider

$$
\begin{align*}
    \langle i\theta |\left( \hat{a}^{\dagger}a \right) ^2|i\theta \rangle &=\langle i\theta |\left[ \left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) \left( \cosh \theta \hat{a}-\sinh \theta \hat{a}^{\dagger} \right) \right] ^2|i\theta \rangle \\
    &=\langle i\theta |\left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) \left( \cosh \theta \hat{a}-\sinh \theta \hat{a}^{\dagger} \right) \\
    &\quad\times \left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) \left( \cosh \theta \hat{a}-\sinh \theta \hat{a}^{\dagger} \right) |i\theta \rangle \\
    &=\sinh ^2\theta \langle i\theta |\hat{a}\left( \cosh \theta \hat{a}-\sinh \theta \hat{a}^{\dagger} \right) \left( -\sinh \theta \hat{a}+\cosh \theta \hat{a}^{\dagger} \right) \hat{a}^{\dagger}|i\theta \rangle \\
    &=\sinh ^2\theta \left( \sinh ^2\theta \langle 0|\hat{a}\hat{a}^{\dagger}\hat{a}\hat{a}^{\dagger}|0\rangle +\cosh ^2\theta \langle 0|\hat{a}\hat{a}\hat{a}^{\dagger}\hat{a}^{\dagger}|0\rangle \right) \\
    &=\sinh ^2\theta \left( \sinh ^2\theta +2\cosh ^2\theta \right)
\end{align*}
$$

Alternatively, we can write down by wick's theorem

$$
\begin{align*}
    \langle i\theta |\left( \hat{a}^{\dagger}a \right) ^2|i\theta \rangle &=\langle \hat{a}^{\dagger}a\hat{a}^{\dagger}a\rangle \\
    &=\langle \hat{a}^{\dagger}a\rangle ^2+\langle \hat{a}^{\dagger}a\rangle \langle a\hat{a}^{\dagger}\rangle +\langle \hat{a}^{\dagger}\hat{a}^{\dagger}\rangle \langle aa\rangle \\
    &=\sinh ^4\theta +\sinh ^2\theta \cosh ^2\theta +\left( -\sinh \theta \cosh \theta \right) ^2\\
    &=\sinh ^2\theta \left( \sinh ^2\theta +2\cosh ^2\theta \right)
\end{align*}
$$

as promised.

## Still remember the main thread?

time to add time back: T-contraction

If you still remember, our goal was to establish

$$ \langle 0|\mathcal{T} \left[ e^{-i\int_0^t{dt'\left( \zeta \left( t' \right) \hat{a}^{\dagger}\left( t' \right) +\zeta ^*\left( t' \right) \hat{a}\left( t' \right) \right)}} \right] |0\rangle =e^{-i\int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}}}$$

$$ \mathscr{G} \left( t_1-t_2 \right) =-i\Theta \left( t_1-t_2 \right) e^{-i\omega \left( t_1-t_2 \right)}$$

and by noticing

$$ \mathrm{LHS}=\sum_{n=0}{\frac{\left( -i \right) ^{2n}}{\left( 2n \right) !}\langle 0|\mathcal{T} \left[ \left( \int_0^t{dt'\hat{\phi}\left( t' \right)} \right) ^n \right] |0\rangle}$$

we wandered into a (long) discussion of how to compute such VEV through Wick's theorem. Now, with Wick's theorem under our belt, we would just need to consider how that "interacts" with the time-ordering upfront.

To see what the new feature is, let's start with the case of two operators: $\hat{\phi}_1$ inserted at time $t_1$ and $\hat{\phi}_2$ inserted at time $t_2$

$$ \mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2 \right] =\Theta \left( t_1-t_2 \right) \hat{\phi}_1\hat{\phi}_2+\Theta \left( t_2-t_1 \right) \hat{\phi}_2\hat{\phi}_1$$

where we have used the Heaviside step function to explicitly select the correct ordering of the operators. Now we might apply Wick's theorem to the operators

$$
\begin{align*}
    \mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2 \right] &=\Theta \left( t_1-t_2 \right) \left( :\hat{\phi}_1\hat{\phi}_2:+\hat{\phi}_{1}^{\bullet}\hat{\phi}_{2}^{\bullet} \right) +\Theta \left( t_2-t_1 \right) \left( :\hat{\phi}_2\hat{\phi}_1:+\hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet} \right) \\
    &=:\hat{\phi}_1\hat{\phi}_2:+\Theta \left( t_1-t_2 \right) \hat{\phi}_{1}^{\bullet}\hat{\phi}_{2}^{\bullet}+\Theta \left( t_2-t_1 \right) \hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet}
\end{align*}
$$

let us define a "T-contraction" (terminology from 1710.09248):

$$
\begin{align*}
    \overbrace{\hat{\phi}_1\hat{\phi}_2}&=\mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2 \right] -:\hat{\phi}_1\hat{\phi}_2:\\
    &=\Theta \left( t_1-t_2 \right) \hat{\phi}_{1}^{\bullet}\hat{\phi}_{2}^{\bullet}+\Theta \left( t_2-t_1 \right) \hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet}
\end{align*}
$$

We now claim the Wick's theorem applies in the same way for a time-ordered product simply by replacing all the contractions by T-contractions.

To illustrate this, suppose $t_2>t_3>t_1$, then

$$
\begin{align*}
    \mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2\hat{\phi}_3 \right] &=\hat{\phi}_2\hat{\phi}_3\hat{\phi}_1\\
    &=:\hat{\phi}_1\hat{\phi}_2\hat{\phi}_3:+\hat{\phi}_{2}^{\bullet}\hat{\phi}_{3}^{\bullet}\hat{\phi}_1+\hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet}\hat{\phi}_3+\hat{\phi}_{3}^{\bullet}\hat{\phi}_{1}^{\bullet}\hat{\phi}_2
\end{align*}
$$

and indeed we have

$$ \overbrace{\hat{\phi}_1\hat{\phi}_2}=\Theta \left( t_1-t_2 \right) \hat{\phi}_{1}^{\bullet}\hat{\phi}_{2}^{\bullet}+\Theta \left( t_2-t_1 \right) \hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet}=\hat{\phi}_{2}^{\bullet}\hat{\phi}_{1}^{\bullet}$$

$$ \overbrace{\hat{\phi}_2\hat{\phi}_3}=\Theta \left( t_2-t_3 \right) \hat{\phi}_{2}^{\bullet}\hat{\phi}_{3}^{\bullet}+\Theta \left( t_3-t_2 \right) \hat{\phi}_{3}^{\bullet}\hat{\phi}_{2}^{\bullet}=\hat{\phi}_{2}^{\bullet}\hat{\phi}_{3}^{\bullet}$$

$$ \overbrace{\hat{\phi}_1\hat{\phi}_3}=\Theta \left( t_1-t_3 \right) \hat{\phi}_{1}^{\bullet}\hat{\phi}_{3}^{\bullet}+\Theta \left( t_3-t_1 \right) \hat{\phi}_{3}^{\bullet}\hat{\phi}_{1}^{\bullet}=\hat{\phi}_{3}^{\bullet}\hat{\phi}_{1}^{\bullet}$$

So we have, explicitly,

$$ \mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2\hat{\phi}_3 \right] =:\hat{\phi}_1\hat{\phi}_2\hat{\phi}_3:+\overbrace{\hat{\phi}_2\hat{\phi}_3}\hat{\phi}_1+\overbrace{\hat{\phi}_2\hat{\phi}_1}\hat{\phi}_3+\overbrace{\hat{\phi}_3\hat{\phi}_1}\hat{\phi}_2$$

as claimed.

Long story short, no matter how the times are really ordered, we can apply the original Wick's theorem to the time-ordered product. However, the order of contraction might have been reversed if the two operators are swapped under the time ordering. The T-contraction takes care of such possible swapping (or not) using the Heaviside step function to toggle between the two.

In addition, we also inherit the general conclusion that the T-contraction can be computed as a "correlation function"

$$ \langle GS|\mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2 \right] |GS\rangle =\langle GS|:\hat{\phi}_1\hat{\phi}_2:|GS\rangle +\overbrace{\hat{\phi}_1\hat{\phi}_2}=\overbrace{\hat{\phi}_1\hat{\phi}_2}$$

provided that the state is Gaussian such that there exists a definition of normal ordering with respect to that. We emphasize that we do not need to perform the actual normal ordering (basis rotation etc.) to evaluate the contraction. Its value is computed through

$$ \overbrace{\hat{\phi}_1\hat{\phi}_2}=\langle \mathcal{T} \left[ \hat{\phi}_1\hat{\phi}_2 \right] \rangle =\Theta \left( t_1-t_2 \right) \langle \hat{\phi}_1\left( t_1 \right) \hat{\phi}_2\left( t_2 \right) \rangle +\Theta \left( t_2-t_1 \right) \langle \hat{\phi}_1\left( t_2 \right) \hat{\phi}_2\left( t_1 \right) \rangle $$

where the first term is the Green's function!

## Finally: Time-ordered exponential meets Green's functions

After 20 pages or so we are finally ready to evaluate the time-ordered exponential

$$ \hat{\phi}\left( t' \right) =\zeta \left( t' \right) \hat{a}^{\dagger}\left( t' \right) +\zeta ^*\left( t' \right) \hat{a}\left( t' \right) $$

$$
\begin{align*}
    &\langle 0|\mathcal{T} \left[ e^{-i\int_0^t{dt'\hat{\phi}\left( t' \right)}} \right] |0\rangle \\
    =&\sum_{n=0}{\frac{\left( -i \right) ^{2n}}{\left( 2n \right) !}\langle 0|\mathcal{T} \left[ \int_0^t{dt_1\int_0^t{dt_2\cdots \int_0^t{dt_n\hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) \cdots \hat{\phi}\left( t_{2n} \right)}}} \right] |0\rangle}\\
    =&\sum_{n=0}{\frac{\left( -i \right) ^{2n}}{\left( 2n \right) !}\int_0^t{dt_1\int_0^t{dt_2\cdots \int_0^t{dt_n{\color{red} \langle 0|\mathcal{T} \left[ \hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) \cdots \hat{\phi}\left( t_{2n} \right) \right] |0\rangle }}}}}
\end{align*}
$$

$$
\begin{align*}
    &{\color{red} \langle 0|\mathcal{T} \left[ \hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) \cdots \hat{\phi}\left( t_{2n} \right) \right] |0\rangle }\\
    =&\overbrace{\hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) }\overbrace{\hat{\phi}\left( t_3 \right) \hat{\phi}\left( t_4 \right) }\cdots \overbrace{\hat{\phi}\left( t_{2n-1} \right) \hat{\phi}\left( t_{2n} \right) }\\
    &\quad+\overbrace{\hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_3 \right) }\overbrace{\hat{\phi}\left( t_2 \right) \hat{\phi}\left( t_4 \right) }\cdots \overbrace{\hat{\phi}\left( t_{2n-1} \right) \hat{\phi}\left( t_{2n} \right) }\\
    &\quad+\cdots ;\quad \left( 2n-1 \right) !! \mathrm{terms}
\end{align*}
$$

Now, we evaluate

$$
\begin{align*}
    &\overbrace{\hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) }\\
    =&\langle 0|\mathcal{T} \left[ \hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) \right] |0\rangle \\
    =&\Theta \left( t_1-t_2 \right) \langle 0|\left( \zeta \left( t_1 \right) \hat{a}^{\dagger}\left( t_1 \right) +\zeta ^*\left( t_1 \right) \hat{a}\left( t_1 \right) \right)\\
    &\quad \times \left( \zeta \left( t_2 \right) \hat{a}^{\dagger}\left( t_2 \right) +\zeta ^*\left( t_2 \right) \hat{a}\left( t_2 \right) \right) |0\rangle +\left( t_1\leftrightarrow t_2 \right) \\
    =&\Theta \left( t_1-t_2 \right) \zeta ^*\left( t_1 \right) \zeta \left( t_2 \right) \langle 0|\hat{a}e^{-i\omega t_1}\hat{a}^{\dagger}e^{i\omega t_2}|0\rangle +\left( t_1\leftrightarrow t_2 \right) \\
    =&\Theta \left( t_1-t_2 \right) \zeta ^*\left( t_1 \right) \zeta \left( t_2 \right) e^{-i\omega \left( t_1-t_2 \right)}+\left( t_1\leftrightarrow t_2 \right)
\end{align*}
$$

We defined

$$ \mathscr{G} \left( t_1-t_2 \right) =\left( -i \right) \Theta \left( t_1-t_2 \right) e^{-i\omega \left( t_1-t_2 \right)}$$

$$
\begin{align*}
    \Rightarrow \quad &\int_0^t{dt_1\int_0^t{dt_2\overbrace{\hat{\phi}\left( t_1 \right) \hat{\phi}\left( t_2 \right) }}}\\
    =&\frac{1}{\left( -i \right)}\int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}}+\left( t_1\leftrightarrow t_2 \right) \\
    =&\left( 2i \right) \int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}}
\end{align*}
$$

In addition, all the other full contractions generated by Wick's theorem correspond to exactly the same expression but with some relabeling of the time indices. In other words, all the $(2n-1)!!$ terms evaluate to the same answer. We can finally write down

$$
\begin{align*}
    &\langle 0|\mathcal{T} \left[ e^{-i\int_0^t{dt'\left( \zeta \left( t' \right) \hat{a}^{\dagger}\left( t' \right) +\zeta ^*\left( t' \right) \hat{a}\left( t' \right) \right)}} \right] |0\rangle \\
    =&\sum_{n=0}{\frac{\left( -i \right) ^{2n}}{\left( 2n \right) !}\left( 2i \right) ^n\left[ \int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}} \right] ^n\times \left( 2n-1 \right) !!}\\
    =&\sum_{n=0}{\left( -i \right) ^n\frac{2^n\left( 2n-1 \right) !!}{\left( 2n \right) !}\left[ \int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}} \right] ^n}\\
    =&\exp \left( -i\int_0^t{dt_1\int_0^t{dt_2\zeta ^*\left( t_1 \right) \mathscr{G} \left( t_1-t_2 \right) \zeta \left( t_2 \right)}} \right)
\end{align*}
$$

where we have used

$$ \frac{2^n\left( 2n-1 \right) !!}{\left( 2n \right) !}=\frac{1}{n!}$$

Finally, we've established this honestly! (Again, see Coleman 5.1.1 if you want an alternative discussion)

Notes:

1. (For the QFT gurus in the audience) You may think that our approach to Wick's theorem is unnecessarily complicated: isn't it just taking functional derivative on the free-field S-matrix? You are right, but note that our "operator" form (as an identity) is actually a bit stronger than a relation between correlation and Green's function.
2. Our calculation above actually works more generally: we simply define

    $$ G\left( x,x';t,t' \right) =\langle \Omega |\mathcal{T} \left[ \hat{\phi}_x\left( t \right) \hat{\phi}_{x'}\left( t' \right) \right] |\Omega \rangle$$

    where $\hat{\phi}_x\left( t \right) ,\hat{\phi}_{x'}\left( t' \right)$ are the "field operators" creating or annihilating particles at different points in space-time, and denotes the many-body ground state which, generally speaking, is not Gaussian = free (why should it be?). We call this the "one-particle" Green's function.

The goal of a perturbation theory is to derive an expansion of the actual quantities in terms of those for an unperturbed problem. A useful unperturbed problem is one for which the same set of quantities could be computed. (Always attack a hard problem starting from an easier starting point, and work your way there!) In our context, we take the Gaussian theory as the starting point, and the perturbative expansions are then organized and computed in terms of "Feynman diagrams".
