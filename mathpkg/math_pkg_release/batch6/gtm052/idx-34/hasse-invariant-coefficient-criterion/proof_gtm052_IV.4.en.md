---
role: proof
locale: en
of_concept: hasse-invariant-coefficient-criterion
source_book: gtm052
source_chapter: "IV"
source_section: "4"
---
Let $X$ be embedded in $\mathbf{P}^2$ with equation $f(x,y,z) = 0$. Let $P = \mathbf{P}^2$ and consider the exact sequence

$$0 \to \mathcal{O}_P(-3) \xrightarrow{f} \mathcal{O}_P \to \mathcal{O}_X \to 0.$$

The long exact cohomology sequence yields an isomorphism

$$H^1(X, \mathcal{O}_X) \xrightarrow{\sim} H^2(P, \mathcal{O}_P(-3)).$$

The Frobenius morphism $F: X \to X$ induces a commutative diagram

$$H^1(X, \mathcal{O}_X) \xrightarrow{\sim} H^2(\mathbf{P}^2, \mathcal{O}_P(-3))$$
$$F^* \downarrow \qquad\qquad\qquad\qquad F_1^* \downarrow$$
$$H^1(X^{(p)}, \mathcal{O}_{X^{(p)}}) \xrightarrow{\sim} H^2(\mathbf{P}^2, \mathcal{O}_P(-3p))$$
$$\downarrow \qquad\qquad\qquad\qquad \downarrow$$
$$H^1(X, \mathcal{O}_X) \xrightarrow{\sim} H^2(\mathbf{P}^2, \mathcal{O}_P(-3))$$

where the vertical maps on the left compose to give $F^*$ on $H^1(X, \mathcal{O}_X)$, and $F_1^*$ on the right is induced by the Frobenius on $\mathbf{P}^2$.

Now $H^2(\mathbf{P}^2, \mathcal{O}_P(-3))$ has a basis consisting of the class of $(xyz)^{-1}$, computed via Čech cohomology. The map $F_1^*$ sends $(xyz)^{-1}$ to $(xyz)^{-p}$ in $H^2(\mathbf{P}^2, \mathcal{O}_P(-3p))$.

To map this back to $H^2(\mathbf{P}^2, \mathcal{O}_P(-3))$, one multiplies by the equation $f^{p-1}$ (this comes from the fact that the diagram uses the $(p-1)$-st power of the defining equation to compensate for the difference between $\mathcal{O}_P(-3p)$ and $\mathcal{O}_P(-3)$). Thus the image of $(xyz)^{-p}$ in $H^2(\mathcal{O}_P(-3))$ is $f^{p-1} \cdot (xyz)^{-p}$.

In the Čech cohomology computation, $H^2(\mathcal{O}_P(-3))$ has basis $(xyz)^{-1}$, and any monomial having a nonnegative exponent on $x$, $y$, or $z$ is cohomologous to $0$. Therefore, when we expand $f^{p-1} \cdot (xyz)^{-p}$, the only term that survives in cohomology is the one where the exponent of $(xyz)^{-p}$ is cancelled, i.e., the coefficient of $(xyz)^{p-1}$ in $f^{p-1}$ multiplied by $(xyz)^{-1}$.

Thus $F^*$ on $H^1(X, \mathcal{O}_X)$ is zero precisely when this coefficient vanishes, which by definition means the Hasse invariant is $0$.
