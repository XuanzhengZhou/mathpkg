---
role: proof
locale: en
of_concept: quotient-by-invariant-subgroup-is-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Quotient of a topological group by an invariant subgroup is a topological group

Let $G$ be a topological group and let $H$ be an invariant (normal) subgroup of $G$. Let $G/H$ be the family of left cosets $xH$ endowed with the quotient topology induced by the canonical projection $\pi : G \to G/H$, $\pi(x) = xH$. Since $H$ is normal, $G/H$ is a group with multiplication $(xH)(yH) = xyH$ and inversion $(xH)^{-1} = x^{-1}H$.

From problem (a) we already know that $\pi$ is open and continuous. We now verify that $G/H$ is a topological group.

---

### 1. Continuity of multiplication

Let $m : G/H \times G/H \to G/H$ be the multiplication map $m(xH, yH) = xyH$, and let $m_G : G \times G \to G$ be multiplication in $G$, i.e., $m_G(x, y) = xy$. These maps are related by

\[
m \circ (\pi \times \pi) = \pi \circ m_G ,
\]

because for any $(x, y) \in G \times G$,

\[
m(\pi(x), \pi(y)) = m(xH, yH) = xyH = \pi(xy) = \pi(m_G(x, y)).
\]

Let $W \subseteq G/H$ be an open set. We must show that $m^{-1}(W)$ is open in $G/H \times G/H$. Since $\pi \times \pi$ is a quotient map (the product of two open surjective maps is open and surjective), a subset of $G/H \times G/H$ is open if and only if its preimage under $\pi \times \pi$ is open in $G \times G$. Compute:

\[
(\pi \times \pi)^{-1}\bigl(m^{-1}(W)\bigr) = (m \circ (\pi \times \pi))^{-1}(W) = (\pi \circ m_G)^{-1}(W) = m_G^{-1}\bigl(\pi^{-1}(W)\bigr).
\]

Since $W$ is open in $G/H$, $\pi^{-1}(W)$ is open in $G$ (by definition of the quotient topology). The multiplication $m_G$ is continuous in the topological group $G$, so $m_G^{-1}(\pi^{-1}(W))$ is open in $G \times G$. Therefore $(\pi \times \pi)^{-1}(m^{-1}(W))$ is open in $G \times G$, which implies that $m^{-1}(W)$ is open in $G/H \times G/H$. Hence $m$ is continuous.

---

### 2. Continuity of inversion

Let $\iota : G/H \to G/H$ be the inversion map $\iota(xH) = x^{-1}H$, and let $\iota_G : G \to G$ be inversion in $G$, i.e., $\iota_G(x) = x^{-1}$. These maps satisfy

\[
\iota \circ \pi = \pi \circ \iota_G ,
\]

because $\iota(\pi(x)) = \iota(xH) = x^{-1}H = \pi(x^{-1}) = \pi(\iota_G(x))$.

Let $W \subseteq G/H$ be open. Then

\[
\pi^{-1}\bigl(\iota^{-1}(W)\bigr) = (\iota \circ \pi)^{-1}(W) = (\pi \circ \iota_G)^{-1}(W) = \iota_G^{-1}\bigl(\pi^{-1}(W)\bigr).
\]

Since $W$ is open, $\pi^{-1}(W)$ is open in $G$. The inversion map $\iota_G$ is continuous in the topological group $G$, so $\iota_G^{-1}(\pi^{-1}(W))$ is open in $G$. Therefore $\pi^{-1}(\iota^{-1}(W))$ is open in $G$, which implies $\iota^{-1}(W)$ is open in $G/H$. Hence $\iota$ is continuous.

---

### 3. The projection is a continuous open homomorphism

The projection $\pi : G \to G/H$ satisfies

\[
\pi(xy) = xyH = (xH)(yH) = \pi(x)\pi(y),
\]

so $\pi$ is a group homomorphism. By problem (a), $\pi$ is open and continuous. This completes the proof. $\square$
