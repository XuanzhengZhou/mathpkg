---
role: proof
locale: en
of_concept: free-lie-algebra-cohomology-vanishing
source_book: gtm004
source_chapter: "VII"
source_section: "2. Definition of Cohomology; H^0, H^1"
---

# Proof of Vanishing of Cohomology for Free Lie Algebras

**Corollary 2.6.** For a free Lie algebra $\mathfrak{f}$, we have $H^n(\mathfrak{f}, A) = 0$ for all $\mathfrak{f}$-modules $A$ and all $n \geq 2$.

---

## Proof

Let $\mathfrak{f} = \mathfrak{f}(V)$ be the free $K$-Lie algebra on the $K$-vector space $V$. By the universal property of the free Lie algebra, the canonical inclusion $V \hookrightarrow \mathfrak{f}$ induces an isomorphism between the universal enveloping algebra $U\mathfrak{f}$ and the tensor algebra $T(V)$:
$$U\mathfrak{f} \cong T(V) = K \oplus V \oplus (V \otimes V) \oplus (V \otimes V \otimes V) \oplus \cdots.$$

Consider the augmentation map $\varepsilon: T(V) \to K$ that sends all tensors of positive degree to $0$ and acts as the identity on $K$. Its kernel $I\mathfrak{f} = \ker(\varepsilon)$ consists of all tensors of degree $\geq 1$. As a left $T(V)$-module, we have an isomorphism
$$I\mathfrak{f} \cong T(V) \otimes_K V,$$
given by stripping off the rightmost tensor factor. Explicitly, for $t \in T(V)$ and $v \in V$, the element $t \otimes v \in T(V) \otimes_K V$ corresponds to $t \otimes v \in I\mathfrak{f}$ (concatenation in the tensor algebra).

This yields a free $U\mathfrak{f}$-module resolution of the trivial module $K$ of length $1$:
$$0 \longrightarrow U\mathfrak{f} \otimes_K V \overset{\mu}{\longrightarrow} U\mathfrak{f} \overset{\varepsilon}{\longrightarrow} K \longrightarrow 0,$$
where $\mu(u \otimes v) = u \cdot v$ (right multiplication, placing $v$ in $I\mathfrak{f} \subset U\mathfrak{f}$).

This is indeed a resolution: $\mu$ is injective because $U\mathfrak{f} = T(V)$ is a free associative algebra, so the multiplication map $T(V) \otimes V \to I\mathfrak{f}$ is an isomorphism of $T(V)$-modules. The image of $\mu$ is precisely $\ker(\varepsilon) = I\mathfrak{f}$.

Since $U\mathfrak{f} \otimes_K V$ is a free $U\mathfrak{f}$-module, the cohomology groups are computed as
$$H^n(\mathfrak{f}, A) = \operatorname{Ext}_{U\mathfrak{f}}^n(K, A) \cong H^n\bigl(\operatorname{Hom}_{U\mathfrak{f}}(P_{\bullet}, A)\bigr),$$
where $P_{\bullet}$ is the projective resolution
$$P_1 = U\mathfrak{f} \otimes_K V \to P_0 = U\mathfrak{f} \to K \to 0,$$
with $P_n = 0$ for $n \geq 2$. Applying $\operatorname{Hom}_{U\mathfrak{f}}(-, A)$ yields the cochain complex
$$0 \to \operatorname{Hom}_{U\mathfrak{f}}(U\mathfrak{f}, A) \to \operatorname{Hom}_{U\mathfrak{f}}(U\mathfrak{f} \otimes_K V, A) \to 0 \to 0 \to \cdots.$$
Since the complex has zero modules in all degrees $n \geq 2$, its cohomology vanishes for $n \geq 2$. Therefore
$$H^n(\mathfrak{f}, A) = 0 \qquad \text{for all } n \geq 2. \quad \square$$

**Remark.** This result is the Lie algebra analogue of Corollary VI.5.6, which asserts that the cohomology of a free group is trivial in dimensions $\geq 2$. The key point in both cases is that a free object has a universal enveloping algebra (or group ring) of global dimension $\leq 1$.
