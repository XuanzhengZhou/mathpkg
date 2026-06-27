---
role: proof
locale: en
of_concept: isomorphism-tangent-normal-bundle-on-sphere
source_book: gtm020
source_chapter: "4"
source_section: "4.7"
---

The map $u \colon \tau(S^n) \oplus \nu(S^n) \rightarrow \theta^{n+1}$ is defined by
$$u((b, x), (b, x')) = (b, x + x')$$
where $(b, x) \in E(\tau(S^n))$ (so $x \in \mathbf{R}^{n+1}$ with $(b \mid x) = 0$) and $(b, x') \in E(\nu(S^n))$ (so $x' = t b$ for some $t \in \mathbf{R}$). The sum $x + x'$ is an arbitrary vector in $\mathbf{R}^{n+1}$, and the image lies in the total space of $\theta^{n+1} = (S^n \times \mathbf{R}^{n+1}, \text{pr}_1, S^n)$.

The inverse $B$-morphism $v \colon \theta^{n+1} \rightarrow \tau(S^n) \oplus \nu(S^n)$ is defined by
$$v(b, x) = ((b, v_b(x)), (b, \pi_b(x) b))$$
where $v_b(x) = x - \pi_b(x) b$ and $\pi_b(x) = (b \mid x)/(b \mid b)$. By construction, $(b \mid v_b(x)) = 0$, so $(b, v_b(x)) \in E(\tau(S^n))$, and $\pi_b(x) b$ is a scalar multiple of $b$, so $(b, \pi_b(x) b) \in E(\nu(S^n))$.

To verify $v \circ u = \text{id}$: for $(b, x) \in E(\tau(S^n))$ and $(b, x') \in E(\nu(S^n))$,
$$v(u((b, x), (b, x'))) = v(b, x + x').$$
Since $x' = t b$ for some $t$, we have $x + x' = x + t b$. Then
$$\pi_b(x + t b) = \frac{(b \mid x + t b)}{(b \mid b)} = \frac{(b \mid x) + t(b \mid b)}{(b \mid b)} = t,$$
because $(b \mid x) = 0$. Hence
$$v_b(x + t b) = (x + t b) - t b = x,$$
and thus $v(b, x + x') = ((b, x), (b, t b)) = ((b, x), (b, x'))$.

To verify $u \circ v = \text{id}$: for $(b, x) \in S^n \times \mathbf{R}^{n+1}$,
$$u(v(b, x)) = u((b, v_b(x)), (b, \pi_b(x) b)) = (b, v_b(x) + \pi_b(x) b) = (b, x),$$
since $x = v_b(x) + \pi_b(x) b$ by the defining relation of the normal map and projection.

Both $u$ and $v$ are continuous and commute with the projections to $S^n$, hence they are $B$-morphisms. Therefore $u$ is a bundle isomorphism with inverse $v$.
