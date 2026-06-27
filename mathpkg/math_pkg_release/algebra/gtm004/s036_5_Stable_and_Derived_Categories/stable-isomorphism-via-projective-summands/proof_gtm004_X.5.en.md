---
role: proof
locale: en
of_concept: stable-isomorphism-via-projective-summands
source_book: gtm004
source_chapter: "X"
source_section: "5. Stable and Derived Categories"
---

# Proof of Characterization of Stable Isomorphism via Projective Summands

Let $R$ be a ring and $\mathfrak{StM}_R$ the stable category of left $R$-modules. We prove that two $R$-modules $A$ and $B$ are isomorphic in $\mathfrak{StM}_R$ if and only if there exist projective $R$-modules $P$ and $Q$ such that $A \oplus P \cong B \oplus Q$ in $\mathfrak{M}_R$.

**($\Leftarrow$)** Suppose there exist projective modules $P$ and $Q$ with an isomorphism $\varphi: A \oplus P \xrightarrow{\cong} B \oplus Q$ in $\mathfrak{M}_R$. Let $\pi_A: A \oplus P \to A$ be the projection and $\iota_B: B \to B \oplus Q$ the inclusion. In $\mathfrak{StM}_R$, projective modules are isomorphic to zero (see the proposition "Projective Modules are Zero in the Stable Category"), so the canonical projection $A \oplus P \to A$ and inclusion $A \to A \oplus P$ induce isomorphisms $A \oplus P \cong A$ in $\mathfrak{StM}_R$. Similarly $B \oplus Q \cong B$. Therefore the isomorphism $\varphi$ in $\mathfrak{M}_R$ descends to an isomorphism $A \cong A \oplus P \cong B \oplus Q \cong B$ in $\mathfrak{StM}_R$.

**($\Rightarrow$)** Suppose $A \cong B$ in $\mathfrak{StM}_R$. Then there exist morphisms $f: A \to B$ and $g: B \to A$ in $\mathfrak{M}_R$ such that their images $\underline{f}$ and $\underline{g}$ in $\underline{\operatorname{Hom}}_R$ are mutual inverses. Thus

$$g \circ f - \operatorname{id}_A \in \operatorname{Phom}_R(A, A), \qquad f \circ g - \operatorname{id}_B \in \operatorname{Phom}_R(B, B).$$

By definition of projective homomorphisms, there exist projective modules $P_1, P_2$ and factorizations

$$g \circ f - \operatorname{id}_A = \alpha \circ \beta, \quad \beta: A \to P_1,\; \alpha: P_1 \to A,$$
$$f \circ g - \operatorname{id}_B = \gamma \circ \delta, \quad \delta: B \to P_2,\; \gamma: P_2 \to B.$$

Define $P = P_1 \oplus P_2$ (projective) and $Q = P$ (also projective). Now consider the maps

$$\Phi: A \oplus P \to B \oplus Q, \quad \Phi(a, p_1, p_2) = (f(a) + \gamma(p_2),\; \beta(a) + \delta \gamma(p_2),\; p_1),$$
$$\Psi: B \oplus Q \to A \oplus P, \quad \Psi(b, q_1, q_2) = (g(b) + \alpha(q_1),\; \delta(b) + \beta \alpha(q_1),\; q_2).$$

A direct computation using the relations $g \circ f = \operatorname{id}_A + \alpha\beta$ and $f \circ g = \operatorname{id}_B + \gamma\delta$ shows that $\Phi \circ \Psi = \operatorname{id}_{B \oplus Q}$ and $\Psi \circ \Phi = \operatorname{id}_{A \oplus P}$. Hence $A \oplus P \cong B \oplus Q$ in $\mathfrak{M}_R$.

Thus $A \cong B$ in $\mathfrak{StM}_R$ if and only if $A$ and $B$ differ by projective direct summands in $\mathfrak{M}_R$. $\square$
