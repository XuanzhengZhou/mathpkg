---
role: proof
locale: en
of_concept: riesz-integral-lower-bound
source_book: gtm018
source_chapter: "56"
source_section: "56. LINEAR FUNCTIONALS"
---

Since both $\int f \, d\mu$ and $\Lambda(f)$ depend linearly on $f$, it is sufficient to prove the inequality for functions $f$ such that $0 \leq f(x) \leq 1$ for all $x$ in $X$.

Let $n$ be a fixed positive integer and write, for $i = 1, \dots, n$,

$$f_i(x) = \begin{cases} 
0 & \text{if } f(x) < \frac{i-1}{n}, \\[4pt]
\dfrac{f(x) - \frac{i-1}{n}}{\frac{1}{n}} = nf(x) - (i-1) & \text{if } \frac{i-1}{n} \leq f(x) \leq \frac{i}{n}, \\[8pt]
1 & \text{if } \frac{i}{n} < f(x).
\end{cases}$$

Since, for $i = 1, \dots, n$,

$$f_i = \big([nf - (i-1)] \cup 0\big) \cap 1 = \big([nf - (i-1)] \cap 1\big) \cup 0,$$

the functions $f_i$ all belong to $\mathcal{L}_+$. Since for any $x$ for which $\frac{j-1}{n} \leq f(x) \leq \frac{j}{n}$, we have

$$f_i(x) = \begin{cases} 
1 & \text{if } 1 \leq i \leq j-1, \\
0 & \text{if } j+1 \leq i \leq n,
\end{cases}$$

it follows that $f(x) = \frac{1}{n} \sum_{i=1}^{n} f_i(x)$ for every $x$ in $X$.

If, for $i = 0, 1, \dots, n$, $U_i = \left\{ x : f(x) > \frac{i}{n} \right\}$, then $U_i$ is a bounded open set such that, for $i = 1, \dots, n$, $U_i \subset f_i$, and hence, by Theorem A, $\mu(U_i) \leq \Lambda(f_i)$. Since $U_0 \supset U_1 \supset \cdots \supset U_n = \emptyset$, we have

\begin{align*}
\Lambda(f) &= \frac{1}{n} \sum_{i=1}^{n} \Lambda(f_i) \geq \frac{1}{n} \sum_{i=1}^{n} \mu(U_i) \\
&= \sum_{i=1}^{n} \mu(U_i) \cdot \frac{1}{n} \\
&\geq \sum_{i=1}^{n-1} \int_{U_i - U_{i+1}} f \, d\mu - \frac{1}{n} \mu(U_1) \\
&= \int_{U_1} f \, d\mu - \frac{1}{n} \mu(U_1) \geq \int f \, d\mu - \frac{1}{n} \mu(U_0).
\end{align*}

The arbitrariness of $n$ and the finiteness of $\mu(U_0)$ imply the desired result.
