---
role: proof
locale: en
of_concept: existence-of-nonzero-represented-elements
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

Assume the conclusion is false, so $g(u, u) = 0$ for all $u \in \Re$. Then for all $x, y \in \Re$,

$$g(x, y) + g(y, x) = g(x + y, x + y) - g(x, x) - g(y, y) = 0.$$

Since $g(y, x) = \overline{g(x, y)}$ (hermitian property), this yields $\overline{g(x, y)} = -g(x, y)$ for all $x, y$.

Now $g \neq 0$, so there exist vectors $u, v$ such that $\rho = g(u, v) \neq 0$. Replacing $u$ by $\rho^{-1}u$ and renaming, we may assume $g(u, v) = 1$.

Then for any $\alpha \in \Delta$,

$$\overline{g(\alpha u, v)} = \overline{\alpha \, g(u, v)} = \overline{\alpha} \cdot \overline{1} = \overline{\alpha}.$$

But also $\overline{g(\alpha u, v)} = -g(\alpha u, v) = -\alpha$. Hence $\overline{\alpha} = -\alpha$ for all $\alpha \in \Delta$.

In the symmetric case ($\overline{\alpha} = \alpha$), this gives $\alpha = -\alpha$ for all $\alpha$, so $2\alpha = 0$ and the characteristic of $\Delta = \Phi$ is $2$, contradicting our assumption that $\operatorname{char} \Phi \neq 2$. For a general hermitian product with non-identity anti-automorphism, the condition $\overline{\alpha} = -\alpha$ for all $\alpha$ implies the anti-automorphism coincides with $-\mathrm{id}$, which is impossible for an involution unless $\operatorname{char} = 2$. Thus the assumption $g(u, u) = 0$ for all $u$ leads to a contradiction, and the lemma follows.
