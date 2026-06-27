---
role: proof
locale: en
of_concept: limit-of-indefinite-integrals
source_book: gtm018
source_chapter: "V"
source_section: "24"
---
**Proof.** Since $|\nu_n(E) - \nu_m(E)| \leq \int |f_n - f_m| d\mu \to 0$, the limit exists uniformly in $E$ and is finite and finitely additive. For a disjoint sequence $\{E_n\}$ with union $E$,
$$|\nu(E) - \sum_{i=1}^{k} \nu(E_i)| \leq |\nu(E) - \nu_n(E)| + |\nu_n(E) - \sum_{i=1}^{k} \nu_n(E_i)| + |\sum_{i=1}^{k} (\nu_n(E_i) - \nu(E_i))|.$$
The first and third terms become small by choosing $n$ large (uniform convergence). For fixed $n$, the middle term becomes small by taking $k$ large (countable additivity of $\nu_n$, Theorem I). Thus $\nu(E) = \sum_{i=1}^{\infty} \nu(E_i)$."
