---
role: proof
locale: en
of_concept: isomorphism-canonical-line-bundle-over-projective-space
source_book: gtm020
source_chapter: "4"
source_section: "4.8"
---

Let $\lambda$ be the canonical line bundle on $\mathbf{R}P^n$. Recall that the total space of $\lambda$ is
$$E(\lambda) = \{(\pm b, t b) \mid b \in S^n,\; t \in \mathbf{R}\} \subset \mathbf{R}P^n \times \mathbf{R}^{n+1}.$$
The $(n+1)$-fold Whitney sum $(n+1)\lambda$ has total space consisting of tuples $(\pm b, (a_0 b, \ldots, a_n b))$ with $a_i \in \mathbf{R}$.

The map $u \colon (n+1)\lambda \rightarrow \tau(\mathbf{R}P^n) \oplus \theta^1$ is defined by
$$u(\pm b, (a_0 b, \ldots, a_n b)) = (\pm(b, v_b(a_0, \ldots, a_n)), (\pm b, \pi_b(a_0, \ldots, a_n)))$$
where $a = (a_0, \ldots, a_n) \in \mathbf{R}^{n+1}$.

**Well-definedness of $u$:** For the first component, $v_b(a)$ satisfies $(b \mid v_b(a)) = 0$, so $\pm(b, v_b(a))$ is an element of the tangent bundle $\tau(\mathbf{R}P^n)$. For the second component, $\pi_b(a)$ is a real scalar, so $(\pm b, \pi_b(a)) \in E(\theta^1) = \mathbf{R}P^n \times \mathbf{R}$.

The map $v$ is defined by
$$v(\pm b, (x, \pm b, k)) = (\pm b, p_0(x + k b) b, \ldots, p_n(x + k b) b)$$
where $p_i \colon \mathbf{R}^{n+1} \rightarrow \mathbf{R}$ is the $i$-th coordinate projection, $x \in \mathbf{R}^{n+1}$ satisfies $(b \mid x) = 0$ (tangent condition), and $k \in \mathbf{R}$ (trivial line bundle component).

**Well-definedness of $v$:** The vector $x + k b \in \mathbf{R}^{n+1}$ is arbitrary, and each coordinate $p_i(x + k b)$ is a real number. Multiplying by $b$ gives a vector collinear with $b$, so the image lies in $(n+1)\lambda$. To check that $v$ respects the antipodal identification: replacing $(\pm b, (x, \pm b, k))$ by $(\mp b, (-x, \mp b, k))$ yields
$$v(\mp b, (-x, \mp b, k)) = (\mp b, p_0(-x + k(-b))(-b), \ldots, p_n(-x + k(-b))(-b)).$$
Using the relation $-a = -v_b(a) + \pi_b(-a)(-b)$, one verifies the output is the same element of $(n+1)\lambda$.

**Verification that $v \circ u = \text{id}$:** Apply $v$ to $u(\pm b, (a_0 b, \ldots, a_n b))$:
$$v(\pm(b, v_b(a)), (\pm b, \pi_b(a))) = (\pm b, p_0(v_b(a) + \pi_b(a) b) b, \ldots, p_n(v_b(a) + \pi_b(a) b) b).$$
Since $v_b(a) + \pi_b(a) b = a$ by the defining relation of $v_b$ and $\pi_b$, we have
$$p_i(v_b(a) + \pi_b(a) b) = p_i(a) = a_i,$$
so the image is $(\pm b, a_0 b, \ldots, a_n b)$ as required.

**Verification that $u \circ v = \text{id}$:** Similarly follows from the decomposition $x + k b = v_b(x + k b) + \pi_b(x + k b) b$. The relations $a = v_b(a) + \pi_b(a) b$ and $-a = -v_b(a) + \pi_b(-a)(-b)$ ensure the maps are well-defined mutual inverses.
