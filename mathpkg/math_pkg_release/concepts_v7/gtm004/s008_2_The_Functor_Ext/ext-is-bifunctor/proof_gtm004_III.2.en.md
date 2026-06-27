---
role: proof
locale: en
of_concept: ext-is-bifunctor
source_book: gtm004
source_chapter: "III"
source_section: "2. The Functor Ext"
---

# Proof of Ext is a Bifunctor

We need to show that $\operatorname{Ext}_\Lambda(-, -)$ is a bifunctor from the category of $\Lambda$-modules to the category of abelian groups, contravariant in the first variable and covariant in the second.

## Functoriality in the second variable (covariant)

Given $\beta : B \to B'$, we define $\beta_* : \operatorname{Ext}_\Lambda(A, B) \to \operatorname{Ext}_\Lambda(A, B')$ as follows. Choose a projective presentation $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$. For a representative $\varphi : R \to B$ of an element $[\varphi] \in \operatorname{Ext}_\Lambda^\varepsilon(A, B)$, define

$$
\beta_*[\varphi] = [\beta \circ \varphi].
$$

This is well-defined because if $\varphi' = \varphi + \psi\mu$ with $\psi : P \to B$, then $\beta\varphi' = \beta\varphi + (\beta\psi)\mu$, so $[\beta\varphi'] = [\beta\varphi]$. The assignment $\beta \mapsto \beta_*$ respects composition and identity, making $\operatorname{Ext}_\Lambda(A, -)$ a covariant functor.

## Functoriality in the first variable (contravariant)

Given $\alpha : A' \to A$, we define $\alpha^* : \operatorname{Ext}_\Lambda(A, B) \to \operatorname{Ext}_\Lambda(A', B)$ as follows. Choose projective presentations $R' \xrightarrow{\mu'} P' \xrightarrow{\varepsilon'} A'$ and $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$. Since $P'$ is projective, there exists a lifting $\pi : P' \to P$ making the diagram

$$
\begin{CD}
R' @>{\mu'}>> P' @>{\varepsilon'}>> A' \\
@V{\sigma}VV @V{\pi}VV @VV{\alpha}V \\
R @>{\mu}>> P @>{\varepsilon}>> A
\end{CD}
$$

commute. The map $\sigma : R' \to R$ is induced by restriction. Define

$$
\alpha^*[\varphi] = [\varphi \circ \sigma].
$$

By Lemma 2.1, this definition is independent of the choice of lifting $\pi$. By Corollary 2.2, it is also independent (up to natural isomorphism) of the choice of projective presentations. The assignment $\alpha \mapsto \alpha^*$ respects composition and identity, making $\operatorname{Ext}_\Lambda(-, B)$ a contravariant functor.

## Bifunctoriality

It remains to verify that the two functorialities are compatible, i.e., for $\alpha : A' \to A$ and $\beta : B \to B'$, the following diagram commutes:

$$
\begin{CD}
\operatorname{Ext}_\Lambda(A, B) @>{\beta_*}>> \operatorname{Ext}_\Lambda(A, B') \\
@V{\alpha^*}VV @VV{\alpha^*}V \\
\operatorname{Ext}_\Lambda(A', B) @>{\beta_*}>> \operatorname{Ext}_\Lambda(A', B')
\end{CD}
$$

This follows directly from the definitions:

$$
\alpha^*\beta_*[\varphi] = \alpha^*[\beta\varphi] = [\beta\varphi\sigma] = \beta_*[\varphi\sigma] = \beta_*\alpha^*[\varphi].
$$

Thus $\operatorname{Ext}_\Lambda(-, -)$ is a bifunctor to the category of abelian groups, contravariant in the first variable and covariant in the second.
