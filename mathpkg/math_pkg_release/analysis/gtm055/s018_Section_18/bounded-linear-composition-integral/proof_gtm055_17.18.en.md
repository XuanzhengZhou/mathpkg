---
role: proof
locale: en
of_concept: bounded-linear-composition-integral
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

The composition $(T \circ \Phi)(x) = T\Phi(x)$ is measurable along with $\Phi$, and since $\| T\Phi(x) \| \leq \| T \| \| \Phi(x) \|$, $x \in X$, it follows that $T \circ \Phi$ belongs to $\mathcal{L}_1(X; \mathcal{F})$ whenever $\Phi$ belongs to $\mathcal{L}_1(X; \mathcal{E})$.

A direct calculation shows that if $\Sigma$ is a simple $\mathcal{E}$-valued mapping on $X$, say $\Sigma = \sum_{i=1}^{N} \chi_{E_i} v_i$, then $T \circ \Sigma$ is the simple $\mathcal{F}$-valued mapping $\sum_{i=1}^{N} \chi_{E_i} T v_i$. Hence if $\Sigma$ is integrable and $\mu(E_i) < +\infty$, $i = 1, \ldots, N$, then

$$\int_X (T \circ \Sigma) d\mu = \sum_{i=1}^{N} \mu(E_i) T v_i = T \left( \sum_{i=1}^{N} \mu(E_i) v_i \right) = T \left( \int_X \Sigma d\mu \right),$$

so the proposition is valid for integrable simple $\mathcal{E}$-valued mappings.

Finally, suppose $\Phi$ is an arbitrary element of $\mathcal{L}_1(X; \mathcal{E})$, and let $\{\Sigma_n\}$ be a sequence of integrable simple mappings converging to $\Phi$ as in Lemma 17.12. Then $\{\Sigma_n\}$ tends to $\Phi$ in $\mathcal{L}_1(X; \mathcal{E})$ by the dominated convergence theorem, and since $\|\int_X \Phi d\mu - \int_X \Sigma_n d\mu\| = \|\int_X (\Phi - \Sigma_n) d\mu\| \leq \|\Phi - \Sigma_n\|_1$, the result follows by continuity.
