---
role: proof
locale: en
of_concept: sesquilinear-form-linear-mapping
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

For each fixed $a \in W$, the map $b \mapsto \tau(a, b)$ is a linear functional on $W$ (since $\tau$ is sesquilinear: linear in the second argument). Because $\sigma$ is nondegenerate and $W$ is finite dimensional, every linear functional on $W$ is representable via $\sigma$: there exists a unique vector, which we denote $af$, such that

$$
\sigma(af, b) = \tau(a, b) \quad \text{for all } b \in W.
$$

This defines a mapping $f \colon W \to W$ by $a \mapsto af$. To verify linearity, let $a_1, a_2 \in W$ and $c \in \mathbb{C}$. For all $b \in W$,

$$
\begin{aligned}
\sigma((a_1 + a_2)f, b) &= \tau(a_1 + a_2, b) = \tau(a_1, b) + \tau(a_2, b) \\
&= \sigma(a_1 f, b) + \sigma(a_2 f, b) = \sigma(a_1 f + a_2 f, b).
\end{aligned}
$$

By nondegeneracy of $\sigma$, $(a_1 + a_2)f = a_1 f + a_2 f$. Similarly, using conjugate-linearity of $\tau$ in the first argument,

$$
\sigma((c a)f, b) = \tau(c a, b) = \bar{c}\,\tau(a, b) = \bar{c}\,\sigma(af, b) = \sigma(c(af), b),
$$

so $(c a)f = c (a f)$. Thus $f$ is linear. (This is left as Exercise 3 in the source text.)
