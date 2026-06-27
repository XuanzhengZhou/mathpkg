---
role: proof
locale: en
of_concept: zariskis-main-theorem
source_book: gtm052
source_chapter: "III"
source_section: "11"
---

*Proof.* By the previous result (Corollary 11.3), it suffices to verify that $f_*\mathcal{O}_X = \mathcal{O}_Y$. The question is local on $Y$, so we may assume $Y$ is affine, say $Y = \operatorname{Spec} A$. Then $A$ is an integrally closed domain. Since $f$ is birational, there is an open dense subset $U \subseteq Y$ over which $f$ is an isomorphism. Hence $\mathcal{O}_Y \to f_*\mathcal{O}_X$ is an isomorphism over $U$.

The sheaf $f_*\mathcal{O}_X$ is coherent (by properness of a projective morphism), so $H^0(Y, f_*\mathcal{O}_X) = H^0(X, \mathcal{O}_X)$ is a finite $A$-module. Moreover, $H^0(X, \mathcal{O}_X)$ is contained in the function field $K(Y)$ because $f$ is birational, and each element of $H^0(X, \mathcal{O}_X)$ is integral over $A$ (by the valuative criterion or by considering local rings). Since $A$ is integrally closed in $K(Y)$, we must have $H^0(X, \mathcal{O}_X) = A$. Thus $f_*\mathcal{O}_X = \mathcal{O}_Y$, completing the proof. $\square$
