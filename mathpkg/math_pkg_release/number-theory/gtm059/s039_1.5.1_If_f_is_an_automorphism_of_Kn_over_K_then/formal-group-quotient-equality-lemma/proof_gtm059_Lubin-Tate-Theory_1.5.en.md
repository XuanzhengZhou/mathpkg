---
role: proof
locale: en
of_concept: formal-group-quotient-equality-lemma
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* The inclusion $\supseteq$ is obvious. We prove the reverse inclusion. Let $x \in A_n(\mathfrak{a})[\pi_1]^n[\mathfrak{a}]^n$ and write $x = x_1 + x_2$ with $x_1 \in A_n(\mathfrak{a})[\pi_1]^n$ and $x_2 \in [\mathfrak{a}]^n A_n(\mathfrak{a})$. Then $\mathfrak{a} = x_1 + x_2$ and applying the endomorphism $[\pi_2]$ yields the desired membership. The argument uses the fact that $[\pi_2] \circ [\pi_1]^{-1}$ has integral coefficients when $\mathfrak{a} \neq \mathfrak{p}$, so the module structure is preserved under change of prime element.

As consequences of the lemma, we obtain inclusions of the form:

$$A(\pi^0)^*(u_1) \leq [\pi^0]^*(u_1),$$
$$A(\pi^0)^*(u_2) \leq [\pi^0]^*(u_2),$$

where the second inclusion follows from taking $k = g^{q-1} = 1$.
