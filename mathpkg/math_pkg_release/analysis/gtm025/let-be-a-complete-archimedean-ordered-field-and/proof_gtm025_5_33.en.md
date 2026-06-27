---
role: proof
locale: en
of_concept: "let-be-a-complete-archimedean-ordered-field-and"
source_book: gtm025
source_chapter: "Set Theory and Algebra"
source_section: "5.33"
---

Let $b$ be any upper bound for $A$, and let $a \in A$. There exist positive integers $M$ and $-m$ such that $M > b$ and $-

If $q > p \geq 1$, then

$$0 \leq a_p - a_q = (a_p - a_{p+1}) + (a_{p+1} - a_{p+2}) + \cdots + (a_{q-1} - a_q)$$

$$\leq \frac{1}{2^{p+1}} + \frac{1}{2^{p+2}} + \cdots + \frac{1}{2^q} = \frac{1}{2^{p+1}} \left( 1 + \frac{1}{2} + \cdots + \frac{1}{2^{q-p-1}} \right)$$

$$= \frac{1}{2^{p+1}} \left( 2 - \frac{1}{2^{q-p-1}} \right) < \frac{1}{2^p}.$$

We thus have $|a_p - a_q| = a_p - a_q < \frac{1}{2^p}$ whenever $q > p \geq 1$. From (5.31) we infer that $(a_p)$ is a Cauchy sequence, and so $\lim_{p \to \infty} a_p$ exists; call it $c$. It is plain that $a_p \geq c$.

We claim that $\sup A = c$. To prove it, assume first that $c$ is not an upper bound for $A$. Then there is an $x \in A$ such that $x > c$, and hence there is a positive integer $p$ such that $a_p - c = |a_p - c| < x - c$; i.e., $a_p < x$. Since $a_p$ is an upper bound for $A$, the last inequality cannot obtain. Therefore $c$ is an upper bound for $A$. Assume next that there exists an upper bound $c'$ for $A$ such that $c' < c$, and choose a positive integer $p$ such that $\frac{1}{2^p} < c - c'$. We then have $a_p - \frac{1}{2^p} \geq c - \frac{1}{2^p} > c + c' - c = c'$, and so $a_p - \frac{1}{2^

If $x \in F_1$ and $x$ is not of the form $\frac{m}{n} 1_1$, then we define

$$\tau(x) = \sup \left\{ \frac{m}{n} 1_2 : \frac{m}{n} 1_1 < x \right\}.$$

It is left to the reader to prove that $\tau$ has the desired properties. $\square$
