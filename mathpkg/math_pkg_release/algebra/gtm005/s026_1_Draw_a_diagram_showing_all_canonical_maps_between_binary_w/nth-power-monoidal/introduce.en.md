---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

In a monoidal category $B$, the $n$-th power $b^n$ of an object $b$ is defined by iterating the monoidal product with a fixed parenthesization (all parentheses in front). For a monoid object $\langle c, \mu, \eta \rangle$ in $B$, the $n$-fold product $\mu^{(n)}: c^n \to c$ generalizes the binary multiplication $\mu$ to $n$ factors via a recursive definition: $\mu^{(0)} = \eta$ (the unit), $\mu^{(1)} = \mathrm{id}_c$, and $\mu^{(n+1)} = \mu(\mu^{(n)} \square 1)$. This construction enables the formulation of the general associative law for monoids.
