---
role: proof
locale: en
of_concept: maximum-principle-harmonic-first
source_book: gtm011
source_chapter: "X"
source_section: "1.6"
---

Let $A = \{z \in G : u(z) = u(a)\}$ where $a \in G$ is a point such that $u(a) \geq u(z)$ for all $z \in G$. Since $u$ is continuous, $A$ is closed in $G$. To show $A$ is open, let $z_0 \in A$ and choose $r > 0$ such that $B(z_0; r) \subset G$. If $z_0$ were not an interior point of $A$, then for some $\rho$ with $0 < \rho < r$ there would exist a point $z_0 + \rho e^{i\beta}$ such that $u(z_0 + \rho e^{i\beta}) < u(z_0)$. By continuity, there is a proper interval $I$ of $[0, 2\pi]$ such that $\beta \in I$ and $u(z_0 + \rho e^{i\theta}) < u(z_0)$ for all $\theta$ in $I$. Hence, by the MVP

$$u(z_0) = \frac{1}{2\pi} \int_0^{2\pi} u(z_0 + \rho e^{i\theta}) \, d\theta < u(z_0),$$

a contradiction. So $B(z_0; r) \subset A$ and $A$ is also open. By the connectedness of $G$, $A = G$, which implies $u$ is constant on $G$.
