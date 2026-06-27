---
role: proof
locale: en
of_concept: locally-finite-measure-characterization
source_book: gtm055
source_chapter: "8"
source_section: "9"
---

If $\mu(A) = +\infty$ and $A$ is an atom, then every measurable $F \subset A$ with $\mu(F) < +\infty$ must satisfy $\mu(F) = 0$, so $\mu$ is not locally finite. Conversely, suppose $\mu$ fails to be locally finite. Then there exists a measurable set $E_0$ with $\mu(E_0) = +\infty$ and
$$M = \sup \{ \mu(F) : F \in \mathbf{S}, F \subset E_0, \mu(F) < +\infty \} < +\infty.$$
Let $\{F_n\}$ be a sequence of measurable subsets of $E_0$ of finite measure with $\mu(F_n) \to M$, and set $E_n = F_1 \cup \cdots \cup F_n$. Then $\mu(E_n) < +\infty$ and $\mu(E_n) \to M$. Let $F_0 = \bigcup_n F_n = \bigcup_n E_n$, so $\mu(F_0) = M$. Set $A = E_0 \setminus F_0$. For any measurable $F \subset A$ with $\mu(F) < +\infty$, we have $\mu(F_0 \cup F) = M + \mu(F) \leq M$, forcing $\mu(F) = 0$. Thus $A$ has infinite measure and every measurable subset has measure $0$ or $+\infty$, making $A$ an infinite atom.
