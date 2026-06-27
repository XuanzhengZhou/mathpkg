---
role: proof
locale: en
of_concept: third-fundamental-form-cayley-relation
source_book: gtm051
source_chapter: "3"
source_section: "5"
---

Let $IV := (dn + \kappa_1 df) \cdot (dn + \kappa_2 df)$, where $\kappa_1, \kappa_2$ are the principal curvatures. Expanding the product of the bilinear forms gives

$$IV = dn \cdot dn + (\kappa_1 + \kappa_2) dn \cdot df + \kappa_1 \kappa_2 \, df \cdot df = III - 2H \, II + K \, I,$$

since $III = dn \cdot dn$, $II = -dn \cdot df$, $I = df \cdot df$, $2H = \kappa_1 + \kappa_2$, and $K = \kappa_1 \kappa_2$.

Now let $X_1$ be a principal direction for $\kappa_1$ and $X_2$ a principal direction for $\kappa_2$. For any tangent vector $Y$, we have $dn(Y) + \kappa_1 df(Y)$ orthogonal to $X_1$ (by definition of principal direction), and similarly $dn(Y) + \kappa_2 df(Y)$ orthogonal to $X_2$. It follows that

$$IV(X_1, Y) = (dn + \kappa_1 df)(X_1) \cdot (dn + \kappa_2 df)(Y) = 0 \cdot (dn + \kappa_2 df)(Y) = 0,$$

and similarly $IV(Y, X_2) = 0$. Since $\{X_1, X_2\}$ forms a basis of the tangent space (when $\kappa_1 \neq \kappa_2$) and $IV$ is a symmetric bilinear form, these conditions force $IV = 0$. Thus $III - 2H \, II + K \, I = 0$.

**Remark.** This proposition is a special case of the Cayley-Hamilton theorem: a linear mapping $L$ (in our case, the Weingarten map $L_u = -dn \circ df^{-1}$) satisfies its characteristic equation $\chi(L) = 0$, where $\chi(\kappa) = \det(L - \kappa \, \mathrm{id}) = \kappa^2 - 2H \kappa + K$.
