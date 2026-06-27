---
role: proof
locale: en
of_concept: subharmonicity-of-diameter-log
source_book: gtm035
source_chapter: "11"
source_section: "11.7"
---
# Proof of Subharmonicity of Log $k$-Diameter

**Theorem 11.7.** For each $g \in A$ and each integer $k \geq 2$, the function

$$\lambda \mapsto \log d_k(g(f^{-1}(\lambda)))$$

is subharmonic on $\Omega$.

*Proof.* For ease of understanding we take $k = 3$. The proof is the same for each $k \geq 2$. By definition,

$$d_3(g(f^{-1}(\lambda))) = \left[\max_{z_1, z_2, z_3 \in g(f^{-1}(\lambda))} |z_1 - z_2| |z_1 - z_3| |z_2 - z_3|\right]^{1/3}.$$

Hence

$$\log d_3(g(f^{-1}(\lambda))) = \frac{1}{3} \log \left[\max_{z_1, z_2, z_3 \in g(f^{-1}(\lambda))} |z_1 - z_2| |z_1 - z_3| |z_2 - z_3|\right].$$

Now the condition $z_j \in g(f^{-1}(\lambda))$ means there exists $x_j \in f^{-1}(\lambda)$ with $g(x_j) = z_j$. So a triple $(z_1, z_2, z_3)$ is admissible exactly when it has the form $(g(x_1), g(x_2), g(x_3))$ with $f(x_j) = \lambda$ for $j = 1, 2, 3$. By Definition 11.3, the triple $(x_1, x_2, x_3) \in X^{(3)}$ if and only if $f(x_1) = f(x_2) = f(x_3)$, and in that case $\pi(x_1, x_2, x_3) = f(x_1)$. Hence

$$\log d_3(g(f^{-1}(\lambda))) = \frac{1}{3} \log \left[\max_{\pi(x_1, x_2, x_3) = \lambda} |g(x_1) - g(x_2)| |g(x_1) - g(x_3)| |g(x_2) - g(x_3)|\right].$$

Define, for $(x_1, x_2, x_3) \in X^{(3)}$,

$$G(x_1, x_2, x_3) = (g(x_1) - g(x_2))(g(x_1) - g(x_3))(g(x_2) - g(x_3)).$$

Then $G \in A^{(3)}$, since $A^{(3)}$ is the restriction of $\otimes^3 A$ to $X^{(3)}$ and $G$ is a polynomial in the coordinate functions $g(x_1), g(x_2), g(x_3)$. We have

$$\log d_3(g(f^{-1}(\lambda))) = \frac{1}{3} \log \left[\max_{\pi(x_1, x_2, x_3) = \lambda} |G(x_1, x_2, x_3)|\right] = \frac{1}{3} \log Z_G(\lambda).$$

By Theorem 11.6, $(A^{(3)}, X^{(3)}, \Omega, \pi)$ is a maximum modulus algebra. Applying Theorem 11.3 to this algebra and the function $G \in A^{(3)}$, we conclude that $\log Z_G$ is subharmonic on $\Omega$. Therefore $\log d_3(g(f^{-1}(\lambda))) = \frac{1}{3} \log Z_G(\lambda)$ is subharmonic on $\Omega$.

The argument for general $k$ is identical, using $X^{(k)}$ and $A^{(k)}$ in place of $X^{(3)}$ and $A^{(3)}$, and defining $G$ as the product of all differences $(g(x_i) - g(x_j))$ for $i < j$, which again belongs to $A^{(k)}$. $\square$
