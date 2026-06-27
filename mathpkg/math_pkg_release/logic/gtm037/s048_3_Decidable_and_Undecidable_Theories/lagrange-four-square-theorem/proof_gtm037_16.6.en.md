---
role: proof
locale: en
of_concept: lagrange-four-square-theorem
source_book: gtm037
source_chapter: "16"
source_section: "1"
---

The proof uses Lemma 16.3 (the four-square multiplication identity) and Lemma 16.4. The direction (i) $\Rightarrow$ (ii) follows from the fact that every natural number is a sum of four squares, which is proved by induction using the following argument.

Suppose not every natural number is a sum of four squares. Let $p$ be the smallest prime for which some multiple $mp$ ($1 \leq m < p$) is a counterexample. Choose the minimal such $mp$, say $x_1^2 + x_2^2 + x_3^2 + x_4^2 = mp$ with $m$ minimal. By Lemma 16.4, such a representation exists for some $m < p$.

If $m = 1$, then $p$ itself is a sum of four squares, contradiction. If $m > 1$, choose integers $y_1, y_2, y_3, y_4$ such that $y_i \equiv x_i \pmod{m}$ and $|y_i| \leq m/2$ for each $i$. Then

$$y_1^2 + y_2^2 + y_3^2 + y_4^2 = mn$$

for some $n$. Since $|y_i| \leq m/2$, we have $mn < 4(m/2)^2 = m^2$, so $n < m$. Also $n \neq 0$, since otherwise $y_i = 0$ for each $i$ and $m \mid x_i$ for each $i$, so $m^2 \mid x_1^2 + \cdots + x_4^2 = mp$, hence $m \mid p$, contradiction.

Now $(mn)(mp)$ is a sum of four squares by Lemma 16.3, and each term in the identity is divisible by $m$. Hence $np$ is a sum of four squares with $0 < n < m$, contradicting the minimality of $m$.

The direction (ii) $\Rightarrow$ (i) holds because every sum of four integer squares is non-negative, i.e., belongs to $\omega$.
