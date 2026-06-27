---
role: proof
locale: en
of_concept: "if-is-purely-discontinuous-then-the-corresponding-has"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.56"
---

Let $\sigma_u = \xi_{]u, \infty[}$. For $t > 0$, we have

$$\alpha(t) = \iota([0, t]) = \Sigma\{\iota(\{u\}) : 0 \leq u < t\}$$

$$= \sum_{x_k \geq 0} \iota(\{x_k\}) \sigma_x_k(t).$$

By (17.18),

define

$$\iota_d = \sum_k \iota(\{x_k\}) \varepsilon_{x_k}.$$

It is obvious that $\iota_d$ is a purely discontinuous measure as in (19.54) and that

$$\iota_d(E) = \sum_{x \in E} \iota(\{x\}) \leq \iota(E)$$

(1)

for every Borel set $E$. It is immediate from (1) that

$$\sum_k f(x_k) \iota(\{x_k\}) = \int_R f d\iota_d \leq \int_R f d\iota$$

(2)

for every nonnegative Borel measurable function $f$ on $R$. Define $I_c$ on $\mathfrak{C}_{00}(R)$ by

$$I_c(f) = \int_R f d\iota - \int_R f d\iota_d.$$

(3)

Since $\iota(F)$ is finite for every compact subset $F$ of $R$, both integrals on the right side of (3) are finite. Thus (2) shows that $I_c$ is a nonnegative linear functional on $\mathfrak{C}_{00}(R)$. Let $\iota_c$ be the regular Borel measure on $R$ constructed from $I_c$ as in § 9. Theorem (12.36) shows that

$$\int_R f d\iota = \int_R f d\iota_c + \int_R f d\iota_d = \int_R f d(\iota_c + \iota_d)$$

for all $f \in \mathfrak{C}_{00}(R)$. The equality (i) follows from (19.54) and (12.41). For all $x \in R$, it is clear that $\iota_c(\{x\}) = \iota(\{x\}) - \iota_d(\{x\}) = 0$, and a moment's thought shows that the decomposition (i) of $\iota$ is unique. $\square$

(19.58) Remark. Let $\iota$ be a regular Borel measure on $R$ and

$A_1 \subset A_2 \subset \cdots, \tilde{\nu}(A_n) < \infty$, and $X = \bigcup_{n=1}^{\infty} A_n$. Thus

$$\nu = \tilde{\nu} + \pi_1 + \pi_2,$$

(1)

where $\pi_1 \ll \mu$ and $\pi_2 \perp \mu$. Since $\tilde{\nu} + \pi_1 \ll \mu$, (1) is a Lebesgue decomposition of $\nu$. Therefore $\tilde{\nu} = 0$.

Suppose that $\nu$ and $\mu$ are not mutually singular. Use (19.42) to write $\nu = v_1 + v_2$, where $v_1 \ll \mu$ and $v_2 \perp \mu$. Then $v_1 \neq 0$ and $v_1 \leq \nu$; hence $v_1$ is the desired $\tilde{\nu}$.
