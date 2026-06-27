---
role: proof
locale: en
of_concept: marcinkiewiczs-theorem
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Marcinkiewicz's Theorem

**Marcinkiewicz's Theorem.** If a characteristic function has the form $\exp \mathcal{P}(t)$, where $\mathcal{P}(t)$ is a polynomial, then this polynomial is of degree at most two.

*The proof is not included in the source text. The reader is referred to [65], 7.3.*

**Consequences:**

1. The function $e^{-t^4}$ is **not** a characteristic function (since $-t^4$ is a polynomial of degree 4).

2. The Gaussian distribution is the only distribution with the property that all its semi-invariants $s_n$ are zero from a certain index onward. Indeed, if $s_n = 0$ for all $n \geq N$, then $\log \varphi(t) = \sum_{k=1}^{N-1} s_k (it)^k/k!$ is a polynomial, so by Marcinkiewicz's theorem it must be of degree at most 2, hence $s_k = 0$ for $k \geq 3$.

3. In particular, if a characteristic function $\varphi(t)$ is of the form $\exp \mathcal{P}(t)$ with $\mathcal{P}$ a polynomial, then necessarily $\varphi(t) = \exp(itm - \sigma^2 t^2/2)$, i.e., it is the characteristic function of a normal distribution (possibly degenerate).
