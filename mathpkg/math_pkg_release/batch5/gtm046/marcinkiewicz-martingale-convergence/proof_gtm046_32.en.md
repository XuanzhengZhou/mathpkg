---
role: proof
locale: en
of_concept: marcinkiewicz-martingale-convergence
source_book: gtm046
source_chapter: "X"
source_section: "32"
---

Let \(X_n = \sum_{k=1}^{n} Y_k\) where the \(Y_k\) are independent random variables centered at expectations (\(EY_k = 0\)), and let \(r \geq 1\).

**Sufficiency (\(X_n \xrightarrow{r} X \Rightarrow X_n \xrightarrow{a.s.} X\)):** If \(X_n\) converges in \(L_r\) to \(X\), then by the \(L_r\)-convergence theorem, the \(|X_n|^r\) are uniformly integrable. Moreover, by the Kolmogorov inequality (extended to arbitrary \(r \geq 1\) as stated in II), for every \(\epsilon > 0\),

$$
P\left[\sup_{k \leq n} |X_k| > c\right] \leq \frac{E|X_n|^r}{c^r}.
$$

Since \(E|X_n|^r\) is uniformly bounded (by uniform integrability and convergence), this inequality extends to the full sequence. The a.s. convergence then follows from the standard argument: the martingale convergence theorem applied to \(X_n\) (which is a martingale since the summands are independent and centered) yields \(X_n \xrightarrow{a.s.} X'\) for some \(X'\), and since \(X_n \xrightarrow{r} X\), we have \(X' = X\) a.s.

**Necessity (\(X_n \xrightarrow{a.s.} X \in L_r \Rightarrow X_n \xrightarrow{r} X\)):** If \(X_n \xrightarrow{a.s.} X\) with \(X \in L_r\), then \(X_n\) is a martingale sequence. Since the summands are independent and centered, \(X_n\) has orthogonal increments for \(r = 2\) and, by the martingale property, \(E|X_n|^r\) is nondecreasing. The a.s. limit \(X \in L_r\) implies that \(\sup_n E|X_n|^r \leq E|X|^r < \infty\). By the \(L_r\)-convergence theorem for submartingales (B in 32.1), the convergence also holds in \(L_r\). Thus \(X_n \xrightarrow{r} X\).

The equivalence is therefore established: for consecutive sums of independent centered random variables, a.s. convergence to an \(L_r\) limit is equivalent to convergence in the \(r\)-th mean.
