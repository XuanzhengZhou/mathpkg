---
role: proof
locale: en
of_concept: chevalley-basis
source_book: gtm009
source_chapter: "VII"
source_section: "25.2"
---

**Proof.** Recall (Proposition 14.3) that $L$ possesses an automorphism $\sigma$ of order $2$ sending $L_{\alpha}$ to $L_{-\alpha}$ ($\alpha \in \Phi$) and acting on $H$ as multiplication by $-1$. For arbitrary nonzero $x_{\alpha} \in L_{\alpha}$, $x_{-\alpha} = -\sigma(x_{\alpha}) \in L_{-\alpha}$ is nonzero, and $\kappa(x_{\alpha}, x_{-\alpha}) \neq 0$ ($\kappa$ the Killing form). Replacing $x_{\alpha}$ by $c x_{\alpha}$ ($c \in F$) multiplies this value by $c^2$. Since $F$ is algebraically closed, it is therefore possible to modify the choice so that $\kappa(x_{\alpha}, x_{-\alpha})$ takes any prescribed nonzero value. We specify $\kappa(x_{\alpha}, x_{-\alpha}) = \frac{2}{(\alpha, \alpha)}$. According to Proposition 8.3(c), this forces $[x_{\alpha} x_{-\alpha}] = h_{\alpha} = \frac{2t_{\alpha}}{(\alpha, \alpha)}$. For each pair of roots $\{\alpha, -\alpha\}$ we fix such a choice of $\{x_{\alpha}, x_{-\alpha}\}$, so (a) is satisfied.

Now let $\alpha, \beta, \alpha + \beta \in \Phi$, so $[x_{\alpha}x_{\beta}] = c_{\alpha\beta} x_{\alpha+\beta}$ for some $c_{\alpha\beta} \in F$. Applying $\sigma$ to this equation, we get $[-x_{-\alpha}, -x_{-\beta}] = -c_{\alpha\beta} x_{-\alpha-\beta}$. On the other hand, $[x_{-\alpha}x_{-\beta}] = c_{-\alpha,-\beta} x_{-\alpha-\beta}$. Therefore $c_{\alpha\beta} = -c_{-\alpha,-\beta}$. This establishes the sign relation in part (b) of the theorem.

The proof that the structure constants $c_{\alpha\beta}$ are integers (specifically $\pm(r+1)$) uses the representation theory of the three-dimensional simple subalgebra $S_{\alpha} \cong \mathfrak{sl}(2, F)$. For each $\alpha \in \Phi$, the elements $x_{\alpha}, x_{-\alpha}, h_{\alpha}$ span a copy of $\mathfrak{sl}(2, F)$. The $\alpha$-string through $\beta$ is a weight string for the action of $S_{\alpha}$, and the representation theory of $\mathfrak{sl}(2, F)$ (specifically Lemma 25.1 and Proposition 25.1(c)) yields:

$$c_{\alpha\beta}^2 = q(r+1) \frac{(\alpha+\beta, \alpha+\beta)}{(\beta, \beta)}.$$

Combined with part (c) of Proposition 25.1, which states that $r+1 = \frac{q(\alpha+\beta, \alpha+\beta)}{(\beta, \beta)}$ when $\alpha+\beta \in \Phi$, we obtain $c_{\alpha\beta}^2 = (r+1)^2$, hence $c_{\alpha\beta} = \pm(r+1)$. This proves the integrality of the structure constants.

As to (c), recall that the dual roots $\alpha' = \frac{2\alpha}{(\alpha, \alpha)}$ form a root system, with base $\Delta' = \{\alpha_1', \ldots, \alpha_l'\}$ (Exercise 10.1). Under the Killing form identification of $H$ with $H^*$, $t_{\alpha}$ corresponds to $\alpha$ and $h_{\alpha}$ to $\alpha'$. Since each $\alpha'$ is a $\mathbb{Z}$-linear combination of $\Delta'$, each $h_{\alpha}$ is a $\mathbb{Z}$-linear combination of $h_1, \ldots, h_l$. Finally, (d) follows from part (c) of the preceding proposition, combined with part (c) of Proposition 25.1.

It may seem strange that we have required $c_{\alpha\beta} = -c_{-\alpha, -\beta}$ rather than $c_{\alpha\beta} = c_{-\alpha, -\beta}$ in the definition of a Chevalley basis. However, this asymmetry is inevitable: given condition (a) of the proposition, it can be shown by skillful use of the Jacobi identity that $c_{\alpha\beta}c_{-\alpha, -\beta} = -(r+1)^2$, which implies that condition (d) of the theorem could not hold unless we had condition (b) of the proposition. (This was Chevalley's original line of argument.)
