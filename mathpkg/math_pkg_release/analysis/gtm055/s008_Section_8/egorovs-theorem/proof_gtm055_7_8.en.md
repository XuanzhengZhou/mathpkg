---
role: proof
locale: en
of_concept: egorovs-theorem
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

For each pair of positive integers $(k, n)$, define

$$E_{k,n} = \bigcap_{m=n}^{\infty} \{x \in X : |f_m(x) - f(x)| < 1/k\}.$$

For fixed $k$, the sets $E_{k,n}$ are measurable and increase with $n$. Since $f_n \to f$ a.e., we have $\mu(X \setminus \bigcup_{n=1}^{\infty} E_{k,n}) = 0$ after possibly removing a null set. Hence $\lim_{n} \mu(X \setminus E_{k,n}) = 0$ by semicontinuity (Proposition 7.4).

Given $\varepsilon > 0$, for each $k$ choose $n_k$ such that $\mu(X \setminus E_{k,n_k}) < \varepsilon / 2^k$. Set

$$E = \bigcap_{k=1}^{\infty} E_{k,n_k}.$$

Then $E$ is measurable and

$$\mu(X \setminus E) = \mu\left(\bigcup_{k=1}^{\infty} (X \setminus E_{k,n_k})\right) \le \sum_{k=1}^{\infty} \mu(X \setminus E_{k,n_k}) < \sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon.$$

On $E$, for every $k$ and every $m \ge n_k$, we have $|f_m(x) - f(x)| < 1/k$. Hence $\{f_n\}$ converges uniformly to $f$ on $E$.
