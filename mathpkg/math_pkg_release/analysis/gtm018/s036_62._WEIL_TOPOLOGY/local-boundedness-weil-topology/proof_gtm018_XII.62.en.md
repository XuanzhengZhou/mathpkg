---
role: proof
locale: en
of_concept: local-boundedness-weil-topology
source_book: gtm018
source_chapter: "XII"
source_section: "62"
---

Let $N_0$ be an arbitrary set of finite measure in $N$ (such a set exists by Theorem C), and let $M_0$ be a set in $N$ such that $M_0 M_0^{-1} \subset N_0$ (which exists by Theorem A and Theorem B). We shall prove that $M_0$ is bounded.

Indeed, for any $x \in M_0$, we have $x \in M_0 \subset N_0$, so $M_0 \subset N_0$. Since $N_0$ has finite measure, $M_0$ has finite measure. Moreover, $M_0$ being bounded is a consequence of Theorem C and the fact that, by definition, a bounded set may be covered by a finite number of left translations of any set in $N$.

For the remaining assertions: if a measurable set $E$ has a nonempty interior, then $E$ contains a translate of some $N \in N$. Since $\mu(N) > 0$ by Theorem C, we have $\mu(E) > 0$. Conversely, if a measurable set $E$ is bounded, then it can be covered by finitely many translates of any fixed $N \in N$ of finite measure, whence $\mu(E) < \infty$.
