---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Corollary 5.12 establishes a universal partial recursive function $g(e,x)$ of two variables that enumerates all unary partial recursive functions: for any such $f$, there exists an index $e$ with $g(e,x) \simeq f(x)$. Despite the apparent threat of a diagonal argument (defining $f(x) \simeq g(x,x)+1$), no contradiction arises because $g$ is partial -- the diagonal yields $g(e,e)$ undefined, which is consistent.
