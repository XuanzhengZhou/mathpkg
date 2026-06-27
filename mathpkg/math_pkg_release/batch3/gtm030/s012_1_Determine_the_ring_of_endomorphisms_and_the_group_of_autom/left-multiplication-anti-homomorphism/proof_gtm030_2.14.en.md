---
role: proof
locale: en
of_concept: left-multiplication-anti-homomorphism
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

For any $x, a, b \in \mathfrak{A}$, we compute using the left distributive law and associativity:

$$x(a + b)_l = (a + b)x = ax + bx = x a_l + x b_l = x(a_l + b_l).$$

Since this holds for all $x$, we obtain $(a + b)_l = a_l + b_l$.

For multiplication, note that

$$x(ab)_l = (ab)x = a(bx) = a(x b_l) = (x b_l) a_l = x(b_l a_l).$$

Thus $(ab)_l = b_l a_l$. This establishes that $a \mapsto a_l$ is an anti-homomorphism of $\mathfrak{A}$ into the endomorphism ring $\mathfrak{E}$, since it preserves addition but reverses multiplication.
