---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Lemma 7.6 provides the key construction for Kalmar's undecidability theorem (Theorem 7.5). It shows how to encode a 4-ary relation $\rho$ on a set $S$ using only a binary relation $r$ on a larger set $S' = \{K\} \cup S^2 \cup S^4$. The diagonal embedding $\Delta: S \to S'$ maps $x$ to $(x,x)$, and the binary relation $r$ is defined so that membership in $\rho(x,y,z,t)$ can be recovered from $r$ restricted to the image of $\Delta$. This reduction technique demonstrates that the expressive power of a single binary predicate is sufficient to simulate predicates of higher arity.
