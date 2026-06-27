---
role: proof
locale: en
of_concept: proposition-5-15-proj-closed-subscheme
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

(a) Let $\mathcal{I}_Y$ be the ideal sheaf of $Y$ on $X = \mathbf{P}_A^r$. Now $\mathcal{I}_Y$ is a subsheaf of $\mathcal{O}_X$; the twisting functor is exact; the global section functor $\Gamma$ is left exact; hence $\Gamma_*(\mathcal{I}_Y)$ is a submodule of $\Gamma_*(\mathcal{O}_X)$. But by (5.13), $\Gamma_*(\mathcal{O}_X) = S$. Hence $\Gamma_*(\mathcal{I}_Y)$ is a homogeneous ideal of $S$, which we will call $I$. Now $I$ determines a closed subscheme of $X$ (Ex. 3.12), whose sheaf of ideals will be $	ilde{I}$. Since $\mathcal{I}_Y$ is quasi-coherent by (5.9), we have $\mathcal{I}_Y \cong 	ilde{I}$ by (5.15), and hence $Y$ is the subscheme determined by $I$. In fact, $\Gamma_*(\mathcal{I}_Y)$ is the largest ideal in $S$ defining $Y$ (Ex. 5.10).

(b) Recall that by definition $Y$ is projective over $\operatorname{Spec} A$ if it is isomorphic to a closed subscheme of $\mathbf{P}_A^r$ for some $r$ (\S 4). By part (a), any such $Y$ is isomorphic to $\operatorname{Proj} S/I$, and we can take $I$ to be contained in $S_+ = igoplus_{d > 0} S_d$ (Ex. 3.12), so that $(S/I)_0 = A$. Conversely, any such graded ring $S$ is a quotient of a polynomial ring, so $\operatorname{Proj} S$ is projective.
