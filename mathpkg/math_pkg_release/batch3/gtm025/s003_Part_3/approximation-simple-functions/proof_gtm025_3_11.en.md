---
role: proof
locale: en
of_concept: approximation-simple-functions
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** For $f \geq 0$, partition the range: for $n \in \mathbb{N}$, $1 \leq k \leq n \cdot 2^n$, let
$$A_{n,k} = \left\{x : \frac{k-1}{2^n} \leq f(x) < \frac{k}{2^n}\right\}, \quad B_n = \{x : f(x) \geq n\},$$
$$s_n = \sum_{k=1}^{n \cdot 2^n} \frac{k-1}{2^n} \xi_{A_{n,k}} + n \xi_{B_n}.$$
Then $0 \leq s_1 \leq s_2 \leq \cdots \leq f$, each $s_n$ is simple and measurable, and $s_n \to f$ pointwise. If $f$ is bounded by $M$, for $n > M$ we have $B_n = \emptyset$ and $|f - s_n| \leq 2^{-n}$, so convergence is uniform. For general $f$, apply to positive/negative parts or real/imaginary parts. $\square$
