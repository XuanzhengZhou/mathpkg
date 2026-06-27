---
role: exercise
locale: en
chapter: "Chapter 17"
section: "17.6"
exercise_number: 17.3
---
# Exercise 17.3

Let $\Sigma$ be a smooth submanifold of $\mathbb{C}^n$ and let $T$ be the tangent space to $\Sigma$ at a point $z_0 \in \Sigma$. Let

$$d(z) = \operatorname{dist}(z, \Sigma), \qquad d(z, T) = \operatorname{dist}(z, T).$$

Show the asymptotic expansion

$$d^2(z) = d^2(z, T) + o(|z - z_0|^2)$$

as $z \to z_0$. Also show that

$$d^2(z, T) = H(z - z_0) + \operatorname{Re} A(z - z_0),$$

where $H(w) = \sum_{j,k=1}^{n} h_{jk} w_j \bar{w}_k$ is a Hermitian-symmetric quadratic form and $A$ is a homogeneous quadratic polynomial in $w$.

Conclude that

$$\sum_{j,k=1}^{n} \frac{\partial^2(d^2)}{\partial z_j \partial \bar{z}_k}(z_0) \, w_j \bar{w}_k = H(w).$$
