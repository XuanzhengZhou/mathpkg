---
role: proof
locale: en
of_concept: flatness-criterion-over-dedekind-domain
source_book: gtm052
source_chapter: "III"
source_section: "9"
---
First suppose that $f$ is flat, and let $x \in X$ be a point whose image $y = f(x)$ is a closed point of $Y$. Then $\mathcal{O}_{y,Y}$ is a discrete valuation ring. Let $t \in \mathfrak{m}_y \setminus \mathfrak{m}_y^2$ be a uniformizing parameter. Then $t$ is not a zero divisor in $\mathcal{O}_{y,Y}$. Since $f$ is flat, $f^\# t \in \mathfrak{m}_x$ is not a zero divisor, so $x$ is not an associated point of $X$.

Conversely, suppose that every associated point of $X$ maps to the generic point of $Y$. To show $f$ is flat, we must show that for any $x \in X$, letting $y = f(x)$, the local ring $\mathcal{O}_{x,X}$ is flat over $\mathcal{O}_{y,Y}$. If $y$ is the generic point, $\mathcal{O}_{y,Y}$ is a field, so there is nothing to prove. If $y$ is a closed point, $\mathcal{O}_{y,Y}$ is a discrete valuation ring, so by (9.1.3) we must show that $\mathcal{O}_{x,X}$ is a torsion-free module. If it is not, then $f^\# t$ must be a zero divisor in $\mathfrak{m}_x$, where $t$ is a uniformizing parameter of $\mathcal{O}_{y,Y}$. Therefore $f^\# t$ is contained in some associated prime ideal $\mathfrak{p}$ of $(0)$ in $\mathcal{O}_X$. Then $\mathfrak{p}$ determines a point $x' \in X$, which is an associated point of $X$, and whose image by $f$ is $y$, which is a contradiction.

Finally, note that if $X$ is reduced, its associated points are just the generic points of its irreducible components, so our condition says that each irreducible component of $X$ dominates $Y$.
