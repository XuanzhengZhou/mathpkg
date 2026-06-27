---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Given a monoidal functor $(F, F_2, F_0)$, the structure maps $F_2$ and $F_0$ can be extended by induction on the length of tensor words to obtain a natural transformation $F_v$ for each word $v$. The base cases are $F_\square = F_2$ and $F_e = F_0$, and the inductive step is $F_{v \square v'} = F_2 \circ (F_v \square F_{v'})$. This extension is the monoidal analogue of the fact that a functor preserving binary products preserves all finite products.
