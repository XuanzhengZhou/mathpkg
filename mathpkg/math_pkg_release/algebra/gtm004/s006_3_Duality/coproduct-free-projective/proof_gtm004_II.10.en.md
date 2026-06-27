---
role: proof
locale: en
of_concept: coproduct-free-projective
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Coproducts of Free and Projective Objects

**(i) A coproduct of free objects is free.** Let $Fr \dashv U$ be the free-forgetful adjunction, where $U: \mathfrak{C} \to \mathfrak{S}$. Since $Fr$ is a left adjoint, it preserves all colimits, in particular coproducts. In $\mathfrak{S}$, coproducts are disjoint unions. Thus if $S_i$ are sets and $Fr(S_i)$ are the corresponding free objects,

$$\coprod_i Fr(S_i) \cong Fr\left(\coprod_i S_i\right) = Fr\left(\bigsqcup_i S_i\right),$$

which is free on the disjoint union of the generating sets. Hence any coproduct of free objects is again free.

**(ii) A coproduct of projective objects is projective.** Let $\{P_i\}_{i \in I}$ be a family of projective objects in $\mathfrak{C}$ and let $P = \coprod_i P_i$ with injections $q_i: P_i \to P$. Consider a diagram

$$\begin{array}{ccc}
P & \xrightarrow{\varphi} & B \\
& & \downarrow{\scriptstyle \varepsilon} \\
A & \xrightarrow{\varepsilon} & B
\end{array}$$

with $\varepsilon$ epimorphic. Write $\varphi = \langle \varphi_i \rangle$ where $\varphi_i = \varphi \circ q_i: P_i \to B$, using the universal property of the coproduct.

For each $i \in I$, since $P_i$ is projective, there exists $\psi_i: P_i \to A$ such that $\varepsilon \circ \psi_i = \varphi_i$. Define $\psi = \langle \psi_i \rangle: P \to A$ by the universal property of the coproduct (so $\psi \circ q_i = \psi_i$). Then for each $i$,

$$(\varepsilon \circ \psi) \circ q_i = \varepsilon \circ \psi_i = \varphi_i = \varphi \circ q_i.$$

By the uniqueness part of the universal property of the coproduct, $\varepsilon \circ \psi = \varphi$. Hence $P$ is projective.

Moreover, if the morphism sets of $\mathfrak{C}$ are nonempty, then the converse also holds: if $P = \coprod_i P_i$ is projective, then each $P_i$ is projective (by Proposition 10.5(i), each $P_i$ is a retract of $P$).
