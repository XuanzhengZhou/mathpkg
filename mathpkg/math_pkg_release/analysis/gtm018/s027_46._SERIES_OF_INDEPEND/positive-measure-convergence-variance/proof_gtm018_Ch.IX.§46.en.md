---
role: proof
locale: en
of_concept: positive-measure-convergence-variance
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

Write $s_0(x) = 0$ and $s_n(x) = \sum_{i=1}^{n} f_i(x)$ for $n = 1, 2, \dots$. Since $\sum f_n$ converges on a set of positive measure, Egoroff's theorem (cf. 21.2) implies the existence of a positive number $d$ such that the set

$$E = \bigcap_{n=0}^{\infty} \{x : |s_n(x)| \leq d\}$$

has positive measure. Define

$$E_n = \bigcap_{i=1}^{n} \{x : |s_i(x)| \leq d\}, \quad n = 0, 1, 2, \dots.$$

Then $\{E_n\}$ is a decreasing sequence of sets whose intersection is $E$.

Let $F_n = E_{n-1} \setminus E_n$ for $n = 1, 2, \dots$, and let $\alpha_n = \int_{E_n} s_n^2 \, d\mu$ for $n = 0, 1, 2, \dots$. Then

$$\alpha_n - \alpha_{n-1} = \int_{E_{n-1}} s_n^2 \, d\mu - \int_{F_n} s_n^2 \, d\mu - \int_{E_{n-1}} s_{n-1}^2 \, d\mu$$

$$= \int_{E_{n-1}} f_n^2 \, d\mu + 2 \int_{E_{n-1}} f_n s_{n-1} \, d\mu - \int_{F_n} s_n^2 \, d\mu.$$

Since $f_n$ is independent of $E_{n-1}$ and $\chi_{E_{n-1}} s_{n-1}$ (which depends only on $f_1, \dots, f_{n-1}$), and $\int f_n \, d\mu = 0$, the cross term vanishes:

$$\int_{E_{n-1}} f_n s_{n-1} \, d\mu = 0.$$

Also $\int_{E_{n-1}} f_n^2 \, d\mu = \mu(E_{n-1}) \sigma^2(f_n)$. Hence

$$\alpha_n - \alpha_{n-1} = \mu(E_{n-1}) \sigma^2(f_n) - \int_{F_n} s_n^2 \, d\mu \geq \mu(E) \sigma^2(f_n) - d^2 \mu(F_n).$$

Summing from $n=1$ to $N$ yields

$$\alpha_N - \alpha_0 \geq \mu(E) \sum_{n=1}^{N} \sigma^2(f_n) - d^2 \sum_{n=1}^{N} \mu(F_n).$$

Since $\alpha_N = \int_{E_N} s_N^2 \, d\mu \leq d^2$ and $\sum \mu(F_n) = \mu(X \setminus E) \leq 1$, we obtain $\sum_{n=1}^{\infty} \sigma^2(f_n) < \infty$.
