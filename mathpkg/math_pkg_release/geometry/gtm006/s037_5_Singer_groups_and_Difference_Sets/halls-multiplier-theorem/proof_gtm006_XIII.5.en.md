---
role: proof
locale: en
of_concept: halls-multiplier-theorem
source_book: gtm006
source_chapter: "XIII"
source_section: "5"
---

*Proof.* Let $G$ be the abelian Singer group of order $n^2 + n + 1$, let $\mathcal{D}$ be a difference set of $n+1$ elements, and let $F$ be the rational field. Work in the group algebra $FG$, identifying the identities of $F$, $G$, and $FG$. Define the special elements

$$\delta = \sum_{d \in \mathcal{D}} d, \qquad \sigma = \sum_{g \in G} g,$$

and the automorphism $*$ of $FG$ by $(\sum a_x x)^* = \sum a_x x^{-1}$.

The condition that $\mathcal{D}$ is a difference set expresses itself in $FG$ as

$$\delta \delta^* = \delta^* \delta = (n+1) + (\sigma - 1) = n + \sigma. \tag{1}$$

Now let $p$ be a prime divisor of $n$ and define $\phi$ to be the automorphism of $FG$ induced by $x^\phi = x^p$ on $G$. By the binomial theorem in the commutative algebra $FG$:

$$\delta^\phi = \sum_{d \in \mathcal{D}} d^p = \left(\sum_{d \in \mathcal{D}} d\right)^p + p\alpha = \delta^p + p\alpha, \tag{2}$$

where $\alpha$ is an integral element of $FG$ (all coefficients are integers).

Now compute $\delta^\phi \delta^*$ in two ways. On one hand, using (1) and (2):

$$\delta^\phi \delta^* = (\delta^p + p\alpha)\delta^* = \delta^{p-1}(\delta\delta^*) + p\alpha\delta^* = \delta^{p-1}(n+\sigma) + p\alpha\delta^*.$$

Since $\delta\sigma = (n+1)\sigma$, this simplifies to

$$\delta^\phi \delta^* = n\delta^{p-1} + \sigma + p\alpha_2 \tag{3}$$

for some integral element $\alpha_2$.

Multiplying (3) by its image under $*$ and using $\sigma^* = \sigma$, $\sigma^2 = (n^2+n+1)\sigma$, and comparing coefficients yields, after algebraic manipulation,

$$\delta^\phi \delta^* = ng + \sigma = (n+\sigma)g$$

for some group element $g \in G$. Hence, using (1) again,

$$\delta^\phi \delta^* = (n+\sigma)g = (\delta g)\delta^*.$$

Since $\delta^*$ has an inverse in a suitable extension (namely $\beta = 1/n - \sigma/[n(n+1)^2]$ satisfies $(n+\sigma)\beta = 1$, so $\delta\beta$ is an inverse for $\delta^*$), we conclude

$$\delta^\phi = \delta g.$$

The equivalent statement in the group $G$ is $\mathcal{D}^\phi = \mathcal{D}g$. Setting $\lambda = g$ gives the desired result. The mapping $\bar{\phi}$ defined in the statement is then verified to be a collineation normalizing $\Gamma$. $\square$
