---
role: proof
locale: en
of_concept: set-t-algebras-isomorphic-to-equational-algebras
source_book: gtm026
source_chapter: "4"
source_section: "4.15"
---

In one direction, given an $(\Omega, E)$-algebra $(X, \delta)$, the structure map of the corresponding $\mathbf{T}$-algebra is defined as $\xi = \delta^{\#}$, where $\delta^{\#}: XT \longrightarrow X$ is the unique $\Omega$-homomorphism extending $\mathrm{id}_X$ via the Principle of Finitary Algebraic General Recursion (1.18). That $\xi$ satisfies the $\mathbf{T}$-algebra axioms follows from the construction of $\mathbf{T}$ in 4.1.

Conversely, given a $\mathbf{T}$-algebra $(X, \xi)$, define an $\Omega$-algebra structure $\delta$ on $X$ by the rule of 4.5: for each $\omega \in \Omega_n$ and $x_1, \ldots, x_n \in X$,

$$
(x_1, \ldots, x_n) \delta_\omega = ([x_1] \cdots [x_n] \omega) \xi,
$$

where $[x_i]$ denotes the word of length $1$ consisting of the symbol $x_i$, and $[x_1] \cdots [x_n] \omega$ is the $\Omega$-word formed by concatenating these symbols followed by the operator $\omega$, considered as an element of $XT$.

We must verify that $\delta$ satisfies the equations $E$ and that the two constructions are mutually inverse.

Let $X\rho: X\Omega \longrightarrow XT$ be the natural inclusion of $\Omega$-words into $T$-words (sending each $\Omega$-word to the corresponding element of the free $T$-algebra). From 4.10 we have the commutative diagram

$$
\begin{CD}
X\Omega @>{X\rho}>> XT \\
@V{\delta^@}VV @VV{\xi}V \\
X @= X
\end{CD}
$$

since $\xi$ is a $T$-homomorphism and therefore its restriction to $\Omega$-words agrees with the $\Omega$-homomorphism $\delta^@$ induced by $\delta$. Equivalently, $X\rho \cdot \xi = \delta^@$.

Now, for any $\omega \in \Omega_n$ and any $p_1, \ldots, p_n \in XT$, let $g = \xi$ in the calculation. The $T$-algebra multiplication $X\mu: XTT \longrightarrow XT$ flattens words of words by deleting parentheses; for example, $([p_1] \cdots [p_n] \omega) X\mu = [p_1 \cdots p_n \omega]$, where the left side is a word of length $1$ in $XTT$ (a single symbol which itself is an $\Omega$-word) and the right side is the concatenated word in $XT$. Using the $T$-algebra axiom $X\mu \cdot \xi = \xi T \cdot \xi$ (from 4.10) together with the explicit description of $\xi T$, one computes for $x_1, \ldots, x_n \in X$:

$$
([x_1] \cdots [x_n] \omega) \xi
= \langle [x_1] \cdots [x_n] \omega,\; \xi \rangle
= \langle [x_1] \cdots [x_n] \omega,\; X\rho \cdot \xi \rangle
= \langle [x_1] \cdots [x_n] \omega,\; \delta^@ \rangle
= ([x_1] \delta^@, \ldots, [x_n] \delta^@) \delta_\omega
= (x_1, \ldots, x_n) \delta_\omega.
$$

But this is precisely the definition of $\delta$ from 4.5, confirming consistency. The equation $X\rho \cdot \xi = \delta^@$ shows both that $\delta$ satisfies the equations $E$ (since $\delta^@$ factors through the $T$-algebra structure, and the algebraic theory $\mathbf{T}$ was constructed to impose exactly the relations $E$) and that $\xi$ is recovered from $\delta$ as $\delta^@$.

The two constructions are therefore mutually inverse. The bijection is natural in $X$: if $h: X \to Y$ is a function, then $h$ is an $(\Omega, E)$-homomorphism if and only if it is a $\mathbf{T}$-homomorphism, because the $\mathbf{T}$-algebra structure map is $\delta^@$ and the naturality of the free-forgetful adjunction ensures compatibility. Thus the passage between $\mathbf{T}$-algebra structures and $(\Omega, E)$-algebra structures defines an isomorphism of categories over $\mathbf{Set}$.
