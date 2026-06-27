---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a vector space over $\mathbb{K}$ and let $A$ be a nonempty convex subset of $E$. Suppose $H$ is an $\mathbb{R}$-hyperplane of $E$ that is **tangent** to $A$; that is, $H \cap A \neq \varnothing$ and $A$ lies entirely on one side of $H$. Then the intersection $F = H \cap A$ is a face of $A$.

The proof uses the analytic description of a tangent hyperplane. Choose an $\mathbb{R}$-linear form $g$ on $E$ and a real number $\alpha$ such that $H = \{x : g(x) = \alpha\}$ and $g \leq \alpha$ on $A$ (this is the sense in which $H$ is tangent — $A$ lies in the closed half-space $\{g \leq \alpha\}$). Then $F$ is nonempty and convex. To verify the face condition, suppose $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap F \neq \varnothing$. Choose $z \in \langle u, v \rangle \cap F$, so $z = (1-\nu)u + \nu v$ with $0 < \nu < 1$ and $g(z) = \alpha$. Since $g(u) \leq \alpha$ and $g(v) \leq \alpha$, the equality $\alpha = g(z) = (1-\nu)g(u) + \nu g(v)$ forces $g(u) = g(v) = \alpha$. Consequently, every point of $\langle u, v \rangle$ has $g$-value $\alpha$, so $\langle u, v \rangle \subset H \cap A = F$.

This proposition provides a crucial bridge between the geometric notion of supporting hyperplanes and the algebraic notion of faces. In the proof of the Krein-Mil'man theorem, it guarantees that the family of closed faces contained in a given tangent hyperplane is nonempty, initiating the Zorn's lemma minimality argument.
