---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma shows that the class $A$ (in the context of characterizing recursive functions) is closed under the primitive recursion schema. Using the $\beta$-function encoding of finite sequences, the function $g$ defined by $g(x_0,\ldots,x_{m-1},0) = f(x_0,\ldots,x_{m-1})$ and $g(x_0,\ldots,x_{m-1},y+1) = h(x_0,\ldots,x_{m-1},y,g(x_0,\ldots,x_{m-1},y))$ can be recovered by searching for a sequence number $z$ encoding the entire computation history. The proof uses the unbounded search operator and the closure properties already established.
