---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The derangement recurrence $D_n = (n-1)(D_{n-1} + D_{n-2})$ admits a simple combinatorial proof: consider where element 1 goes, and where the displaced element goes in turn. This recurrence can also be solved using exponential generating functions, yielding $E(x) = e^{-x}/(1-x)$, from which the explicit formula $D_n = n! \sum_{k=0}^n (-1)^k/k!$ follows by series expansion — though the inclusion-exclusion method gives the same result more directly.
