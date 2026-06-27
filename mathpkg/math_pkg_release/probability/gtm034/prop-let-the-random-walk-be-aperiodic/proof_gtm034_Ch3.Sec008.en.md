---
role: proof
locale: en
of_concept: prop-let-the-random-walk-be-aperiodic
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: To apply the renewal theorem, P9.3, it is helpful to think of a random walk

$$y_n = Z_1 + Z_2 + \cdots + Z_n, \quad y_0 = 0,$$

where $Z_1, Z_2, \ldots$ are independent with the same distribution as the ladder random variable $Z$. If this random walk is aperiodic, and if $E[Z] < \infty$, then the renewal theorem gives

$$\lim_{x \to \infty} \sum_{n=0}^{\infty} P_0[y_n = x] = \frac{1}{E[Z]}.$$

But that is precisely the result desired in part (a), since it follows from P7 that

$$v(x) = \frac{1}{\sqrt{c}} \sum_{n=0}^{\infty} P_0[y_n = x].$$

Finally, the evaluation of the limit in part (a) of P7 comes from P5. Therefore it remains only to check that the random walk $y_n$ is aperiodic if the given random walk has this property. The converse is obvious since the possible values of $y_n$ are a

such that $P(0,x_1)P(x_1,x_2)\ldots P(x_{m-1},x) = p > 0$. But then $P[Z = 1] \geq pP(x,1) > 0$. This construction fails only in one case, namely if $P(0,x) = 0$ for all $x \leq 0$, but in this case the random walk $y_n$ is exactly the original random walk.

That was the proof of part (a) and in part (b) there is nothing new. The criterion in terms of $\mu$ and $\sigma^2$ comes verbatim from the main theorem (T1) of this section.

E3 The case of symmetric random walk deserves special mention. It is clear from D2 that in this case

$$U(z) = V(z), \quad u(n) = v(n).$$

Hence also the limits in P8 should be the same, if they exist. That does not look obvious, but is true because the definition of $\alpha$ in P5 gives

$$\sqrt{c} e^\alpha = e^{\sum_{k=1}^{\infty} \frac{1}{k} \left\{ -\frac{1}{2} P[S_k = 0] + \frac{1}{2} - P[S_k > 0] \right\}} = 1.$$

Specializing still further (as far as possible) we consider symmetric simple random walk. In this case the result of P8 is exact in the sense that (see E17.1)

$$U(z) = V(z) = \frac{\sqrt{2}}{1 - z}, \quad u(n) = v(n) = \frac{\sqrt{2}}{\sigma} = \sqrt{2}.$$

In order to explain the usefulness of P8, let us anticipate a little. In P19.3 of the next section it will be proved that the Green function $g_B(x,y)$ of the left half-line $B = [x | x \leq -1]$ can be represented by

(1) $$g_B(x,y) = \sum_{n=0}^{\min(x,y)} u(x - n)v(y - n),$$

for $x$ and $y$ in $R - B$.
