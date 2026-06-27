---
role: proof
locale: en
of_concept: cone-natural-transformation-bijection
source_book: gtm005
source_chapter: "X"
source_section: "5. Pointwise Kan Extensions"
---

**Proof.** A cone $\tau: a \to TQ$ assigns to each object $\langle f, m \rangle$ of the comma category $(c \downarrow K)$ (so $f: c \to Km$) an arrow $\tau(f, m): a \to Tm$ subject to the cone condition: for each arrow $h: m \to m'$ in $M$,
$$\tau(Kh \circ f, m') = Th \circ \tau(f, m).$$

A natural transformation $\beta: C(c, K-) \to A(a, T-)$ assigns to each $m \in M$ a function $\beta_m: C(c, Km) \to A(a, Tm)$, natural in $m$, so that for each $h: m' \to m$,
$$\beta_{m'}(Kh \circ f) = Th \circ \beta_m(f)$$
for every $f: c \to Km$. (Note the variance: $C(c, K-): M \to \mathbf{Set}$ is covariant, while naturality for $\beta$ follows the usual pattern.)

Given $\tau$, define $\beta_m(f) = \tau(f, m)$. Given $\beta$, define $\tau(f, m) = \beta_m(f)$. The cone condition for $\tau$ translates exactly to the naturality condition for $\beta$, and vice versa. This establishes the bijection, which is evidently natural in $a$ and $c$.
