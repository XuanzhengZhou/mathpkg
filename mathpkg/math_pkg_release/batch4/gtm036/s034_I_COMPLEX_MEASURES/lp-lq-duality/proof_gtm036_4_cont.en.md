---
role: proof
locale: en
of_concept: lp-lq-duality
source_book: gtm036
source_chapter: "4"
source_section: "Problem section (L^p duality)"
---
When $(X, \mathcal{S}, \mu)$ is totally finite, the assertion is clear. For each $f \in L^\infty$ it is obvious that the linear functional $\phi(f) = \int f g d\mu$ is continuous on $L^p$ with $\|\phi\| \leq \|g\|_q$. Conversely, if $\phi$ is a given continuous linear functional on $L^p$, let $\nu(A) = \phi(\chi_A)$ for $A \in \mathcal{S}$. Then $\nu$ is a signed (or complex) measure, absolutely continuous with respect to $\mu$. By the Radon-Nikodym theorem, there exists $g \in L^1$ with $\nu(A) = \int_A g d\mu$.

Taking a sequence of bounded non-negative $\mu$-measurable functions increasing to $|g|$,
$$\|g_n\|_q^q \leq \int g_n^{q-1} |g| d\mu = \phi(g_n^{q-1} \overline{\operatorname{sgn}} g) \leq \|\phi\| \|g_n\|_q^{q/p},$$
and so
$$\|g\|_q = \sup \{\|g_n\|_q : n = 1, 2, \cdots\} \leq \|\phi\|.$$

In the general case when $(X, \mathcal{S}, \mu)$ is not totally finite, there is, for each $A \in \mathcal{S}_0$, a function $g_A \in L^q$ vanishing off $A$ with $\phi(f \chi_A) = \int f g_A d\mu$. If $k = \sup \{\|g_A\|_q : A \in \mathcal{S}_0\}$, then $k \leq \|\phi\|$ and, for any increasing sequence $\{A_n\}$ of sets of $\mathcal{S}_0$ for which $\|g_{A_n}\|_q \to k$, $\{g_{A_n}\}$ converges in $L^q$. The limit $g$ is independent of the particular sequence chosen and is the required function.
