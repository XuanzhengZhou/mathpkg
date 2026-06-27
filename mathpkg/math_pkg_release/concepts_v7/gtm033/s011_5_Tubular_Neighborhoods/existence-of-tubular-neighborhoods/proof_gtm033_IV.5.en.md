---
role: proof
locale: en
of_concept: existence-of-tubular-neighborhoods
source_book: gtm033
source_chapter: "IV"
source_section: "5"
---

# Proof of Existence of Tubular Neighborhoods (Theorem 5.2)

**Theorem (5.2).** Let $M \subset V$ be a submanifold, $\partial M = \partial V = \varnothing$. Then $M$ has a tubular neighborhood in $V$.

*Proof.* We may assume $V \subset \mathbb{R}^n$. Let $W \subset \mathbb{R}^n$ be a neighborhood of $V$ and $r: W \rightarrow V$ a $C^\infty$ retraction. (Such a $W$ and $r$ exist because $V$ has a tubular neighborhood in $\mathbb{R}^n$, which provides a smooth retraction onto $V$.)

Let $\nu$ be the normal bundle of $M$ in $\mathbb{R}^n$ (obtained by pulling back the canonical $k$-plane bundle over the Grassmannian). Thus $\nu$ is a vector bundle over $M$, and

$$E(\nu) = \{(x, y) \in M \times \mathbb{R}^n : y \in \nu_x\}.$$

For each $x \in M$ let

$$U_x = \{(x, y) \in \nu_x : x + y \in W\}.$$

Put $U = \bigcup_{x \in M} U_x$. Then $U$ is open in $E(\nu)$, being the inverse image of $W$ under the map

$$E(\nu) \rightarrow \mathbb{R}^n,$$
$$(x, y) \mapsto x + y \quad (y \in \nu_x).$$

It is easy to verify that the map

$$f: U \rightarrow V,$$
$$f(x, y) = r(x + y)$$

provides a partial tubular neighborhood for $(V, M)$.

To obtain a full tubular neighborhood, observe that since $f$ is an immersion on the zero section and $f|M = 1_M$, there exists an open neighborhood $U_0 \subset U$ of the zero section such that $f|_{U_0}$ is an embedding (by Exercise 7, Section 2.1). Then $(f|_{U_0}, \nu|_{U_0})$ is a tubular neighborhood of $M$ in $V$. ∎
