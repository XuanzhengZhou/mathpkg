---
role: proof
locale: en
of_concept: divisibility-by-primitive-polynomial
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** We have $b f(x) = g(x) h(x)$ for some $h(x) \in R[x]$. By Gauss's Lemma (Lemma 1),

$$b \cdot c(f) = c(g) \cdot c(h) = c(h),$$

where the last equality holds because $g$ is primitive, so $c(g)$ is a unit in $R$ (and contents are defined up to unit factors). Thus $b$ divides $c(h)$ in $R$, and consequently $b$ divides every coefficient of $h(x)$ — that is, $h(x) = b \cdot k(x)$ for some $k(x) \in R[x]$. Then $b f(x) = g(x) \cdot b k(x)$, and canceling $b$ (in the integral domain of coefficients) yields $f(x) = g(x) k(x)$, so $g(x)$ divides $f(x)$.
