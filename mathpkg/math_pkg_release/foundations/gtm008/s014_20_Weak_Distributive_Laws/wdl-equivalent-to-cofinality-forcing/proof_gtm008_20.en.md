---
role: proof
locale: en
of_concept: wdl-equivalent-to-cofinality-forcing
source_book: gtm008
source_chapter: "20"
source_section: "20. Weak Distributive Laws"
---

**Forward direction.** Assume $B$ satisfies the $(\omega, \omega_\alpha)$-WDL. Let $f \in V^{(B)}$ be such that $\llbracket f: \check{\omega} \to (\omega_\alpha)^\vee \rrbracket = 1$. For each $n \in \omega$ and $\xi < \omega_\alpha$, define
$$
b_{n\xi} = \llbracket f(\check{n}) = \check{\xi} \rrbracket,
$$
which is formally understood as
$$
\llbracket (\forall z) [\langle \check{n}, z \rangle \in f \leftrightarrow z = \check{\xi}] \rrbracket.
$$

Since $f$ is forced to be a function from $\check{\omega}$ into $(\omega_\alpha)^\vee$, we have
$$
\prod_{n < \omega} \sum_{\xi < \omega_\alpha} b_{n\xi} = \llbracket (\forall n < \check{\omega}) (\exists \xi < (\omega_\alpha)^\vee) [f(\check{n}) = \check{\xi}] \rrbracket = 1.
$$

By the $(\omega, \omega_\alpha)$-WDL and the Remark after Definition 20.1 (which applies since $\operatorname{cf}(\omega_\alpha) > \omega$ by the definition of the $(\omega, \omega_\alpha)$-WDL),
$$
1 = \prod_{n < \omega} \sum_{\xi < \omega_\alpha} b_{n\xi}
= \sum_{\eta < \omega_\alpha} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}
= \llbracket (\exists \eta < (\omega_\alpha)^\vee) (\forall n < \check{\omega}) [f(\check{n}) \leq \check{\eta}] \rrbracket.
$$

Since $f$ was arbitrary, this shows
$$
\llbracket \operatorname{cf}((\omega_\alpha)^\vee) > \check{\omega} \rrbracket
= \llbracket (\forall f) [\text{if } f: \check{\omega} \to (\omega_\alpha)^\vee \text{ then } (\exists \eta < (\omega_\alpha)^\vee) (\forall n < \check{\omega}) [f(n) \leq \eta]] \rrbracket
= 1.
$$

**Converse direction.** Assume $\llbracket \operatorname{cf}((\omega_\alpha)^\vee) > \check{\omega} \rrbracket = 1$. Let $\{b_{n\xi} \mid n \in \omega \land \xi < \omega_\alpha\} \subseteq B$. Define $f \in V^{(B)}$ by
$$
\mathcal{D}(f) = \{\langle \check{n}, \check{\xi} \rangle^{(B)} \mid n \in \omega \land \xi < \omega_\alpha\},
$$
and for all $n \in \omega$, $\xi < \omega_\alpha$,
$$
f(\langle \check{n}, \check{\xi} \rangle^{(B)}) = b_{n\xi},
$$
with $f(x) = 0$ for all other $x \in \mathcal{D}(f)$.

Then for each $n \in \omega$, the family $\{b_{n\xi} \mid \xi < \omega_\alpha\}$ forms a partition of the value of $f(\check{n})$ in the Boolean-valued model, so
$$
\llbracket f: \check{\omega} \to (\omega_\alpha)^\vee \rrbracket = \prod_{n < \omega} \sum_{\xi < \omega_\alpha} b_{n\xi}.
$$

By the assumption on cofinality,
$$
\llbracket (\exists \eta < (\omega_\alpha)^\vee) (\forall n < \check{\omega}) [f(n) \leq \eta] \rrbracket = 1.
$$

Computing this Boolean value yields
$$
\sum_{\eta < \omega_\alpha} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi} = 1.
$$

But $\prod_{n < \omega} \sum_{\xi < \omega_\alpha} b_{n\xi} = \llbracket f: \check{\omega} \to (\omega_\alpha)^\vee \rrbracket \geq 1$, so both sides equal $1$ and
$$
\prod_{n < \omega} \sum_{\xi < \omega_\alpha} b_{n\xi}
= \sum_{\eta < \omega_\alpha} \prod_{n < \omega} \sum_{\xi \leq \eta} b_{n\xi}.
$$

By the Remark after Definition 20.1, the right-hand side equals
$$
\sum_{f \in \omega_\alpha^{\omega}} \prod_{n \in \omega} \sum_{\xi \leq f(n)} b_{n\xi},
$$
which establishes the $(\omega, \omega_\alpha)$-WDL.
