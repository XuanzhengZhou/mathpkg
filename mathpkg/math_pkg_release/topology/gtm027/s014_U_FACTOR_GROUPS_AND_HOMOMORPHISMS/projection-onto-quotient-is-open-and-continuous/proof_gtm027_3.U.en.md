---
role: proof
locale: en
of_concept: projection-onto-quotient-is-open-and-continuous
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Projection of a topological group onto the homogeneous quotient space is open and continuous

Let $G$ be a topological group, $H$ a subgroup, and $\pi: G \to G/H$ the natural projection defined by $\pi(x) = xH$.

---

**Continuity.** By definition of the quotient topology on $G/H$, a subset $V \subseteq G/H$ is open if and only if $\pi^{-1}(V)$ is open in $G$. Hence $\pi$ is continuous by construction.

---

**Openness.** Let $U \subseteq G$ be an arbitrary open set. We show that $\pi(U)$ is open in $G/H$, i.e., its saturation $\pi^{-1}(\pi(U))$ is open in $G$.

The saturation is

$$\pi^{-1}(\pi(U)) = \{g \in G : gH \in \pi(U)\} = \{g \in G : gH = uH \text{ for some } u \in U\}.$$

If $gH = uH$, then $u^{-1}g \in H$, so $g = uh$ for some $h \in H$. Conversely, if $g = uh$ with $u \in U$, $h \in H$, then $gH = uhH = uH$. Therefore

$$\pi^{-1}(\pi(U)) = U \cdot H = \{uh : u \in U,\; h \in H\} = \bigcup_{h \in H} U h.$$

For each $h \in H$, the set $Uh = \{uh : u \in U\}$ is the image of $U$ under right translation $x \mapsto xh$, which is a homeomorphism of $G$ (since $G$ is a topological group). Hence each $Uh$ is open in $G$. The union $\bigcup_{h \in H} Uh$ is therefore open in $G$.

Consequently $\pi^{-1}(\pi(U))$ is open, so $\pi(U)$ is open in $G/H$ by definition of the quotient topology. Thus $\pi$ is an open map.

We have shown that $\pi$ is both continuous and open. $\square$
