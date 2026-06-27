---
role: proof
locale: en
of_concept: tangent-hyperplane-yields-face
source_book: gtm015
source_chapter: "36. Extremal points of a convex set; Krein-Mil'man theorem"
source_section: "36"
---

# Proof of Tangent hyperplane yields a face

Let $F = H \cap A$. By the assumptions (30.8), $H$ is tangent to $A$, so $F$ is nonempty. Moreover, $F$ is convex as the intersection of convex sets.

Choose an $\mathbb{R}$-linear form $g$ on $E$ and a real number $\alpha$ such that

$$H = \{x \in E : g(x) = \alpha\}$$

and $g \leq \alpha$ on $A$ (this is the definition of a tangent hyperplane, cf. 30.8).

To show $F$ is a face of $A$, suppose $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap F \neq \varnothing$. We must prove $\langle u, v \rangle \subset F$.

Choose $z \in \langle u, v \rangle \cap F$. Since $z \in \langle u, v \rangle$, there exists $\lambda \in (0, 1)$ such that

$$z = (1 - \lambda)u + \lambda v.$$

Since $z \in F = H \cap A$, we have $g(z) = \alpha$. Meanwhile, $g \leq \alpha$ on $A$, so in particular $g(u) \leq \alpha$ and $g(v) \leq \alpha$. Now

$$\alpha = g(z) = (1 - \lambda)g(u) + \lambda g(v).$$

If either $g(u) < \alpha$ or $g(v) < \alpha$, then

$$(1 - \lambda)g(u) + \lambda g(v) < (1 - \lambda)\alpha + \lambda\alpha = \alpha,$$

a contradiction. Hence $g(u) = g(v) = \alpha$, so $u, v \in H$.

For any point $w \in \langle u, v \rangle$, write $w = (1 - \mu)u + \mu v$ with $\mu \in (0, 1)$. Then

$$g(w) = (1 - \mu)g(u) + \mu g(v) = (1 - \mu)\alpha + \mu\alpha = \alpha,$$

so $w \in H$. Since $\langle u, v \rangle \subset A$ by hypothesis, we have $w \in H \cap A = F$. Thus $\langle u, v \rangle \subset F$, completing the proof that $F$ is a face of $A$. $\square$
