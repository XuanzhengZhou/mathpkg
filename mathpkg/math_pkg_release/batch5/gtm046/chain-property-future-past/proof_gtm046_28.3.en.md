---
role: proof
locale: en
of_concept: chain-property-future-past
source_book: gtm046
source_chapter: "VIII"
source_section: "28.3"
---

**Proof.** Let the $\mathfrak{B}_n$ form a chain. By definition, for $n < n+1 < \cdots < n+m$,

$$P^{\mathfrak{B}_n}(B_{n+1} \cdots B_{n+m}) = P^{\mathfrak{B}_n}(B_{n+1} \cdots B_{n+m}) \quad \text{a.s.}$$

Let $k_1 < \cdots < k_{n-1} < k_n < k_{n+1} < \cdots < k_{n+m}$ be arbitrary integers. Apply the operation $E^{\mathfrak{B}_{k_1} \vee \cdots \vee \mathfrak{B}_{k_n}}$ to both sides of the chain relation (where $n$ and $n+m$ are replaced by $k_n$ and $k_{n+m}$ respectively). By property 24.2 (smoothing), and upon replacing by $\Omega$ all events whose subscripts differ from $k_{n+1}, \ldots, k_{n+m}$, we obtain

$$P^{\mathfrak{B}_{k_1} \vee \cdots \vee \mathfrak{B}_{k_n}}(B_{k_{n+1}} \cdots B_{k_{n+m}}) = P^{\mathfrak{B}_{k_n}}(B_{k_{n+1}} \cdots B_{k_{n+m}}) \quad \text{a.s.}$$

This shows that, loosely speaking, whatever the "future," it depends a.s. only upon the last given "past." The condition encodes the Markov property: the future is conditionally independent of the past given the present.
