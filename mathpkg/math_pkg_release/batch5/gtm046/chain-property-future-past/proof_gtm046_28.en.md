---
role: proof
locale: en
of_concept: chain-property-future-past
source_book: gtm046
source_chapter: "VIII"
source_section: "28.3"
---
Let $k_1 < \cdots < k_n < k_{n+1} < \cdots < k_{n+m}$ be arbitrary integers. Apply the operation $E^{\mathfrak{B}_{k_1} \cdots \mathfrak{B}_{k_n}}$ to both sides of the defining chain relation (with $n$ replaced by $k_n$ and $n+m$ by $k_{n+m}$). Using property 24.2 (iterated conditioning) and replacing by $\Omega$ all events whose subscripts differ from $k_{n+1}, \cdots, k_{n+m}$, we obtain
$$P^{\mathfrak{B}_{k_1} \cdots \mathfrak{B}_{k_n}} B_{k_{n+1}} \cdots B_{k_{n+m}} = P^{\mathfrak{B}_{k_n}} B_{k_{n+1}} \cdots B_{k_{n+m}} \text{ a.s.}$$
This shows that, whatever the "future" events, their conditional probability depends almost surely only upon the last given "past" $\mathfrak{B}_{k_n}$, not on the entire past $\mathfrak{B}_{k_1} \cdots \mathfrak{B}_{k_n}$.
