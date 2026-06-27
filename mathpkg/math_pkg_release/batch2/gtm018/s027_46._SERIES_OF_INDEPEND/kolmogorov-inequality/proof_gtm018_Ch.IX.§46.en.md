---
role: proof
locale: en
of_concept: kolmogorov-inequality
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

Define $s_k(x) = \sum_{i=1}^{k} f_i(x)$ for $k = 1, \dots, n$, and let

$$E_1 = \{x : |s_1(x)| \geq \epsilon\},$$

$$E_k = \{x : |s_i(x)| < \epsilon \text{ for } i = 1, \dots, k-1, \text{ and } |s_k(x)| \geq \epsilon\}, \quad k = 2, \dots, n.$$

The sets $E_k$ are disjoint and $E = \{x : f(x) \geq \epsilon\} = \bigcup_{k=1}^{n} E_k$.

Since the $f_i$ are independent and have zero mean, we have $\int s_n \chi_{E_k} d\mu = \int_{E_k} s_n d\mu$ and by the properties of independent functions, $\int_{E_k} f_i d\mu = 0$ for $i > k$ when integrating against $\chi_{E_k}$.

More directly, because $E_k$ depends only on $f_1, \dots, f_k$, the functions $f_{k+1}, \dots, f_n$ are independent of $\chi_{E_k}$. Hence

$$\int_{E_k} s_n^2 d\mu \geq \int_{E_k} s_k^2 d\mu \geq \epsilon^2 \mu(E_k).$$

Therefore,

$$\sum_{k=1}^{n} \sigma^2(f_k) = \int (f_1 + \cdots + f_n)^2 d\mu = \int s_n^2 d\mu \geq \int_E s_n^2 d\mu = \sum_{k=1}^{n} \int_{E_k} s_n^2 d\mu \geq \sum_{k=1}^{n} \mu(E_k) \epsilon^2 = \mu(E) \epsilon^2.$$

Dividing by $\epsilon^2$ yields the desired inequality:

$$\mu(\{x : f(x) \geq \epsilon\}) \leq \frac{1}{\epsilon^2} \sum_{i=1}^{n} \sigma^2(f_i).$$
