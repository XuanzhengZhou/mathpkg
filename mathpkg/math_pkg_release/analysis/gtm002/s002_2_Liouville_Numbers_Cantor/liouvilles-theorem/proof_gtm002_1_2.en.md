---
role: proof
locale: en
of_concept: liouvilles-theorem
source_book: gtm002
source_chapter: "1"
source_section: "2"
---

**Proof of Theorem 2.3.** Suppose $z$ is a Liouville number and suppose, for contradiction, that $z$ is algebraic of degree $n$. If $n = 1$, then $z$ is rational, which is impossible since a Liouville number cannot be rational (a rational number $a/b$ satisfies $|a/b - p/q| = |aq - bp|/(bq) \geq 1/(bq)$, which for fixed $b$ and large $k$ cannot be less than $1/q^k$ for infinitely many $q$). Hence $n > 1$.

By Lemma 2.2, there exists a positive integer $M$ such that

$$\left| z - \frac{p}{q} \right| > \frac{1}{Mq^n}$$

for all integers $p$ and $q$ with $q > 0$.

On the other hand, since $z$ is a Liouville number, for every positive integer $k$ there exist integers $p$ and $q$ with $q > 1$ such that

$$\left| z - \frac{p}{q} \right| < \frac{1}{q^k}.$$

Choose $k$ sufficiently large so that $2^{k-n} \geq M$. From the two inequalities we obtain

$$\frac{1}{q^k} > \left| z - \frac{p}{q} \right| > \frac{1}{Mq^n},$$

hence $M > q^{k-n}$. But $q \geq 2$, so $q^{k-n} \geq 2^{k-n} \geq M$, a contradiction. Therefore $z$ cannot be algebraic, so $z$ is transcendental. $\square$
