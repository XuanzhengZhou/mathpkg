---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition lists the formal axioms of Zermelo-Fraenkel set theory expressed in the first-order language $\mathrm{L}_1\mathrm{Set}$, and asserts that they are true in the standard interpretation given by the von Neumann universe $V$. The axioms include the empty set, extensionality, pairing, union, power set, and regularity (foundation).

Each axiom is verified by reasoning about the cumulative hierarchy $V = \bigcup_\alpha V_\alpha$. For example, the pairing axiom holds because if $U, W \in V_\alpha$, then $\{U, W\} \in \mathcal{P}(V_\alpha) = V_{\alpha+1}$. The power set axiom holds because if $X \in V_\alpha$, then $\mathcal{P}(X) \in V_{\alpha+2}$. The axiom of regularity holds because any nonempty set in $V$ has an $\in$-minimal element.
