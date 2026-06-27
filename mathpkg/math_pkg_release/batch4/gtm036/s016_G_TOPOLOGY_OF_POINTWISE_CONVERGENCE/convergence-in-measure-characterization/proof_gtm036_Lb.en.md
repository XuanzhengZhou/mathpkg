---
role: proof
locale: en
of_concept: convergence-in-measure-characterization
source_book: gtm036
source_chapter: "L"
source_section: "L(b)"
---

Suppose $f_n \to 0$ in $\mathcal{T}$. For any $r > 0$, choose $n$ with $1/n < r$. Since $f_n \to 0$, eventually $f_n \in U_N$ for sufficiently large $N$, meaning $\mu(\{x : |f_n(x)| > 1/N\}) < 1/N$. For large enough $n$, $1/N < r$, so $\mu(\{x : |f_n(x)| > r\}) \leq \mu(\{x : |f_n(x)| > 1/N\}) \to 0$.

Conversely, suppose $\mu(\{x : |f_n(x)| > r\}) \to 0$ for every $r > 0$. Given any $U_m$, choose $r = 1/m$. Since $\mu(\{x : |f_n(x)| > 1/m\}) \to 0$, we have $\mu(\{x : |f_n(x)| > 1/m\}) < 1/m$ for all sufficiently large $n$, i.e., $f_n \in U_m$. Thus $f_n \to 0$ in $\mathcal{T}$.
