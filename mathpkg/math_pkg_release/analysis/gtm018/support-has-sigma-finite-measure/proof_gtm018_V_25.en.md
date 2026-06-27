---
role: proof
locale: en
of_concept: support-has-sigma-finite-measure
source_book: gtm018
source_chapter: "V"
source_section: "25"
---
**Proof.** Let $\{f_n\}$ be a mean fundamental sequence of integrable simple functions converging in measure to $f$. Each $N(f_n)$ has finite measure. If $E = N(f) - \bigcup_n N(f_n)$ and $F$ is any measurable subset of $E$, then $\int_F f d\mu = \lim_n \int_F f_n d\mu = 0$, so by Theorem E, $f = 0$ a.e. on $E$. Thus $\mu(E) = 0$, and $N(f) \subset \bigcup_n N(f_n) \cup E$ is contained in a $\sigma$-finite set, hence $\sigma$-finite.
