---
role: proof
locale: en
of_concept: conditional-inequalities
source_book: gtm046
source_chapter: "VIII"
source_section: "28.1"
---

**Proof.** Upon replacing $E$ by $E^\mathfrak{B}$, the $c_r$-, Minkowski and Hölder inequalities, as well as their consequences and the inequalities for convex functions, remain valid almost surely. 

The reason is that, on account of the linearity of $E^\mathfrak{B}$ (property 1 of §28.1), the proofs of these inequalities remain valid up to a $P^\mathfrak{B}$-equivalence. For Hölder's inequality, one additionally uses property 25.2.3 (the commutation of $E^\mathfrak{B}$ with $\mathfrak{B}$-measurable functions).

Specifically, for any $r \geq 1$, the conditional $c_r$-inequality states

$$E^\mathfrak{B}|X + Y|^r \leq c_r (E^\mathfrak{B}|X|^r + E^\mathfrak{B}|Y|^r) \quad \text{a.s.}$$

The conditional Hölder inequality: for $p, q > 1$ with $1/p + 1/q = 1$,

$$E^\mathfrak{B}|XY| \leq (E^\mathfrak{B}|X|^p)^{1/p} (E^\mathfrak{B}|Y|^q)^{1/q} \quad \text{a.s.}$$

The conditional Minkowski inequality: for $r \geq 1$,

$$(E^\mathfrak{B}|X + Y|^r)^{1/r} \leq (E^\mathfrak{B}|X|^r)^{1/r} + (E^\mathfrak{B}|Y|^r)^{1/r} \quad \text{a.s.}$$

And for a convex function $\varphi$, Jensen's inequality for conditional expectations:

$$\varphi(E^\mathfrak{B}X) \leq E^\mathfrak{B}\varphi(X) \quad \text{a.s.}$$

All hold because the standard proofs only involve algebraic manipulations, monotonicity, and linearity of the integral, which carry over to $E^\mathfrak{B}$ almost surely.
