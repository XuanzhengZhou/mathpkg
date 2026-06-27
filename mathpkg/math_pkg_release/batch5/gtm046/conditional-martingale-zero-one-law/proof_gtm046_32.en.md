---
role: proof
locale: en
of_concept: conditional-martingale-zero-one-law
source_book: gtm046
source_chapter: "X"
source_section: "32"
---

Let \(Y, Y_1, Y_2, \ldots\) be random variables and apply the submartingale convergence theorem (29.3A). Define the sequence

$$
Z_n = E(Y \mid Y_1, \ldots, Y_n).
$$

This is a martingale sequence with respect to the filtration \(\mathcal{B}_n = \sigma(Y_1, \ldots, Y_n)\), since

$$
E(Z_{n+1} \mid \mathcal{B}_n) = E(E(Y \mid Y_1, \ldots, Y_{n+1}) \mid \mathcal{B}_n) = E(Y \mid \mathcal{B}_n) = Z_n.
$$

If \(EY^+ < \infty\), then every \(EZ_n^+ \leq EY^+\) (by the conditional Jensen inequality applied to the submartingale property), and hence \(\sup_n EZ_n^+ < \infty\). By the martingale convergence theorem (I in 32.1), it follows that \(Z_n \xrightarrow{a.s.} Z\) for some random variable \(Z\) with \(Z < \infty\) a.s.

If furthermore \(E|Y|^r < \infty\) for some \(r \geq 1\), then the \(|Z_n|^r\) are uniformly integrable (by the conditional Jensen inequality, \(E|Z_n|^r \leq E|Y|^r < \infty\)), so by the submartingale closure theorem (B in 32.1), the martingale is closed on the right by \(Z = E(Y \mid Y_1, Y_2, \ldots)\). Thus \(Z_n \xrightarrow{a.s.} E(Y \mid Y_1, Y_2, \ldots)\).

Finally, if \(Y\) is defined on the \(Y_n\) (i.e., \(Y\) is \(\sigma(Y_1, Y_2, \ldots)\)-measurable), then \(Z = E(Y \mid Y_1, Y_2, \ldots) = Y\) a.s., and the convergence reduces to \(Z_n \xrightarrow{a.s.} Y\).

Specializing to indicator functions \(Y = I_B\) where \(B\) is an event defined on the \(Y_n\) yields the zero-one law: \(P(B \mid Y_1, \ldots, Y_n) \xrightarrow{a.s.} I_B\).
