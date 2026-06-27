---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition introduces the arrow notation $M \rightarrow N$ for sequential composition of Turing machines. The halting rows of $M$ are redirected to the initial state of $N$, so that when $M$ would normally halt, control passes to $N$. The notation extends naturally to three machines as $M \rightarrow N \rightarrow P$, and can be combined into large flow charts. Crucially, state sets can be renamed via one-one mappings, so the disjointness requirement is not a real restriction. This notation provides a modular way to build complex Turing machines from simpler ones.
