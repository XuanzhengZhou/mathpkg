---
role: proof
locale: en
of_concept: thm-18-4-riesz-representation
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

All that is really necessary is to show that there exists a regular signed Borel measure $\mu$ such that $\varphi(f) = \int_X f \, d\mu$ for all $f \in \mathcal{C}_{\mathbb{R}}(X)$. To this end one defines a new functional $\varphi'$ on the collection of nonnegative functions in $\mathcal{C}_{\mathbb{R}}(X)$ by $\varphi'(f) = \sup\{\varphi(g) : 0 \leq g \leq f\}$ for $f \geq 0$. Then one extends $\varphi'$ to $\mathcal{C}_{\mathbb{R}}(X)$ by setting $\varphi'(f) = \varphi'(f^+) - \varphi'(f^-)$ for all $f \in \mathcal{C}_{\mathbb{R}}(X)$.

To verify that $\varphi'$ thus extended is a linear functional, observe that if $t \geq 0$, then $(tf)^+ = tf^+$ and $(tf)^- = tf^-$, so $\varphi'(tf) = t\varphi'(f^+) - t\varphi'(f^-) = t\varphi'(f)$. On the other hand, if $t \leq 0$, then $(tf)^+ = -tf^-$ and $(tf)^- = -tf^+$, so $\varphi'(tf) = \varphi'(-tf^-) - \varphi'(-tf^+) = t\varphi'(f)$. Thus $\varphi'$ is homogeneous.

To verify additivity, let $f_1$ and $f_2$ be two functions in $\mathcal{C}_{\mathbb{R}}(X)$ and write $h = f_1^+ + f_2^+ - (f_1 + f_2)^+$. Then $h \geq 0$, so $\varphi'(f_1^+) + \varphi'(f_2^+) = \varphi'(f_1^+ + f_2^+) = \varphi'((f_1 + f_2)^+) + \varphi'(h)$. On the other hand, $h = f_1^- + f_2^- - (f_1 + f_2)^-$, and therefore $\varphi'(f_1^-) + \varphi'(f_2^-) = \varphi'((f_1 + f_2)^-) + \varphi'(h)$, whence it follows at once that $\varphi'(f_1 + f_2) = \varphi'(f_1) + \varphi'(f_2)$. Thus $\varphi'$ is a positive linear functional on $\mathcal{C}_{\mathbb{R}}(X)$. The existence of $\mu$ then follows from the correspondence between positive linear functionals and regular Borel measures.
