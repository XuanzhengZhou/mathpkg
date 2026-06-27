---
role: proof
locale: en
of_concept: factorization-of-continuous-homomorphism
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Factorization of a continuous homomorphism into an open homomorphism and a one-to-one homomorphism

Let $f : G \to J$ be a continuous homomorphism of topological groups. Let $H = f[G]$ be the image of $f$, endowed with the **quotient topology** induced by the surjective map $f : G \to H$. That is, a subset $W \subseteq H$ is open if and only if $f^{-1}(W)$ is open in $G$.

Define two maps:

\[
q : G \longrightarrow H, \qquad q(x) = f(x),
\]
\[
i : H \longrightarrow J, \qquad i(y) = y \quad (\text{the inclusion map}).
\]

Then clearly $f = i \circ q$. We verify the claimed properties of $q$ and $i$.

---

### 1. $q$ is a continuous, open homomorphism

**Homomorphism:** For $x, y \in G$,
\[
q(xy) = f(xy) = f(x)f(y) = q(x) q(y),
\]
so $q$ is a group homomorphism.

**Surjectivity:** $q$ is surjective onto $H = f[G]$ by definition.

**Continuity:** By definition of the quotient topology, a map into a quotient space is continuous precisely when its composition with the quotient map yields a continuous map. Here the quotient map is $q$ itself, but more concretely: $q$ is continuous because for any open $W \subseteq H$, we have $q^{-1}(W) = f^{-1}(W)$, which is open in $G$ since $f$ is continuous and $W$ is open in the quotient topology (meaning $f^{-1}(W)$ is open). In fact, the quotient topology is the *finest* topology on $H$ making $q$ continuous, so $q$ is continuous by construction.

**Openness:** Let $U \subseteq G$ be an open set. We must show that $q(U)$ is open in the quotient topology on $H$. By definition, $q(U)$ is open iff $q^{-1}(q(U))$ is open in $G$. Compute:

\[
q^{-1}(q(U)) = \{ x \in G : q(x) = q(u) \text{ for some } u \in U \}
            = \{ x \in G : f(x) = f(u) \text{ for some } u \in U \}.
\]

If $f(x) = f(u)$, then $f(u^{-1}x) = f(u)^{-1}f(x) = e_J$, so $u^{-1}x \in \ker f$. Hence $x = u \cdot k$ for some $k \in \ker f$. Thus

\[
q^{-1}(q(U)) = U \cdot \ker f = \bigcup_{k \in \ker f} U \cdot k .
\]

In a topological group, right translation $x \mapsto x \cdot k$ is a homeomorphism for each fixed $k$. Therefore each translate $U \cdot k$ is open, and the union of open sets is open. Hence $q^{-1}(q(U))$ is open in $G$, which proves that $q(U)$ is open in the quotient topology. Thus $q$ is an open map.

---

### 2. $i$ is a continuous, one-to-one homomorphism

**Homomorphism:** $i$ is the inclusion of the subgroup $H$ into $J$, so it is trivially a group homomorphism.

**Injectivity:** $i$ is the identity on $H$, hence injective (one-to-one).

**Continuity:** Let $W \subseteq J$ be open. Then $i^{-1}(W) = W \cap H$. In the quotient topology on $H$, this set is open iff $f^{-1}(W \cap H)$ is open in $G$. But $f^{-1}(W \cap H) = f^{-1}(W)$, and $f^{-1}(W)$ is open in $G$ because $f : G \to J$ is continuous. Hence $i^{-1}(W)$ is open in $H$, proving that $i$ is continuous.

---

### 3. Factorization

We have $f = i \circ q$, where $q : G \to H$ is a continuous open homomorphism (surjective) and $i : H \to J$ is a continuous one-to-one homomorphism (injective). This completes the factorization. $\square$
