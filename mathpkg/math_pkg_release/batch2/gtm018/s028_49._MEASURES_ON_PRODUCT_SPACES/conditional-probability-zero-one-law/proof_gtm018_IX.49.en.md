---
role: proof
locale: en
of_concept: conditional-probability-zero-one-law
source_book: gtm018
source_chapter: "IX"
source_section: "49"
---

It is convenient to prove almost uniform convergence instead of almost everywhere convergence — it follows from 21.A and 21.B that the two are equivalent. Let $\epsilon$ and $\delta$ be any two positive numbers and suppose that $\delta < 1$. By 13.D there exists a positive integer $n_0$ and a measurable $\{1, \cdots, n_0\}$-cylinder $E_0$ such that

$$\mu(E \Delta E_0) < \frac{\epsilon \delta}{2}.$$

Write $B = E \Delta E_0$ and observe that if $x \in E' \cup B$, then

$$\chi_E(x) = \chi_{E_0}(x).$$

Define
$$C_n = \{x: p(B, T_n(x)) \geq \delta\}, \quad D_n = C_n - \bigcup_{1 \leq i < n} C_i, \quad n = 1, 2, \cdots,$$
and $C = \bigcup_{n=1}^{\infty} C_n = \bigcup_{n=1}^{\infty} D_n$. For each $n$, $C_n$ and $D_n$ are measurable $\{1, \cdots, n\}$-cylinders. It follows that

$$\mu(B \cap D_n) = \int_{D_n} p(B, T_n(x)) d\mu(x) \geq \delta \mu(D_n),$$

and hence that

$$\frac{\epsilon \delta}{2} > \mu(B) \geq \mu(B \cap C) = \sum_{n=1}^{\infty} \mu(B \cap D_n) \geq \delta \sum_{n=1}^{\infty} \mu(D_n) = \delta \mu(C).$$

Thus $\mu(C) < \epsilon/2$. If $A = X - C$, then $\mu(A) > 1 - \epsilon/2$. One may assume that the conditional probability relations are valid for every $x$ in $X$. If $n \geq n_0$, then it follows from 38.A and 48.B that

$$|p(E, T_n(x)) - \chi_{E_0}(x)| \leq p(B, T_n(x)).$$

If, in addition, $x \in A$, then, in the first place $\chi_{E_0}(x) = \chi_E(x)$ and, in the second place $p(B, T_n(x)) < \delta$, so that

$$|p(E, T_n(x)) - \chi_E(x)| < \delta.$$

Since $\epsilon$ and $\delta$ are arbitrary, this establishes almost uniform convergence, and hence almost everywhere convergence, of $p(E, T_n(x))$ to $\chi_E(x)$.
