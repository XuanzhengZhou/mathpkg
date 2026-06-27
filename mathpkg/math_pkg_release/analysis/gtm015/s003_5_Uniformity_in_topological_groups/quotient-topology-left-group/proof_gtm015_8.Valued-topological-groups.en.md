---
role: proof
locale: en
of_concept: quotient-topology-left-group
source_book: gtm015
source_chapter: "8"
source_section: "Valued topological groups"
---

# Proof of Quotient topology properties for left topological groups

Let $G$ be a left topological group, $H$ a subgroup, $H \setminus G$ the space of right cosets with the quotient topology, and $\pi: G \to H \setminus G$ the canonical mapping $\pi(x) = Hx$.

**(i)** The mapping $x \mapsto ax$ is a homeomorphism of $G$ sending $e$ to $a$. Therefore the neighborhoods of $a$ are precisely the sets $aV$, where $V$ is a neighborhood of $e$. Moreover, if $U$ is open in $G$, then $aU$ is also open.

**(ii)** By definition of the quotient topology, $A \subset H \setminus G$ is open iff $\pi^{-1}(A)$ is open in $G$; in particular $\pi$ is continuous. If $U$ is open in $G$, then

$$\pi^{-1}(\pi(U)) = HU = \bigcup_{a \in H} aU$$

is a union of open sets (each $aU$ is open by (i)), hence is open in $G$. Therefore $\pi(U)$ is open in $H \setminus G$, so $\pi$ is an open mapping.

**(iii)** In view of (i), the proof given in (4.4) applies verbatim (with the notation $\pi$ interpreted as right coset projection). Explicitly, a set $W \subset H \setminus G$ is a neighborhood of $\pi(a)$ iff $\pi^{-1}(W)$ is a neighborhood of $a$, which by (i) means $aV \subset \pi^{-1}(W)$ for some neighborhood $V$ of $e$. Equivalently, $\pi(aV) \subset W$. Thus the neighborhoods of $\pi(a)$ are precisely the sets $\pi(aV)$ where $V$ runs over neighborhoods of $e$.
