---
role: proof
locale: en
of_concept: homotopy-invariance-of-degree
source_book: gtm033
source_chapter: "5"
source_section: "Introduction"
---

# Proof of Homotopy Invariance of the Degree

The theorem follows from the sequence of lemmas established in Section 5.1. We prove the oriented case; the mod 2 case is similar.

**Theorem 5.1.6.** Let $M, N$ be compact $n$-manifolds without boundary, with $N$ connected.

(a) Homotopic maps $M \to N$ have the same degree if $M, N$ are oriented, and the same mod 2 degree otherwise.

(b) If $M = \partial W$ with $W$ compact, and a map $f: M \to N$ extends to $W$, then $\deg f = 0$ if $W$ and $N$ are orientable, and $\deg_2 f = 0$ otherwise.

*Proof of (a).* Let $f, g: M \to N$ be homotopic continuous maps. By Lemma 5.1.5, every continuous map can be approximated by $C^\infty$ maps homotopic to it. Thus we may replace $f$ and $g$ by $C^\infty$ maps $f', g'$ with $f \simeq f'$, $g \simeq g'$, and a $C^\infty$ homotopy $H: M \times I \to N$ between them.

Let $y \in N$ be a regular value for both $H$ and $H|_{\partial(M \times I)}$. Since $\partial M = \varnothing$, we have $\partial(M \times I) = M \times \{0\} \cup M \times \{1\}$, where $M \times \{1\}$ is given the opposite orientation to $M \times \{0\}$ (by the convention for the boundary orientation of a product). The restriction $H|_{M \times \{0\}}$ equals $f'$ and $H|_{M \times \{1\}}$ equals $g'$.

Applying Lemma 5.1.2 to the compact oriented $(n+1)$-manifold $W = M \times I$ and the map $h = H$, we obtain
$$\deg(H|_{\partial(M \times I)}, y) = 0.$$

By the definition of the degree on a disjoint union and the orientation convention,
$$\deg(H|_{\partial(M \times I)}, y) = \deg(f', y) - \deg(g', y).$$

Hence $\deg(f', y) = \deg(g', y)$. By Lemma 5.1.4, the degree $\deg(f', y)$ is independent of the choice of regular value $y$ when $N$ is connected. Therefore $\deg(f') = \deg(g')$.

Since homotopic maps have the same degree by the construction above, and $f \simeq f'$, $g \simeq g'$, we conclude $\deg(f) = \deg(g)$.

*Proof of (b).* Suppose $f: M = \partial W \to N$ extends to a $C^\infty$ map $F: W \to N$ (after approximation if necessary). Let $y \in N$ be a regular value for both $F$ and $F|_{\partial W} = f$. Applying Lemma 5.1.2 directly to $W$, $N$, $F$, and $y$ gives $\deg(f, y) = 0$. By Lemma 5.1.4, $\deg(f) = 0$.

The mod 2 case follows by the same argument, replacing the integer degree with the mod 2 degree throughout.

QED

**Remarks.** Lemma 5.1.1 (the orientation-flip lemma for arcs) provides the crucial orientation bookkeeping for Lemma 5.1.2. Lemma 5.1.3 establishes that the local degree at a regular point is $\pm 1$ depending on whether the derivative preserves or reverses orientation. Lemma 5.1.4 (independence of regular value) relies on the connectedness of $N$ and the existence of an isotopy moving one regular value to another. Lemma 5.1.5 (approximation) uses the fact that every $C^\infty$ manifold is a $C^\infty$ retract of an open subset of Euclidean half-space.
