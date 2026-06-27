---
role: proof
locale: en
of_concept: neighborhood-system-properties
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof of Neighborhood System Properties

**Theorem.** If $\mathfrak{u}$ is the neighborhood system of a point $x$ in a topological space, then:

1. Finite intersections of members of $\mathfrak{u}$ belong to $\mathfrak{u}$;
2. Each set which contains a member of $\mathfrak{u}$ belongs to $\mathfrak{u}$.

*Proof.* (1) Let $U$ and $V$ be neighborhoods of a point $x$. By definition, there exist open neighborhoods $U_0$ and $V_0$ such that $U_0 \subseteq U$, $V_0 \subseteq V$, and $x \in U_0$, $x \in V_0$. Then $U_0 \cap V_0$ is an open set containing $x$ and contained in $U \cap V$. Hence $U \cap V$ is a neighborhood of $x$. By induction, the intersection of any finite number of members of $\mathfrak{u}$ is again a member of $\mathfrak{u}$.

(2) If a set $W$ contains a neighborhood $U$ of a point $x$, then $W$ contains an open neighborhood $U_0$ of $x$ (since $U$ itself contains some open neighborhood $U_0$ with $x \in U_0 \subseteq U \subseteq W$). Therefore $W$ is itself a neighborhood of $x$. $\square$
