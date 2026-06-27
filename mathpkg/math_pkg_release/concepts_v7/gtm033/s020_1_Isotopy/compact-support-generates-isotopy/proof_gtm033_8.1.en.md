---
role: proof
locale: en
of_concept: compact-support-generates-isotopy
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Time-Dependent Vector Field with Compact Support Generates Isotopy

**Theorem 1.2.** A time-dependent vector field which has compact support generates an isotopy. In particular every time-dependent vector field on a compact manifold generates an isotopy.

*Proof.* If $G$ is a time-dependent vector field on $M$ with compact support $\operatorname{Supp} G \subset M$, then $G$ has bounded velocity (since the support is compact and $G$ is smooth). By Theorem 1.1, $G$ generates a diffeotopy $F: M \times I \rightarrow M$ satisfying $\frac{\partial F}{\partial t}(x,t) = G(F(x,t),t)$. The restriction of this diffeotopy to any sub-interval of $I$ yields an isotopy. In particular, $F$ itself is an isotopy of $M$.

When $M$ is compact, every time-dependent vector field on $M$ automatically has compact support (since $M$ itself is compact), and the conclusion follows. $\square$
