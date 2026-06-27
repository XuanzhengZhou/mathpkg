---
role: proof
locale: en
of_concept: ideal-complement-in-semisimple
source_book: gtm004
source_chapter: "VII"
source_section: "5"
---

# Proof of Existence of Complementary Ideals

**Corollary 5.4.** Let $\mathfrak{a}$ be an ideal in the semi-simple Lie algebra $\mathfrak{g}$ (over a field of characteristic 0). Then there exists an ideal $\mathfrak{b}$ of $\mathfrak{g}$ such that $\mathfrak{g} = \mathfrak{a} \oplus \mathfrak{b}$ as Lie algebras.

**Proof.** Consider the Killing form $\kappa : \mathfrak{g} \times \mathfrak{g} \to K$, which is non-degenerate by Corollary 5.3. Define

$$\mathfrak{b} = \mathfrak{a}^{\perp} = \{ x \in \mathfrak{g} \mid \kappa(x, y) = 0 \text{ for all } y \in \mathfrak{a} \}.$$

We claim that $\mathfrak{b}$ is an ideal of $\mathfrak{g}$ and that $\mathfrak{g} = \mathfrak{a} \oplus \mathfrak{b}$.

First, $\mathfrak{b}$ is an ideal because for any $x \in \mathfrak{g}$, $y \in \mathfrak{b}$, and $z \in \mathfrak{a}$, the invariance of the Killing form gives

$$\kappa([x, y], z) = \kappa(x, [y, z]) - \kappa(y, [x, z]) = 0 - 0 = 0,$$

since $[y, z] \in \mathfrak{a}$ (as $\mathfrak{a}$ is an ideal and $z \in \mathfrak{a}$) and $[x, z] \in \mathfrak{a}$ (as $\mathfrak{a}$ is an ideal). Hence $[x, y] \in \mathfrak{b}$.

Second, $\mathfrak{a} \cap \mathfrak{b}$ is an ideal of $\mathfrak{g}$ on which the Killing form is identically zero. Cartan's criterion implies that $\operatorname{ad}(\mathfrak{a} \cap \mathfrak{b})$ is solvable, and since $\operatorname{ad}$ is faithful (as $\mathfrak{g}$ is semi-simple with trivial center), $\mathfrak{a} \cap \mathfrak{b}$ is a solvable ideal of the semi-simple algebra $\mathfrak{g}$. Hence $\mathfrak{a} \cap \mathfrak{b} = \{0\}$.

Finally, since $\kappa$ is non-degenerate, the orthogonal complement $\mathfrak{b}$ has dimension $\dim \mathfrak{g} - \dim \mathfrak{a}$. Together with $\mathfrak{a} \cap \mathfrak{b} = 0$, we obtain $\mathfrak{g} = \mathfrak{a} \oplus \mathfrak{b}$ as vector spaces, and the direct sum is a direct sum of Lie algebras because both summands are ideals. $\square$
