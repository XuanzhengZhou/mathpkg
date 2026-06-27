---
role: proof
locale: en
of_concept: jensen-inequality
source_book: gtm017
source_chapter: "II"
source_section: "problems"
---
By induction on $n$. For $n=2$, this is the definition of convexity. Assume true for $n-1$. Then for $p_n < 1$:
$$f\left(\sum_{i=1}^{n} p_i x_i\right) = f\left((1-p_n)\sum_{i=1}^{n-1} \frac{p_i}{1-p_n} x_i + p_n x_n\right)$$
$$\leq (1-p_n) f\left(\sum_{i=1}^{n-1} \frac{p_i}{1-p_n} x_i\right) + p_n f(x_n)$$
$$\leq (1-p_n) \sum_{i=1}^{n-1} \frac{p_i}{1-p_n} f(x_i) + p_n f(x_n) = \sum_{i=1}^{n} p_i f(x_i).$$
