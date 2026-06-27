---
role: proof
locale: en
of_concept: h0-invariant-elements
source_book: gtm004
source_chapter: "VII"
source_section: "2. Definition of Cohomology; H^0, H^1"
---

# Proof of Characterization of $H^0$: the Subspace of Invariant Elements

**Statement.** For any $\mathfrak{g}$-module $A$,
$$H^0(\mathfrak{g}, A) = \{a \in A \mid x \circ a = 0 \text{ for all } x \in \mathfrak{g}\} = A^{\mathfrak{g}},$$
the subspace of invariant elements in $A$.

---

## Proof

By definition,
$$H^0(\mathfrak{g}, A) = \operatorname{Ext}_{\mathfrak{g}}^0(K, A) = \operatorname{Hom}_{\mathfrak{g}}(K, A),$$
where $K$ is regarded as a trivial $\mathfrak{g}$-module.

Let $\varphi: K \to A$ be a $\mathfrak{g}$-module homomorphism and set $a = \varphi(1) \in A$. For any $x \in \mathfrak{g}$, since $K$ is trivial we have $x \cdot 1 = 0$ in $K$, and by the $\mathfrak{g}$-module homomorphism property,
$$x \circ a = x \circ \varphi(1) = \varphi(x \cdot 1) = \varphi(0) = 0.$$
Thus $a \in A^{\mathfrak{g}}$. Moreover, $\varphi$ is determined by $a$ since $\varphi(\lambda) = \varphi(\lambda \cdot 1) = \lambda \circ \varphi(1) = \lambda a$ for all $\lambda \in K$.

Conversely, given $a \in A$ with $x \circ a = 0$ for all $x \in \mathfrak{g}$, define $\varphi: K \to A$ by $\varphi(\lambda) = \lambda a$. For any $x \in \mathfrak{g}$ and $\lambda \in K$,
$$\varphi(x \cdot \lambda) = \varphi(0) = 0,$$
while
$$x \circ \varphi(\lambda) = x \circ (\lambda a) = \lambda(x \circ a) = \lambda \cdot 0 = 0.$$
Thus $\varphi$ is a $\mathfrak{g}$-module homomorphism.

The correspondences $\varphi \mapsto \varphi(1)$ and $a \mapsto (\lambda \mapsto \lambda a)$ are easily seen to be mutually inverse $K$-linear isomorphisms, establishing
$$H^0(\mathfrak{g}, A) = \operatorname{Hom}_{\mathfrak{g}}(K, A) \cong A^{\mathfrak{g}}. \quad \square$$
