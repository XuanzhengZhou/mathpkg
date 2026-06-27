---
role: proof
locale: en
of_concept: left-translation-on-homogeneous-space-is-homeomorphism
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Left translation on a homogeneous quotient space is a homeomorphism

Let $G$ be a topological group, $H$ a subgroup, and $G/H$ the homogeneous space of left cosets endowed with the quotient topology. Let $\pi : G \to G/H$ be the canonical projection $\pi(x) = xH$.

Fix an element $a \in G$. Define the left translation map

\[
L_a : G/H \longrightarrow G/H, \qquad L_a(xH) = a \cdot xH = (ax)H .
\]

---

### 1. Well-definedness

If $xH = yH$, then $y^{-1}x \in H$. Consequently,

\[
(ay)^{-1}(ax) = y^{-1}a^{-1}ax = y^{-1}x \in H,
\]

so $(ax)H = (ay)H$, i.e., $L_a(xH) = L_a(yH)$. Thus $L_a$ is well-defined.

---

### 2. Bijectivity

The map $L_a$ is bijective: its inverse is $L_{a^{-1}}$, because

\[
L_{a^{-1}}(L_a(xH)) = L_{a^{-1}}(axH) = a^{-1}axH = xH,
\]
\[
L_a(L_{a^{-1}}(xH)) = L_a(a^{-1}xH) = aa^{-1}xH = xH .
\]

---

### 3. Continuity

We use the factorization through the projection $\pi$. For any $x \in G$,

\[
L_a(\pi(x)) = L_a(xH) = axH = \pi(ax) = \pi(\lambda_a(x)),
\]

where $\lambda_a : G \to G$ is the left translation $\lambda_a(x) = ax$. Thus

\[
L_a \circ \pi = \pi \circ \lambda_a .
\]

Now let $W \subseteq G/H$ be an open set. To show $L_a$ is continuous, we must verify that $L_a^{-1}(W)$ is open. Since $\pi$ is a quotient map, a subset $U \subseteq G/H$ is open if and only if $\pi^{-1}(U)$ is open in $G$. Compute:

\[
\pi^{-1}\bigl(L_a^{-1}(W)\bigr) = (L_a \circ \pi)^{-1}(W) = (\pi \circ \lambda_a)^{-1}(W) = \lambda_a^{-1}\bigl(\pi^{-1}(W)\bigr).
\]

Since $W$ is open in $G/H$, $\pi^{-1}(W)$ is open in $G$. The map $\lambda_a$ is a homeomorphism of $G$ (left translation in a topological group is continuous with continuous inverse $\lambda_{a^{-1}}$), so $\lambda_a^{-1}(\pi^{-1}(W))$ is open in $G$. Therefore $\pi^{-1}(L_a^{-1}(W))$ is open in $G$, which implies $L_a^{-1}(W)$ is open in $G/H$. Hence $L_a$ is continuous.

---

### 4. Homeomorphism

Since $L_a$ is bijective and continuous, and its inverse $L_{a^{-1}}$ is continuous by the same argument (replace $a$ by $a^{-1}$), we conclude that $L_a$ is a homeomorphism. $\square$
