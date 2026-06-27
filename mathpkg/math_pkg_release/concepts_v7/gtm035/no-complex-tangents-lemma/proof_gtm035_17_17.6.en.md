---
role: proof
locale: en
of_concept: no-complex-tangents-lemma
source_book: gtm035
source_chapter: "Chapter 17"
source_section: "17.6"
---
# Proof of No Complex Tangents Lemma

**Lemma 17.2.** Let $\Sigma$ be a $k$-dimensional sufficiently smooth submanifold of an open set in $\mathbb{C}^n$. Assume that $\Sigma$ has no complex tangents. Then the squared distance function

$$d^2(z) = \operatorname{dist}(z, \Sigma)^2$$

is strongly plurisubharmonic in a neighborhood of $\Sigma$.

*Proof.* Let $U$ be a neighborhood of $\Sigma$ such that $d^2 \in C^2(U)$. Fix $z_0 \in \Sigma$. We assert that

$$\sum_{j,k=1}^{n} \frac{\partial^2(d^2)}{\partial z_j \partial \bar{z}_k} (z_0) \xi_j \bar{\xi}_k > 0$$

for all $\xi = (\xi_1, \ldots, \xi_n)$ with $\xi \neq 0$.

Without loss of generality $z_0 = 0$. Let $T$ be the tangent space to $\Sigma$ at $0$ and put $d(z, T) = \operatorname{dist}(z, T)$, the distance from $z$ to $T$. One can show that

$$d^2(z) = d^2(z, T) + o(|z|^2).$$

Also

$$d^2(z, T) = H(z) + \operatorname{Re} A(z),$$

where $H(z) = \sum_{j,k=1}^{n} h_{jk} z_j \bar{z}_k$ is Hermitian-symmetric and $A$ is a homogeneous quadratic polynomial in $z$.

These equations imply that

$$\sum_{j,k=1}^{n} \frac{\partial^2(d^2)}{\partial z_j \partial \bar{z}_k} (0) z_j \bar{z}_k = H(z).$$

Now

$$d^2(z, T) + d^2(iz, T) = 2H(z).$$

If $z \neq 0$, either $z$ or $iz \notin T$, since by hypothesis $T$ contains no complex line. Hence $H(z) > 0$. This shows that the Levi form is positive definite at each point.

It follows by continuity that

$$\sum_{j,k} \frac{\partial^2(d^2)}{\partial z_j \partial \bar{z}_k} \xi_j \bar{\xi}_k \geq c |\xi|^2$$

for some positive constant $c > 0$ in a neighborhood of $\Sigma$. Thus $d^2$ is strongly plurisubharmonic in that neighborhood. $\square$
