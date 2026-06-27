---
role: proof
locale: en
of_concept: rotation-block-from-nonreal-eigenvalue
source_book: gtm049
source_chapter: "VI"
source_section: "6.4"
---
Let $$c = a + ib$$ be an eigenvector with non-real eigenvalue $$e^{i\theta}$$. Then
$$\sigma(c, c) = \sigma(cf, cf) = e^{2i\theta}\sigma(c, c),$$
so $$\sigma(c, c) = 0$$ because $$e^{2i\theta} \neq 1$$. This gives
$$\sigma(a, a) - \sigma(b, b) + 2i\sigma(a, b) = 0,$$
hence $$\sigma(a, a) = \sigma(b, b)$$ and $$\sigma(a, b) = 0$$. Moreover, $$\sigma(a, a) > 0$$ (otherwise $$a = b = 0$$, contradicting $$c \neq 0$$).

Set $$u = a / \sqrt{\sigma(a,a)}$$ and $$v = b / \sqrt{\sigma(b,b)}$$. Then $$(u, v)$$ is a Cartesian basis of the subspace $$T = [a, b]$$. From $$(a+ib)f = e^{i\theta}(a+ib) = (\cos\theta + i\sin\theta)(a+ib)$$, equating real and imaginary parts gives:
$$af = a\cos\theta - b\sin\theta, \quad bf = a\sin\theta + b\cos\theta.$$
In the basis $$(u, v)$$, this yields the rotation matrix $$(f; (u, v)) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$, and clearly $$Tf = T$$.
