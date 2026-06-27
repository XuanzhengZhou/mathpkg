---
role: proof
locale: en
of_concept: projective-implies-flat
source_book: gtm004
source_chapter: "III"
source_section: "7"
---

# Proof that Every Projective Module is Flat (Proposition 7.4)

Every projective $\Lambda$-module is flat.

**Proof.** A projective module $P$ is a direct summand of a free module $F = \bigoplus \Lambda$. Since $A \otimes_\Lambda -$ preserves direct sums (coproducts), it suffices to show that free modules are flat.

For a free module $\Lambda$, we have the natural isomorphism $A \otimes_\Lambda \Lambda \cong A$ (via $a \otimes \lambda \mapsto a\lambda$). The functor $- \otimes_\Lambda \Lambda$ is isomorphic to the identity functor on $\mathfrak{M}_\Lambda^r$, which is exact. Hence $\Lambda$ is flat.

For an arbitrary free module $F = \bigoplus_i \Lambda$, since $A \otimes_\Lambda F \cong \bigoplus_i (A \otimes_\Lambda \Lambda) \cong \bigoplus_i A$, and direct sums of exact sequences are exact, the functor $A \otimes_\Lambda F$ is exact. Thus $F$ is flat.

Now let $P$ be projective, so $P \oplus Q \cong F$ for some $Q$ and some free module $F$. For any monomorphism $\mu : A' \hookrightarrow A$, we have the commutative diagram:

$$
\begin{array}{ccc}
A' \otimes_\Lambda P \oplus A' \otimes_\Lambda Q & \cong & A' \otimes_\Lambda F \\
\downarrow \mu \otimes 1_P \oplus \mu \otimes 1_Q & & \downarrow \mu \otimes 1_F \\
A \otimes_\Lambda P \oplus A \otimes_\Lambda Q & \cong & A \otimes_\Lambda F
\end{array}
$$

Since $\mu \otimes 1_F$ is monomorphic (as $F$ is flat), its restriction to the direct summand $\mu \otimes 1_P$ must also be monomorphic. Hence $P$ is flat.
