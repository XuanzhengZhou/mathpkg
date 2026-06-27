---
role: proof
locale: en
of_concept: root-space-decomposition-properties
source_book: gtm009
source_chapter: "8"
source_section: "8.1"
---

(1) Let $x \in L_\alpha$, $y \in L_\beta$, $h \in H$. By the Jacobi identity:
$$\operatorname{ad} h([x,y]) = [[h,x],y] + [x,[h,y]] = \alpha(h)[x,y] + \beta(h)[x,y] = (\alpha+\beta)(h)[x,y].$$
Thus $[x,y] \in L_{\alpha+\beta}$.

(2) Since $\Phi$ is finite, only finitely many spaces $L_{\alpha+i\alpha}$ are nonzero for $i \in \mathbb{Z}$. So $\operatorname{ad} x$ is nilpotent for $x \in L_\alpha$, $\alpha \neq 0$.

(3) Find $h \in H$ with $(\alpha+\beta)(h) \neq 0$. For $x \in L_\alpha$, $y \in L_\beta$:
$$\kappa([h,x],y) = -\kappa([x,h],y) = -\kappa(x,[h,y]).$$
Thus $\alpha(h)\kappa(x,y) = -\beta(h)\kappa(x,y)$, so $(\alpha+\beta)(h)\kappa(x,y) = 0$, forcing $\kappa(x,y) = 0$. $\square$
