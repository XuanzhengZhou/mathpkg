---
role: proof
locale: en
of_concept: cohomology-commutes-with-flat-base-extension
source_book: gtm052
source_chapter: "III"
source_section: "9"
---
The question is local on $Y$ and on $Y'$, so we may assume they are both affine, say $Y = \operatorname{Spec} A$ and $Y' = \operatorname{Spec} A'$. Then by (8.5) what we have to show is that
$$H^i(X, \mathcal{F}) \otimes_A A' \cong H^i(X', \mathcal{F}').$$
Since $X$ is separated and noetherian, and $\mathcal{F}$ is quasi-coherent, we can calculate $H^i(X, \mathcal{F})$ by Čech cohomology with respect to an open affine cover $\mathfrak{U}$ of $X$ (4.5). On the other hand, $\{v^{-1}(U) \mid U \in \mathfrak{U}\}$ forms an open affine cover $\mathfrak{U}'$ of $X'$, and clearly the Čech complex $C'(\mathfrak{U}', v^* \mathcal{F})$ is just $C'(\mathfrak{U}, \mathcal{F}) \otimes_A A'$. Since $A'$ is flat over $A$, the functor $\cdot \otimes_A A'$ commutes with taking cohomology groups of the Čech complex, so we get our result.
