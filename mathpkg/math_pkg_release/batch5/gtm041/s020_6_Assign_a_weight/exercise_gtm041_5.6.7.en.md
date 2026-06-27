---
role: exercise
locale: en
chapter: "5"
section: "6"
exercise_number: 7
---

Let

$$S_n = \sum_{(b, d) \in T_n'} \frac{1}{bd(b+d)}.$$

[Rademacher's series for the partition function.] Let

$$A_r = \sum_{k=1}^{r} \frac{1}{r^2(r+k)} = \sum_{k=1}^{r} \sum_{d \mid (r,k)} \frac{\mu(d)}{r^2(r+k)},$$

so that

$$S_n = 2 \sum_{r > n} A_r.$$

(a) Show that

$$A_r = \sum_{d \mid r} \sum_{h=1}^{d} \frac{d\mu(r/d)}{r^3(h+d)}$$

and deduce that

$$A_r = \log 2 \frac{\varphi(r)}{r^3} + O\left(\frac{1}{r^3} \sum_{d \mid r} |\mu(d)|\right).$$

(b) Show that $\sum_{r=1}^{n} \sum_{d \mid r} |\mu(d)| = O(n \log n)$ and deduce that

$$\sum_{r > n} \frac{1}{r^3} \sum_{d \mid r} |\mu(d)| = O\left(\frac{\log n}{n^2}\right).$$

(c) Use the formula $\sum_{r \leq n} \varphi(r) = 3n^2/\pi^2 + O(n \log n)$ (proved in [4], Theorem 3.7) to deduce that

$$\sum_{r > n} \frac{\varphi(r)}{r^3} = \frac{6}{n\pi^2} + O\left(\frac{\log n}{n^2}\right).$$

(d) Use (a), (b), and (c) to deduce (16).
