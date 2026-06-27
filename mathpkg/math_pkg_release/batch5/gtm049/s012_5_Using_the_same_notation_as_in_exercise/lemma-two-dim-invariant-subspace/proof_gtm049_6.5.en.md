---
role: proof
locale: en
of_concept: lemma-two-dim-invariant-subspace
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

Let $c = a + ib$ be the eigenvector with $cf = e^{i\theta}c$. Then

$$\sigma'(c, c) = \sigma'(cf, cf) = e^{2i\theta}\sigma'(c, c)$$

and therefore $\sigma'(c, c) = 0$ because $e^{2i\theta} \neq 1$ (since $\theta$ is not an integer multiple of $\pi$, the eigenvalue being non-real). Expanding:

$$0 = \sigma'(a + ib, a + ib) = \sigma(a, a) - \sigma(b, b) + 2i\sigma(a, b).$$

Thus $\sigma(a, a) = \sigma(b, b)$ and $\sigma(a, b) = 0$. Since $c \neq 0$, we have $\sigma(a, a) = \sigma(b, b) > 0$. 

Set $u = a / \sqrt{\sigma(a, a)}$ and $v = b / \sqrt{\sigma(b, b)}$. Then $(u, v)$ is a cartesian basis of $T = [a, b]$, the real subspace spanned by $a$ and $b$.

From $cf = e^{i\theta}c$ we obtain $(a + ib)f = (\cos\theta + i\sin\theta)(a + ib)$. Separating real and imaginary parts:

$$af = \cos\theta \cdot a - \sin\theta \cdot b,$$
$$bf = \sin\theta \cdot a + \cos\theta \cdot b.$$

Thus $Tf = T$ and with respect to $(u, v)$, $f$ has the required rotation matrix.
