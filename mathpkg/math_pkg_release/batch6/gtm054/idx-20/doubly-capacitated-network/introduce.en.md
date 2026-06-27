---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A doubly-capacitated network generalizes the standard integral network by assigning both a lower capacity $k_1(e)$ and an upper capacity $k_2(e)$ to each edge $e$, with the constraint that $k_1(e) \leq k_2(e)$. This models pipeline systems where each link must carry a minimum flow to prevent deterioration, in addition to respecting a maximum capacity. The standard integral network $(V, k)$ from Section C corresponds to the special case $(V, 0, k)$ where the lower capacity is identically zero.
