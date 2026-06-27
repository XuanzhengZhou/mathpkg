---
role: proof
locale: en
of_concept: continuity-criterion-for-homomorphisms-via-identity-neighborhoods
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Continuity criterion for homomorphisms of topological groups via identity neighborhoods

Let $G$ and $H$ be topological groups and let $f : G \to H$ be a group homomorphism (not a priori continuous). Denote the identity elements by $e_G \in G$ and $e_H \in H$.

---

### Proof of ($\Rightarrow$) — necessity

Assume $f$ is continuous. Let $V \subseteq H$ be any neighborhood of $e_H$. Since $f(e_G) = e_H$, we have $e_G \in f^{-1}(V)$. By continuity of $f$, the preimage $f^{-1}(V)$ is an open set containing $e_G$, hence a neighborhood of $e_G$ in $G$. Thus the condition holds.

---

### Proof of ($\Leftarrow$) — sufficiency

Assume that for every neighborhood $V$ of $e_H$ in $H$, the set $f^{-1}(V)$ is a neighborhood of $e_G$ in $G$. We prove that $f$ is continuous at every point of $G$.

Let $x \in G$ and let $W$ be an open neighborhood of $f(x)$ in $H$. By continuity of the group operations in $H$, there exists an open neighborhood $V$ of $e_H$ such that

\[
f(x) \cdot V \subseteq W .
\]

(Explicitly, the multiplication map $H \times H \to H$ is continuous, so there exist neighborhoods $V_1$ of $f(x)$ and $V_2$ of $e_H$ with $V_1 \cdot V_2 \subseteq W$; we may take $V_1 = f(x) \cdot V$ for some neighborhood $V$ of $e_H$, yielding $f(x)VV \subseteq W$, and then replace $V$ by $V \cap V^{-1}$ to ensure $VV \subseteq W$; in any case such a $V$ exists.)

By hypothesis, $U := f^{-1}(V)$ is a neighborhood of $e_G$ in $G$. Consider the set

\[
x \cdot U = \{ x u : u \in U \}.
\]

This is a neighborhood of $x$ in $G$ (left translation is a homeomorphism). For any $y \in xU$, write $y = xu$ with $u \in U$. Then

\[
f(y) = f(xu) = f(x) f(u) \in f(x) \cdot V \subseteq W .
\]

Thus $f(xU) \subseteq W$, which shows that $f$ is continuous at $x$. Since $x$ was arbitrary, $f$ is continuous on $G$. $\square$

---

### Remark

A common equivalent formulation: a homomorphism $f : G \to H$ of topological groups is continuous if and only if it is continuous at the identity $e_G$. The above argument establishes this equivalence explicitly by translating the neighborhood condition from $e_G$ to an arbitrary point $x \in G$.
