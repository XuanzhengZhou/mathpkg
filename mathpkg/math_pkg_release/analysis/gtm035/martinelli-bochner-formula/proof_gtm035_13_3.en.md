---
role: proof
locale: en
of_concept: martinelli-bochner-formula
source_book: gtm035
source_chapter: "Chapter 13"
source_section: "13.3"
---
# Proof of Theorem 13.3 (Martinelli-Bochner Formula)

Let $D$ be a smoothly bounded domain in $\mathbb{C}^n$, $n > 1$, and let $K_{MB}$ be the Bochner-Martinelli kernel

$$K_{MB}(\zeta, z) = \sum_{j=1}^{n} \frac{\bar{\zeta}_j - \bar{z}_j}{|\zeta - z|^{2n}} \; d\bar{\zeta}_1 \wedge d\zeta_1 \wedge \cdots \wedge \widehat{d\bar{\zeta}_j} \wedge d\zeta_j \wedge \cdots \wedge d\bar{\zeta}_n \wedge d\zeta_n.$$

**Theorem 13.3 (Bochner-Martinelli Formula).** For each $f \in A(D) \cap \mathcal{C}^1(\bar{D})$ and $z \in D$,

$$f(z) = \frac{(n-1)!}{(2\pi i)^n} \int_{\partial D} f(\zeta) K_{MB}(\zeta, z).$$

**Proof.** By Lemma 13.2, the kernel $K_{MB}$ satisfies conditions (4), (5), and (6) on every smoothly bounded domain $D \subseteq \mathbb{C}^n$, with constant

$$c_0 = \frac{(2\pi i)^n}{(n-1)!}$$

in condition (5).

Now apply Theorem 13.1 with $K = K_{MB}$ and this value of $c_0$. Theorem 13.1 asserts that for any kernel $K$ satisfying (4), (5), (6), and for any $f \in A(D) \cap \mathcal{C}^1(\bar{D})$,

$$c_0 f(z) = \int_{\partial D} f(\zeta) K(\zeta, z), \quad z \in D.$$

Substituting $K_{MB}$ for $K$ and $c_0 = (2\pi i)^n/(n-1)!$ yields

$$\frac{(2\pi i)^n}{(n-1)!} f(z) = \int_{\partial D} f(\zeta) K_{MB}(\zeta, z).$$

Dividing both sides by $c_0$ gives the desired formula:

$$f(z) = \frac{(n-1)!}{(2\pi i)^n} \int_{\partial D} f(\zeta) K_{MB}(\zeta, z).$$

$\square$

**Remark.** This formula generalizes the classical Cauchy integral formula

$$f(z) = \frac{1}{2\pi i} \int_{\partial D} \frac{f(\zeta)}{\zeta - z} d\zeta$$

from $n = 1$ to arbitrary dimension $n > 1$. The theorem was discovered independently by E. Martinelli and S. Bochner in the 1940s.
