---
role: proof
locale: en
of_concept: liouville-approximation-lemma
source_book: gtm002
source_chapter: "2"
source_section: "Liouville Numbers"
---

Let (x)$ be a polynomial of degree $ with integer coefficients for which (z) = 0$. Let $ be a positive integer such that $|f'(x)| \leq M$ whenever $|z - x| \leq 1$. By the mean value theorem,
2239885|f(x)| = |f(z) - f(x)| \leq M|z - x| \quad \text{whenever} \quad |z-x| \leq 1.2239885
If $|z - p/q| > 1$, the inequality holds trivially. Otherwise, $|f(p/q)| \leq M|z - p/q|$. The number ^n f(p/q)$ is a non-zero integer (since $ has no rational root). Hence $|q^n f(p/q)| \geq 1$. Therefore
22398851 \leq |q^n f(p/q)| \leq M q^n |z - p/q|.2239885
Thus $|z - p/q| \geq 1/Mq^n$. Strict inequality follows since a rational root would imply $ satisfies an equation of lower degree.
