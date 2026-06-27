---
role: proof
locale: en
of_concept: resolvent-set-is-proper
source_book: gtm015
source_chapter: "51"
source_section: "51.7"
---

# Proof of The resolvent set is a proper subset

(51.7) Theorem. For each $x$ in $A$, $\rho(x)$ is a proper subset of $\mathbb{C}$.

Proof. Assume to the contrary that $\rho(x) = \mathbb{C}$ for some element $x$; then the resolvent function $R_x$ is defined on all of $\mathbb{C}$. Let $f$ be any continuous linear form on $A$ and define $F(\lambda) = f(R_x(\lambda)) (\lambda \in \mathbb{C})$. In view of (51.6), $F$ is a bounded entire function, therefore $F$ is constant by Liouville’s theorem; moreover, the constant must be zero, thus $F(\lambda) = 0$ for all $\lambda$. In particular, $0 = F(0) = -f(x^{-1})$; since $f$ is arbitrary, the Hahn-Banach theorem yields the absurdity $x^{-1} = 0$ (40.10).

A striking dividend of analyticity is that the theory of complex Banach algebras contains no new fields:
