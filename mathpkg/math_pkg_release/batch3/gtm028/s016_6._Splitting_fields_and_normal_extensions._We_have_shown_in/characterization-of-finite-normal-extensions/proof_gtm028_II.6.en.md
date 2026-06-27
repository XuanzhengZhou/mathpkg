---
role: proof
locale: en
of_concept: characterization-of-finite-normal-extensions
source_book: gtm028
source_chapter: "II"
source_section: "6. Splitting fields and normal extensions"
---

That any (finite or infinite) normal extension $K$ of $k$ satisfies the condition of the theorem is obvious, since a $k$-isomorphism of $K$ into $K'$ sends any element of $K$ into a conjugate element over $k$, and by normality all conjugates lie in $K$, so the image is contained in $K$ and is all of $K$ by finite dimensionality.

Conversely, assume that a finite extension $K$ of $k$ satisfies that condition. We fix a finite extension $K'$ of $K$ which is normal over $k$, for instance a least normal extension of $k$ containing $K$ (Theorem 14). If $\gamma$ is any element of $K$, then $K'$ contains all the conjugates of $\gamma$ over $k$. If $\gamma'$ is one of these conjugate elements, then there exists a $k$-automorphism $\rho$ of $K'$ which sends $\gamma$ into $\gamma'$ (Definition 2, Corollary 2). Then $\rho$ induces a $k$-isomorphism of $K$ into $K'$, and by our assumption this induced $k$-isomorphism is necessarily a $k$-automorphism of $K$. Hence $\gamma' = \gamma\rho \in K$ (since $\gamma \in K$). We have thus shown that $K$ contains all the conjugates of $\gamma$ over $k$. Since $\gamma$ is an arbitrary element of $K$ it follows that $K$ is normal over $k$.
