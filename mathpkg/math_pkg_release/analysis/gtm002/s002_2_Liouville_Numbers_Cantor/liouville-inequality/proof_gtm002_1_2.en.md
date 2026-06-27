---
role: proof
locale: en
of_concept: liouville-inequality
source_book: gtm002
source_chapter: "1"
source_section: "2"
---

**Proof of Lemma 2.2.** Let $f(x)$ be a polynomial of degree $n$ with integer coefficients for which $f(z) = 0$. Let $M$ be a positive integer such that $|f'(x)| \leq M$ whenever $|z - x| \leq 1$. Then, by the mean value theorem,

$$|f(x)| = |f(z) - f(x)| \leq M|z - x| \quad \text{whenever} \quad |z - x| \leq 1. \tag{1}$$

Now consider any two integers $p$ and $q$, with $q > 0$. We wish to show that $|z - p/q| > 1/(Mq^n)$. This is evidently true in case $|z - p/q| > 1$, so we may assume that $|z - p/q| \leq 1$. Then, by (1), $|f(p/q)| \leq M|z - p/q|$, and therefore

$$\left| q^n f\left(\frac{p}{q}\right) \right| \leq Mq^n \left| z - \frac{p}{q} \right|. \tag{2}$$

The equation $f(x) = 0$ has no rational root (otherwise $z$ would satisfy an equation of degree less than $n$). Moreover, $q^n f(p/q)$ is an integer. Since $f(p/q) \neq 0$, it follows that

$$\left| q^n f\left(\frac{p}{q}\right) \right| \geq 1. \tag{3}$$

Combining (2) and (3) yields

$$1 \leq Mq^n \left| z - \frac{p}{q} \right|,$$

and therefore

$$\left| z - \frac{p}{q} \right| \geq \frac{1}{Mq^n}.$$

The strict inequality $> 1/(Mq^n)$ follows since equality cannot occur (if it did, $f(p/q) = \pm 1/M$ would not be an integer, contradicting that $q^n f(p/q)$ is integral). $\square$
