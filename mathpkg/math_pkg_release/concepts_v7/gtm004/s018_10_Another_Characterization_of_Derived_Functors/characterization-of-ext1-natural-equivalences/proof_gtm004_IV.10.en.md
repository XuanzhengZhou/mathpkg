---
role: proof
locale: en
of_concept: characterization-of-ext1-natural-equivalences
source_book: gtm004
source_chapter: "IV"
source_section: "10. Another Characterization of Derived Functors"
---

# Proof of Characterization of Natural Equivalences of $\operatorname{Ext}^1$

**Theorem 10.4.** For a homomorphism $\alpha : A' \to A$, the induced natural transformation

$$\alpha^* : \operatorname{Ext}_\Lambda^1(A, -) \longrightarrow \operatorname{Ext}_\Lambda^1(A', -)$$

is a natural equivalence if and only if $\alpha$ can be factored as

$$A' \xrightarrow{\sigma} A \oplus P \xrightarrow{\pi_A} A$$

where $P$ is a projective $\Lambda$-module, $\pi_A$ is the projection onto the summand $A$, and $\sigma$ is an isomorphism.

---

**Proof.**

We first prove the result under the additional assumption that $\alpha$ is an epimorphism; the general case will then be reduced to this one.

*Step 1: The epimorphism case* $(\Rightarrow)$. Suppose $\alpha : A' \twoheadrightarrow A$ is surjective and $\alpha^*$ is a natural equivalence. Let $A'' = \ker \alpha$ and form the short exact sequence

$$0 \longrightarrow A'' \longrightarrow A' \xrightarrow{\alpha} A \longrightarrow 0.$$

Applying the functor $\operatorname{Ext}_\Lambda^*(-, B)$ to this sequence yields, by Theorem IV.7.5, a long exact sequence

$$
\begin{aligned}
0 &\to \operatorname{Hom}_\Lambda(A, B) \to \operatorname{Hom}_\Lambda(A', B) \to \operatorname{Hom}_\Lambda(A'', B) \\
  &\to \operatorname{Ext}_\Lambda^1(A, B) \xrightarrow{\alpha^*} \operatorname{Ext}_\Lambda^1(A', B) \\
  &\to \operatorname{Ext}_\Lambda^1(A'', B) \to \operatorname{Ext}_\Lambda^2(A, B) \to \operatorname{Ext}_\Lambda^2(A', B) \to \cdots
\end{aligned}
\tag{10.5}
$$

Since $\alpha^*$ is an isomorphism, the connecting homomorphism $\operatorname{Hom}_\Lambda(A'', B) \to \operatorname{Ext}_\Lambda^1(A, B)$ is zero and the map $\operatorname{Ext}_\Lambda^1(A'', B) \to \operatorname{Ext}_\Lambda^2(A, B)$ is injective. A standard diagram chase using naturality then forces $\operatorname{Ext}_\Lambda^1(A'', B) = 0$ for all $B$. By Corollary III.5.5, this implies that $A''$ is projective.

Now choose $B = A''$ in the sequence (10.5). Since $\alpha^*$ is an isomorphism, we have $\operatorname{Ext}_\Lambda^1(A, A'') = 0$, and the map

$$\operatorname{Hom}_\Lambda(A', A'') \longrightarrow \operatorname{Hom}_\Lambda(A'', A'')$$

is surjective. The identity map $1_{A''}$ therefore lifts to a homomorphism $A' \to A''$, providing a splitting of the inclusion $A'' \hookrightarrow A'$. Hence the short exact sequence splits:

$$A' \cong A \oplus A''.$$

Setting $P = A''$ (which is projective), the map $\alpha$ corresponds under this isomorphism to the projection $\pi_A : A \oplus P \to A$.

*Step 2: Reduction of the general case to the epimorphism case.* Let $\alpha : A' \to A$ be an arbitrary homomorphism (not necessarily surjective) such that $\alpha^*$ is a natural equivalence. Take a projective presentation $\varepsilon : Q \twoheadrightarrow A$ of $A$ and form the map

$$\bar{\alpha} = \langle \alpha, \varepsilon \rangle : A' \oplus Q \longrightarrow A,$$

given by $\bar{\alpha}(a', q) = \alpha(a') + \varepsilon(q)$. Since $\varepsilon$ is surjective, $\bar{\alpha}$ is an epimorphism.

Let $\iota = \iota_{A'} : A' \to A' \oplus Q$ be the canonical inclusion into the direct sum. Then $\bar{\alpha} \circ \iota = \alpha$, and therefore

$$\alpha^* = \iota^* \circ \bar{\alpha}^*.$$

Now $Q$ is projective and $\iota$ is a split monomorphism with cokernel $Q$; it follows readily that $\iota^* : \operatorname{Ext}_\Lambda^1(A' \oplus Q, -) \to \operatorname{Ext}_\Lambda^1(A', -)$ is a natural equivalence. Since $\alpha^*$ is assumed to be a natural equivalence, the composition $\bar{\alpha}^* = (\iota^*)^{-1} \circ \alpha^*$ is also a natural equivalence. Applying Step 1 to the epimorphism $\bar{\alpha}$, we conclude that $\bar{\alpha}$ factors as

$$\bar{\alpha} : A' \oplus Q \xrightarrow{\cong} A \oplus \bar{P} \xrightarrow{\pi_A} A$$

with $\bar{P}$ projective. Restricting this factorization via $\iota$, we obtain

$$\alpha = \bar{\alpha} \circ \iota : A' \xrightarrow{\iota} A' \oplus Q \xrightarrow{\cong} A \oplus \bar{P} \xrightarrow{\pi_A} A,$$

which exhibits $\alpha$ in the required form (with $P = \bar{P}$ projective). This completes the proof of the forward implication.

*Step 3: The converse* $(\Leftarrow)$. Suppose $\alpha : A' \to A$ factors as

$$A' \xrightarrow{\sigma} A \oplus P \xrightarrow{\pi_A} A$$

where $P$ is projective, $\pi_A$ is the projection, and $\sigma$ is an isomorphism. Then $\alpha^* = \sigma^* \circ \pi_A^*$.

The map $\sigma^* : \operatorname{Ext}_\Lambda^1(A \oplus P, -) \to \operatorname{Ext}_\Lambda^1(A', -)$ is a natural equivalence because $\sigma$ is an isomorphism. For the projection $\pi_A$, we use the additivity of $\operatorname{Ext}_\Lambda^1$:

$$\operatorname{Ext}_\Lambda^1(A \oplus P, B) \cong \operatorname{Ext}_\Lambda^1(A, B) \oplus \operatorname{Ext}_\Lambda^1(P, B) = \operatorname{Ext}_\Lambda^1(A, B),$$

since $\operatorname{Ext}_\Lambda^1(P, B) = 0$ for $P$ projective. The projection $\pi_A$ induces the inclusion of the first summand, which is an isomorphism. Hence $\pi_A^*$ is a natural equivalence. The composition $\alpha^* = \sigma^* \circ \pi_A^*$ is therefore a natural equivalence.

This completes the proof. $\square$

---

**Remark.** The theorem shows in particular that natural equivalences between $\operatorname{Ext}_\Lambda^1(A, -)$ and $\operatorname{Ext}_\Lambda^1(A', -)$ correspond exactly to homomorphisms $\alpha : A' \to A$ whose kernel (if $\alpha$ is surjective) or "defect from surjectivity" (in the general case) is projective. Equivalently, such natural equivalences arise precisely from homomorphisms that are split epimorphisms after stabilizing by a projective module.
