---
role: proof
locale: en
of_concept: poisson-kernel-dirichlet-problem
source_book: gtm012
source_chapter: "5"
source_section: "6. Laplace's equation and the Dirichlet problem"
---

# Proof of Solution of the Dirichlet Problem via the Poisson Kernel

**Theorem 6.1.** Suppose $F$ is a periodic distribution. There is a unique function $u(r, \theta)$ defined and smooth in the open unit disc, satisfying (3), and such that the distributions defined by the functions $u_r(\theta) = u(r, \theta)$ converge to $F$ in the sense of $\mathcal{P}'$ as $r \to 1$. Moreover, if $F = F_g$ where $g \in \mathcal{C}$, then $u_r \to g$ uniformly as $r \to 1$. The functions $u_r$ are given by convolution with the Poisson kernel:

$$u_r = F * P_r.$$

*Proof.* Uniqueness was proved in the derivation above. Let $u_r = F * P_r$. Since $P_r$ is an approximate identity, we do have $u_r \to F$ (in $\mathcal{P}'$) as $r \to 1$, and $u_r \to g$ uniformly if $F = F_g$, $g \in \mathcal{C}$. We must show that $u$ is smooth and satisfies (3). Note that when $F = F_g$, $g \in \mathcal{C}$, then explicitly

$$u(r, \theta) = \frac{1}{2\pi} \int_0^{2\pi} P(r, \theta - \varphi) g(\varphi) \, d\varphi$$

and we may differentiate under the integral sign to prove that $u$ is smooth. Moreover, since $P(r, \theta)$ satisfies (3), so does $u$.

Finally, suppose $u$ has merely a distribution $F$ as its value on the boundary. Note that if $0 \leq r, s < 1$ then (by computing Fourier coefficients, for example)

$$P_r * P_s = P_{rs}.$$

In particular, choose any $R > 0$, $R < 1$. It suffices to show that $u$ is smooth in the disc $r < R$ and satisfies (3) there. But when $r < R$,

$$s = rR^{-1} < 1$$

and

$$u_r = F * P_r = F * (P_R * P_s) = (F * P_R) * P_s.$$

Now $F * P_R$ is the smooth function $u_R$. Therefore $u$ near the disc of radius $r$ is obtained by convolving a smooth function with the Poisson kernel $P_s$, and the argument above for the case $F = F_g$ with $g$ continuous applies. Hence $u$ is smooth and harmonic. $\square$
