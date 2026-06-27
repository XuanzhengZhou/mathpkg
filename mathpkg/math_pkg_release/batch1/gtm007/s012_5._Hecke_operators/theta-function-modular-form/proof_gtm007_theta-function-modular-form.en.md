---
role: proof
locale: en
of_concept: theta-function-modular-form
source_book: gtm007
source_chapter: "VII"
source_section: "6.4"
---
(a) The fact that $n$ is divisible by $8$ was already proved in Chapter V, \S 2.1, Corollary 2 to Theorem 2. The argument uses that for a self-dual even lattice (conditions (i) and (ii)), the associated quadratic module belongs to the category $S_n$, and the signature modulo $8$ is an invariant forcing $n \equiv 0 \pmod{8}$.

(b) We prove the modular transformation property. From Proposition 16, with $v = 1$ and $\Gamma = \Gamma'$ (conditions (i)-(ii)), we have $\Theta_\Gamma(t) = t^{-n/2} \Theta_\Gamma(t^{-1})$. Now,
$$\theta_\Gamma(it) = \sum_{x \in \Gamma} e^{-\pi t (x \cdot x)} = \Theta_\Gamma(t),$$
and similarly $\theta_\Gamma(-1/it) = \theta_\Gamma(i/t) = \Theta_\Gamma(t^{-1})$. Thus $\theta_\Gamma(-1/(it)) = t^{n/2} \theta_\Gamma(it)$. Since both sides are analytic in $z$, the identity extends to
$$\theta_\Gamma(-1/z) = (z/i)^{n/2} \theta_\Gamma(z).$$
Since $n$ is divisible by $8$, we have $(z/i)^{n/2} = z^{n/2}$, giving $\theta_\Gamma(-1/z) = z^{n/2} \theta_\Gamma(z)$. Together with the trivial periodicity $\theta_\Gamma(z+1) = \theta_\Gamma(z)$ (which follows from $(x,x)$ being even, so $e^{\pi i (z+1)(x,x)} = e^{\pi i z(x,x)}$), this shows $\theta_\Gamma$ is a modular form of weight $n/2$.
