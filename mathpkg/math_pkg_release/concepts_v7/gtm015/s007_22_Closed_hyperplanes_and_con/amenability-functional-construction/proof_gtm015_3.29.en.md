---
role: proof
locale: en
of_concept: amenability-functional-construction
source_book: gtm015
source_chapter: "3"
source_section: "29"
---

# Proof of Construction of a subadditive functional for abelian semigroups

If $T$ is an abelian semigroup, there exists a real-valued function $p$ on $\mathcal{B} = \mathcal{B}_{\mathbb{R}}(T)$ such that

(1) $p(x + y) \le p(x) + p(y)$ for all $x, y \in \mathcal{B}$,
(2) $p(\alpha x) = \alpha p(x)$ for all $x \in \mathcal{B}, \alpha > 0$,
(3) $\inf x \le p(x) \le \sup x$ for all $x \in \mathcal{B}$,
(4) $p(x - x_s) = p(x_s - x) = 0$ for all $x \in \mathcal{B}, s \in T$.

Denote by $\mathcal{F}$ the set of all $n$-tuples $F = (t_1, \ldots, t_n)$ of elements of $T$, with $n$ arbitrary and with repetitions allowed. For $F = (t_1, \ldots, t_n)$ and $x \in \mathcal{B}$, define

$$M_F(x) = \sup\left\{(1/n) \sum_{i=1}^{n} x(t + t_i) : t \in T\right\}.$$

Then $\inf x \le M_F(x) \le \sup x$. Moreover, $M_{F+G}(x+y) \le M_F(x) + M_G(y)$ for $F, G \in \mathcal{F}$, and $M_F(\alpha x) = \alpha M_F(x)$ for $\alpha > 0$.

Define $p(x) = \inf\{M_F(x) : F \in \mathcal{F}\}$. Conditions (1)-(3) follow from the corresponding properties of $M_F$. For (4), given $s \in T$ and any positive integer $n$, set $t_1 = s, t_2 = 2s, \ldots, t_n = ns$. Then $M_F(x - x_s) \le (1/n)(\sup x - \inf x)$, so $p(x - x_s) \le 0$ and $p(x_s - x) \le 0$. Since $-p(-y) \le p(y)$ for all $y$, we get $0 \le p(x_s - x) = p(x - x_s) \le 0$, hence $p(x_s - x) = p(x - x_s) = 0$.
