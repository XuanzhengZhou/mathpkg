---
role: proof
locale: en
of_concept: limit-factorization-proposition
source_book: gtm004
source_chapter: "VIII"
source_section: "8"
---

# Proof of Limit Factorization Property

**Proposition 8.2.** Suppose that for all $p$, the inclusion $\nu^p: X^p \to X$ factorizes as

$$X^p \xrightarrow{\nu'^p} Y \xrightarrow{\mu} X,$$

where $\mu: Y \to X$ is independent of $p$. Set $Y_p = Y / X^p$ and let $\eta'_p: Y \to Y_p$ be the canonical projection. Then the transition maps $\xi_p: X_p \to X_{p+1}$ induce maps $\xi'_p: Y_p \to Y_{p+1}$, and we have the commutative diagram

$$
\begin{array}{ccccccc}
X^{p-1} & \xrightarrow{\xi^p} & X^p & & Y & \xrightarrow{\eta'_p} & Y_p & \xrightarrow{\xi'_p} & Y_{p+1} \\
\parallel & & \parallel & & {\scriptstyle\mu}\downarrow & & {\scriptstyle\mu_p}\downarrow & & {\scriptstyle\mu_{p+1}}\downarrow \\
X^{p-1} & \xrightarrow{\xi^p} & X^p & \xrightarrow{\nu^p} & X & \xrightarrow{\eta_p} & X_p & \xrightarrow{\xi_p} & X_{p+1}
\end{array}
$$

which is easily seen to be bicartesian (each square is both a pushout and a pullback). If

$$(X; \eta_p) = \varprojlim (X_p, \xi_p),$$

i.e., if the filtration of $X$ is right complete, then

$$(Y; \eta'_p) = \varprojlim (Y_p, \xi'_p).$$

**Proof.** Let $Z$ be an arbitrary object equipped with a compatible family of morphisms $\zeta_p: Z \to Y_p$, i.e., $\xi'_p \zeta_p = \zeta_{p+1}$ for all $p$. Compose with $\mu_{p+1}: Y_{p+1} \to X_{p+1}$ to obtain morphisms

$$\mu_{p+1} \zeta_{p+1}: Z \to X_{p+1}.$$

These morphisms are compatible with the transition maps $\xi_p: X_p \to X_{p+1}$ because the right-hand squares of the diagram commute. Since $(X; \eta_p) = \varprojlim (X_p, \xi_p)$, there exists a unique morphism $\zeta: Z \to X$ such that $\eta_p \zeta = \mu_{p+1} \zeta_{p+1}$ for all $p$.

Now the bicartesian property of the central squares implies that $\zeta$ factors uniquely through $\mu: Y \to X$, yielding a morphism $\tilde{\zeta}: Z \to Y$ with $\mu \tilde{\zeta} = \zeta$. The uniqueness of the factorization through the limit then forces $\eta'_p \tilde{\zeta} = \zeta_p$ for all $p$. Thus $(Y; \eta'_p)$ satisfies the universal property of the limit, proving the claim. $\square$
