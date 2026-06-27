---
role: proof
locale: en
of_concept: compatibility-normal-limiting-system
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

It is easily seen that $\operatorname{Comp}(x, y)$ implies $\operatorname{Comp}(x, p_{\alpha\beta}(y))$: if $z \leq x$ and $z \leq y$, then $p_{\alpha\beta}(z) \leq p_{\alpha\beta}(x) = x$ (since $x \in P_{\alpha}$ and $p_{\alpha\beta}$ acts as identity on $P_{\alpha}$) and $p_{\alpha\beta}(z) \leq p_{\alpha\beta}(y)$.

Now assume $x$ and $p_{\alpha\beta}(y)$ are compatible. Then
$$(\exists z \in P_{\alpha})[z \leq x \land z \in [p_{\alpha\beta}(y)]_{P_{\alpha}} = p_{\alpha\beta}``[y]_{P_{\beta}}],$$
where the equality follows from condition 4 of the normal limiting system (Theorem 22.24(2)). Therefore
$$(\exists u \in P_{\beta})[u \leq y \land z = p_{\alpha\beta}(u)].$$

Now $p_{\alpha\beta}(u) = z \leq x$, and by the lifting property (condition 4*), $u \leq x$. Hence $u$ witnesses that $x$ and $y$ are compatible.
