---
role: proof
locale: en
of_concept: lambda-is-xi-power
source_book: gtm026
source_chapter: "4"
source_section: "1"
---

*Proof.* Let $g: 1 \longrightarrow 1T$ and $x: 1 \longrightarrow X$ be arbitrary elements. Using 1.5.8, 1.5.6, and 1.4.13,

$$\langle x, \xi^g \rangle = \langle x, 1\hat{g}.\xi \rangle = \langle g, xT.\xi \rangle = \langle g, x^{\#} \rangle.$$

As $\langle 1\eta, x^{\#} \rangle = x = \langle \mathrm{id}_X, \mathrm{pr}_x \rangle$ (where $\mathrm{pr}_x: E(X, \xi) \longrightarrow (X, \xi)$ is the restricted projection) $= \langle 1\eta, \lambda.\mathrm{pr}_x \rangle$, we have $x^{\#} = \lambda.\mathrm{pr}_x$. Thus

$$x\langle g, \lambda \rangle = \langle g, \lambda.\mathrm{pr}_x \rangle = \langle g, x^{\#} \rangle = x\xi^g.$$

Since $x$ was arbitrary, $\langle g, \lambda \rangle = \xi^g$, which is precisely the statement that $\lambda(g) = \xi^g$. $\square$
