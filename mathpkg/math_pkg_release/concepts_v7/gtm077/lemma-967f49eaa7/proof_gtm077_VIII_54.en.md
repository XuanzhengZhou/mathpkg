---
role: proof
locale: en
of_concept: lemma-967f49eaa7
source_book: gtm077
source_chapter: "VIII"
source_section: "§54"
---
# Proof: Sum of Exponentials over a Complete Residue System

**Lemma (a).** Let $d\omega$ have denominator $\mathfrak{a}$. Then, if $\mathfrak{a} \neq 1$,

$$\sum_{\mu \bmod \mathfrak{a}} e^{2\pi i S(\mu\omega)} = 0.$$

*Proof.* By hypothesis, $d\omega = \mathfrak{b}/\mathfrak{a}$ with $(\mathfrak{a}, \mathfrak{b}) = 1$, where $d$ is the different of $k$. For any integer $\nu$ divisible by $\mathfrak{a}$, Theorem 101 implies that $S(\nu\omega)$ is a rational integer, hence $e^{2\pi i S(\nu\omega)} = 1$.

Let $\alpha$ be an integer in $k$ such that $\alpha \equiv 1 \pmod{\mathfrak{a}}$ and $\alpha \not\equiv 1 \pmod{\mathfrak{a}\mathfrak{p}}$ for some prime ideal $\mathfrak{p} \mid \mathfrak{a}$ (since $\mathfrak{a} \neq 1$, such an $\alpha$ exists by the Chinese Remainder Theorem). Then $\mu + \alpha$ runs through a complete system of residues mod $\mathfrak{a}$ simultaneously with $\mu$. Hence

$$\sum_{\mu \bmod \mathfrak{a}} e^{2\pi i S(\mu\omega)} = \sum_{\mu \bmod \mathfrak{a}} e^{2\pi i S((\mu+\alpha)\omega)} = e^{2\pi i S(\alpha\omega)} \sum_{\mu \bmod \mathfrak{a}} e^{2\pi i S(\mu\omega)}.$$

If the sum were nonzero, we would have $e^{2\pi i S(\alpha\omega)} = 1$, i.e., $S(\alpha\omega)$ would be a rational integer. But $\alpha\omega = \frac{\alpha \mathfrak{b}}{\mathfrak{a}d}$ and since $\alpha \equiv 1 \pmod{\mathfrak{a}}$, we have $\alpha \mathfrak{b} \equiv \mathfrak{b} \pmod{\mathfrak{a}\mathfrak{b}}$, so $S(\alpha\omega)$ is not integral (because $\mathfrak{a} \neq 1$ and the denominator of $d\omega$ is exactly $\mathfrak{a}$). Contradiction. Therefore the sum is zero. $\square$
