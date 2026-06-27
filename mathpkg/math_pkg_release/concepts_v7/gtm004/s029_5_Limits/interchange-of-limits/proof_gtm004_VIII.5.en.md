---
role: proof
locale: en
of_concept: interchange-of-limits
source_book: gtm004
source_chapter: "VIII"
source_section: "5"
---

# Proof of Interchange of Limits

Let $\mathfrak{C}$ be a category and $I, J$ small index categories. Recall the canonical identifications given by the exponential law for functor categories:

$$
\mathfrak{C}^{I \times J} \cong (\mathfrak{C}^J)^I \cong (\mathfrak{C}^I)^J.
$$

Let $P: \mathfrak{C} \to \mathfrak{C}^{I \times J}$, $P_1: \mathfrak{C} \to \mathfrak{C}^I$, and $P_2: \mathfrak{C} \to \mathfrak{C}^J$ be the diagonal (constant) functors. By hypothesis, each admits a right adjoint:

$$
P \dashv R, \qquad P_1 \dashv R_1, \qquad P_2 \dashv R_2.
$$

We have adjunctions $P_i \dashv R_i$ with $R_i P_i \cong 1_{\mathfrak{C}}$ for $i = 1, 2$, and similarly $RP \cong 1_{\mathfrak{C}}$ (see Proposition II.7.6 and Theorem II.8.3).

Now consider a functor $F: I \times J \to \mathfrak{C}$. Via the exponential law, $F$ corresponds to a functor $\tilde{F}: I \to \mathfrak{C}^J$, where $\tilde{F}(i)(j) = F(i,j)$. Applying $R_2: \mathfrak{C}^J \to \mathfrak{C}$ componentwise yields a functor $R_2 \circ \tilde{F}: I \to \mathfrak{C}$, and then $R_1(R_2 \circ \tilde{F})$ is an object of $\mathfrak{C}$. This is precisely $\lim_I \lim_J F$.

Conversely, we may view $F$ as a functor $I \times J \to \mathfrak{C}$ and apply $R: \mathfrak{C}^{I \times J} \to \mathfrak{C}$ directly, obtaining $R(F) = \lim_{I \times J} F$.

The key point is that both $R$ and $R_1 \circ (R_2)_*$ (where $(R_2)_*: \mathfrak{C}^{I \times J} \to \mathfrak{C}^I$ is the functor induced by $R_2$) are right adjoint to the same functor $P: \mathfrak{C} \to \mathfrak{C}^{I \times J}$, hence they are canonically naturally isomorphic. More explicitly, for any $C \in \mathfrak{C}$ and any $F \in \mathfrak{C}^{I \times J}$, we have natural bijections:

$$
\begin{aligned}
\mathfrak{C}^{I \times J}(P(C), F) &\cong \mathfrak{C}^I(P_1(C), R_J(F)) \\
&\cong \mathfrak{C}(C, R_1 R_J(F)),
\end{aligned}
$$

where $R_J: \mathfrak{C}^{I \times J} \to \mathfrak{C}^I$ is the right adjoint to the functor $\mathfrak{C}^{I \times J} \to \mathfrak{C}^I$ induced by $P_1$. Similarly, exchanging the roles of $I$ and $J$ yields a natural isomorphism with $R_2 R_I(F)$.

Thus we obtain the commutative diagram of right adjoints:

$$
\begin{CD}
\mathfrak{C}^{I \times J} @>{R_I}>> \mathfrak{C}^J \\
@V{R_J}VV @VV{R_2}V \\
\mathfrak{C}^I @>>{R_1}> \mathfrak{C}
\end{CD}
$$

By uniqueness of right adjoints up to canonical isomorphism, we conclude:

$$
\lim_I \lim_J \;\cong\; \lim_{I \times J} \;\cong\; \lim_J \lim_I.
$$

In other words, limits commute with limits. The result is stated as Theorem 5.1 in the text, and it provides the foundation for the subsequent theorems on pullback towers and spectral sequence limits. $\square$

**Remark.** This theorem holds in any category admitting the relevant limits. The proof uses only the formal properties of adjoint functors and the exponential law; no elementwise arguments are required.
