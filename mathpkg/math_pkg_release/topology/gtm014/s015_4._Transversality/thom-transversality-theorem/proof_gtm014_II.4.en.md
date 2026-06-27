---
role: proof
locale: en
of_concept: thom-transversality-theorem
source_book: gtm014
source_chapter: "II"
source_section: "4. Transversality"
---

We will use Corollary 4.8 to show that $f$ can be perturbed slightly to be transversal to $\overline{W_{r}}$. The perturbation will be accomplished locally using the data defined in the previous paragraph. Let $B'$ be the space of polynomial mappings of $\mathbf{R}^{n} \to \mathbf{R}^{m}$ of degree $k$. For $b$ in $B'$, define $g_{b}: X \to Y$ by

$$g_{b}(x) = \begin{cases} f(x) & \text{if } x \notin U_{r} \text{ or } f(x) \notin V_{r} \\ \eta^{-1}\big(\rho(\psi(x))\,\rho'(\eta f(x))\,b(\psi(x)) + \eta f(x)\big) & \text{otherwise.} \end{cases}$$

The choice of $\rho$ and $\rho'$ guarantees that $g_{b}$ is a smooth function from $X$ to $Y$ and is just a polynomial perturbation of $f$ done locally and smoothed out so that it is equal to $f$ off the domain.

$\Phi: X \times B \to J^{k}(X, Y)$ is locally a diffeomorphism near $(x, b)$. For let $\sigma$ be in $J^{k}(X, Y)$ near $\Phi(x, b)$, let $x' = \alpha(\sigma)$, and let $b'$ be the unique polynomial mapping of degree $\leq k$ such that $\sigma = j^{k}(\eta(b' \cdot \psi + \eta \cdot f))(x')$. Then $\sigma \mapsto (b', x')$ is a smooth mapping and is the inverse of $\Phi$.
