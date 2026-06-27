---
role: exercise
locale: en
chapter: "III"
section: "§2. Nonclassical CLT conditions"
exercise_number: 11
---

# Exercise 11: Lindeberg's Condition of Order $k$

Let $X_1, X_2, \ldots$ be a sequence of independent random variables with
$\mathbb{E} X_n = 0$, $\mathbb{E} X_n^2 = \sigma_n^2$. Assume that they obey the
Central Limit Theorem and

$$\mathbb{E}\Bigl( D_n^{-1/2} \sum_{i=1}^{n} X_i \Bigr)^k \to \frac{(2k)!}{2^k k!}$$

for some $k \geq 1$.

Show that in this case Lindeberg's condition of order $k$ holds, i.e.,

$$\sum_{j=1}^{n} \int_{\{|x| > \varepsilon\}} |x|^k \, dF_j(x) = o(D_n^k), \qquad \varepsilon > 0.$$

(The ordinary Lindeberg condition corresponds to $k = 2$.)
