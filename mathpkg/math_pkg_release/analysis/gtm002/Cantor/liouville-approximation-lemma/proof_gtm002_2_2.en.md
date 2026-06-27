---
role: proof
locale: en
of_concept: liouville-approximation-lemma
source_book: gtm002
source_chapter: "2"
source_section: "2"
---

Let $f(x)$ be a polynomial of degree $n$ with integer coefficients for which $f(z) = 0$. Let $M$ be a positive integer such that $|f'(x)| \leq M$ whenever $|z - x| \leq 1$. Then, by the mean value theorem,

$$|f(x)| = |f(z) - f(x)| \leq M |z - x| \quad \text{whenever} \quad |z - x| \leq 1. \tag{1}$$

Now consider any two integers $p$ and $q$, with $q > 0$. We wish to show that $|z - p/q| > 1/Mq^n$. This is evidently true in case $|z - p/q| > 1$, so we may assume that $|z - p/q| \leq 1$. Then, by (1), $|f(p/q)| \leq M |z - p/q|$, and therefore

$$|q^n f(p/q)| \leq M q^n |z - p/q|. \tag{2}$$

The equation $f(x) = 0$ has no rational root (otherwise $z$ would satisfy an equation of degree less than $n$). Moreover, $q^n f(p/q)$ is an integer, not zero. Therefore $|q^n f(p/q)| \geq 1$. From (2) we obtain

$$1 \leq M q^n |z - p/q|,$$

which is equivalent to the desired inequality.
