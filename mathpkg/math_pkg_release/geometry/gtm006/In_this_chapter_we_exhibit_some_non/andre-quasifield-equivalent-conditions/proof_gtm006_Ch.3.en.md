---
role: proof
locale: en
of_concept: andre-quasifield-equivalent-conditions
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

$(i) \Rightarrow (iv)$: Suppose $F_\phi$ is a division ring. Then the right distributive law holds. For all $a, b, x \in F^*$ we have
\[
a x^{\alpha_a} + b x^{\alpha_b} = (a+b) x^{\alpha_{a+b}} \tag{1}
\]
where $\alpha_x = \nu(x)\phi(\nu(x))$. Regarding $a$ and $b$ as fixed, (1) is an identity in $x$. Replacing $x$ by $xy$:
\[
a x^{\alpha_a} y^{\alpha_a} + b x^{\alpha_b} y^{\alpha_b} = (a+b)(x^{\alpha_{a+b}} y^{\alpha_{a+b}}) = [(a+b)x^{\alpha_{a+b}}] y^{\alpha_{a+b}}. \tag{2}
\]

Using (1), equation (2) becomes:
\[
a x^{\alpha_a} y^{\alpha_a} + b x^{\alpha_b} y^{\alpha_b} = a x^{\alpha_a} y^{\alpha_{a+b}} + b x^{\alpha_b} y^{\alpha_{a+b}}.
\]

Since this holds for all $x$, comparing terms forces $\alpha_a = \alpha_b = \alpha_{a+b}$ for all $a, b \in F^*$, which implies $\alpha$ is constant. Since $\alpha_1 = \varepsilon$, we have $\alpha_x = \varepsilon$ for all $x$, and thus $k^\phi = \varepsilon$ for all $k \in N$.

$(iv) \Rightarrow (iii)$: If $k^\phi = \varepsilon$ for all $k \in N$, then $\alpha_x = \nu(x)$ and the multiplication becomes $x \odot y = x y^{\nu(x)}$. The map $x \mapsto x$ is an isomorphism between $F$ and $F_\phi$, as can be verified directly.

$(iii) \Rightarrow (ii) \Rightarrow (i)$ are immediate. $\square$
