---
role: proof
locale: en
of_concept: omega-omega-wdl-equivalent-to-dominating-reals
source_book: gtm008
source_chapter: "20"
source_section: "20. Weak Distributive Laws"
---

**Forward direction.** Assume $B$ satisfies the $(\omega, \omega)$-WDL. Let $g \in V^{(B)}$ be such that $\llbracket g: \check{\omega} \to \check{\omega} \rrbracket = 1$. For each $n, m \in \omega$, define
$$
b_{nm} = \llbracket g(\check{n}) = \check{m} \rrbracket.
$$

Since $g$ is forced to be a function from $\check{\omega}$ into $\check{\omega}$, we have
$$
b = \prod_{n < \omega} \sum_{m < \omega} b_{nm} = \llbracket (\forall n < \check{\omega}) (\exists m < \check{\omega}) [g(\check{n}) = \check{m}] \rrbracket = 1.
$$

By the $(\omega, \omega)$-WDL,
$$
1 = \prod_{n < \omega} \sum_{m < \omega} b_{nm}
= \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}
= \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \llbracket g(\check{n}) \leq \check{f}(\check{n}) \rrbracket
= \llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket.
$$

Since $g$ was arbitrary, this proves
$$
\llbracket (\forall g \in (\omega^{\omega})^{\vee}) (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket = 1,
$$
where the outer universal quantifier ranges over all functions $g: \check{\omega} \to \check{\omega}$ in $V^{(B)}$, while the existential quantifier ranges over the canonical check names of ground model functions in $\omega^\omega$.

**Converse direction.** Assume
$$
\llbracket (\forall g) [g: \check{\omega} \to \check{\omega} \to (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)]] \rrbracket = 1.
$$
Let $\{b_{nm} \mid n, m \in \omega\} \subseteq B$. Define $g \in V^{(B)}$ by
$$
\mathcal{D}(g) = \{\langle \check{n}, \check{m} \rangle^{(B)} \mid n, m \in \omega\},
$$
and for all $n, m \in \omega$,
$$
g(\langle \check{n}, \check{m} \rangle^{(B)}) = b_{nm},
$$
with $g(x) = 0$ for all other $x \in \mathcal{D}(g)$.

Then $\llbracket g: \check{\omega} \to \check{\omega} \rrbracket = \prod_{n < \omega} \sum_{m < \omega} b_{nm}$.
By the assumption on dominating functions,
$$
\llbracket (\exists f \in (\omega^{\omega})^{\vee}) (\forall n < \check{\omega}) [g(n) \leq f(n)] \rrbracket = 1.
$$

Expanding this Boolean value gives
$$
\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = 1.
$$

Since $\prod_{n < \omega} \sum_{m < \omega} b_{nm} = \llbracket g: \check{\omega} \to \check{\omega} \rrbracket$ and each $b_{nm} \in B$, we have
$$
\prod_{n < \omega} \sum_{m < \omega} b_{nm}
= \sum_{f \in \omega^{\omega}} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm},
$$
which is precisely the $(\omega, \omega)$-WDL.
