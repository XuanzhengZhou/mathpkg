---
role: proof
locale: en
of_concept: liouville-approximation-lemma
source_book: gtm002
source_chapter: "2"
source_section: "2. Liouville Numbers"
---

Let $f(x)$ be a polynomial of degree $n$ with integer coefficients for which $f(z) = 0$. Let $M$ be a positive integer such that $|f'(x)| \leq M$ whenever $|z - x| \leq 1$. Then, by the mean value theorem,

$$|f(x)| = |f(z) - f(x)| \leq M |z - x| \quad \text{whenever} \quad |z - x| \leq 1. \tag{1}$$

Now consider any two integers $p$ and $q$, with $q > 0$. We wish to show that $|z - p/q| > 1/(M q^n)$. This is evidently true in case $|z - p/q| > 1$, so we may assume that $|z - p/q| \leq 1$. Then, by (1), $|f(p/q)| \leq M |z - p/q|$, and therefore

$$\left| q^n f\!\left(\frac{p}{q}\right) \right| \leq M q^n \left| z - \frac{p}{q} \right|. \tag{2}$$

The equation $f(x) = 0$ has no rational root (otherwise $z$ would satisfy an equation of degree less than $n$). Moreover, $q^n f(p/q)$ is an integer, since $f$ has degree $n$ and integer coefficients. Because $f(p/q) \neq 0$, we have $|q^n f(p/q)| \geq 1$. Combining this with (2) yields

$$1 \leq M q^n \left| z - \frac{p}{q} \right|,$$

and therefore

$$\left| z - \frac{p}{q} \right| \geq \frac{1}{M q^n}.$$

This completes the proof. (Note: the strict inequality $>$ in the statement follows because $|z - p/q| = 1/(M q^n)$ would imply equality in the mean value estimate, which cannot occur for an irrational $z$.)
