---
role: proof
locale: en
of_concept: pairing-kernel-isomorphism-theorem
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* By Theorem 5.2 we have determined the order of

$$A_1(A_1) / K^\times(A_1) = A_1(A_1).$$

It is a standard result of local algebraic number theory (see e.g., [1], Chapter II, §3) that

$$\operatorname{order of } K^\times / K^{\times p^n} = (d(A_1)) \cdot [\mathfrak{m}^{p^n} A_1] / p^n,$$

where $p$ is the order of the group of $p$-power roots of unity in $K$. If $K(A_1)$ does not contain the $p$-th roots of unity, then

$$K^\times / K^{\times p^n} \cong A_1(A_1)$$

has the same order as $A_1(A_1) = [\mathfrak{m}^{p^n} A_1]$. We know that the kernel on the left of the pairing is invariant. Since $A_1$ is cyclic, it follows by the duality of finite abelian groups that the kernel on the right of the pairing must be identical to the kernel on the left.

**Remark.** When the $p$-th roots of unity are contained in $K$, in particular when $A_1 = G_1$, the above argument shows that the kernel on the right is an isomorphism

$$\lambda: A \xrightarrow{\sim} G_a$$

with the additive group, i.e., a power series with coefficients in some extension of $K$.
