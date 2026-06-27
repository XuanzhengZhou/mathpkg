---
role: proof
locale: en
of_concept: rank-function-in-boolean-valued-universe
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

**1.** By the definition of the Boolean embedding $\check{\alpha}$, one computes directly that $\llbracket u \in R(\check{\alpha}) \rrbracket$ equals the sum over $V_\alpha^{(\mathbf{B})}$ of $\llbracket u = v \rrbracket$. This in turn equals the truth value of $u$ belonging to the set $V_\alpha^{(\mathbf{B})} \times \{1\}$ (the set whose elements are the members of $V_\alpha^{(\mathbf{B})}$, each with truth value $1$). Hence $\llbracket R(\check{\alpha}) = V_\alpha^{(\mathbf{B})} \times \{1\} \rrbracket = 1$.

**2.** If $\mathcal{D}(u) \subseteq V_\alpha^{(\mathbf{B})}$, then for each $x \in \mathcal{D}(u)$, part 1 gives $\llbracket x \in R(\check{\alpha}) \rrbracket = 1$. Thus
$$\llbracket u \subseteq R(\check{\alpha}) \rrbracket = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow \llbracket x \in R(\check{\alpha}) \rrbracket) = \prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow 1) = 1.$$

**3.** This follows from part 1 and Theorem 16.25 applied with $u = R(\check{\alpha})$.
