---
role: proof
locale: en
of_concept: lemma-killing-field-constant-rescaling
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

**Proof.** Suppose $x \in M$. By Section 3.6.1c,
$$g(D_X(\ell W), Y) + g(X, D_Y(\ell W)) = 0 = (X\ell)g(W, Y) + (Y\ell)g(X, W) \quad \forall X, Y \in M_x.$$

Suppose $g(X, W) = 0$. Since $Wx \neq 0$ we can choose $Y$ such that $g(Y, W) \neq 0$ and conclude $X\ell = 0$. Suppose $g(X, W) \neq 0$. Choosing $Y = X$ gives $X\ell = 0$ again. Thus $X\ell = 0$ for all $X \in M_x$. Since $M$ is connected and $x$ was arbitrary, $\ell$ is constant.
