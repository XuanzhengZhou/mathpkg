---
role: proof
locale: en
of_concept: symmetric-random-walk-recurrence-transience
source_book: gtm040
source_chapter: "7"
source_section: "Symmetric random walk in n dimensions"
---

**Dimension 1 (recurrence).** All states communicate in the random walks of all dimensions; hence each of them is either transient or recurrent. In one dimension the state space is the integers, and

$$P_{i,i+1} = P_{i,i-1} = \frac{1}{2}.$$

Since the mean step is zero, the process is recurrent by Proposition 5-22. 

A more direct proof of the recurrence proceeds as follows. It is impossible to get from state $2$ to state $0$ without going through $1$. This fact, together with the translation invariance of the hitting probabilities, implies that

$$H_{20} = H_{21}H_{10} = (H_{10})^2.$$

But

$$\bar{H}_{00} = \frac{1}{2}H_{10} + \frac{1}{2}H_{-1,0} = \frac{1}{2}H_{10} + \frac{1}{2}H_{01} = H_{10}$$

since $H_{01} = H_{10}$. Therefore, the identity

$$H_{10} = \frac{1}{2}H_{00} + \frac{1}{2}H_{20} = \frac{1}{2} + \frac{1}{2}(H_{10})^2$$

implies that $H_{10} = 1$ and hence $\bar{H}_{00} = 1$. Consequently, the process is recurrent.

**Dimension 2 (recurrence).** In the two-dimensional case there are two simultaneous processes going on in perpendicular directions, and for the process to return to the origin, both of them must return to their zero positions at the same time. Letting $k$ be the number of steps to the right and $n-k$ the number of steps up in $2n$ steps, we have

$$P_{00}^{(2n)} = 4^{-2n} \sum_{k=0}^{n} \binom{2n}{k, k, n-k, n-k}.$$

Multiply numerator and denominator of the multinomial coefficient by $(n!)^2$ to see that it equals $\binom{2n}{n} \binom{n}{k}^2$. Thus

$$P_{00}^{(2n)} = 4^{-2n} \binom{2n}{n} \sum_{k=0}^{n} \binom{n}{k}^2.$$

The identity

$$\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$$

shows that

$$P_{00}^{(2n)} = 4^{-2n} \binom{2n}{n}^2.$$

Since $\binom{2n}{n} \sim c 2^{2n} \frac{1}{\sqrt{n}}$, we have

$$P_{00}^{(2n)} \sim c^2 \frac{1}{n}.$$

Thus the series $N_{00} = \sum P_{00}^{(2n)}$ dominates a multiple of $\sum 1/n$, so $N_{00}$ must be infinite, and the process is recurrent.

An alternate proof uses the coordinate transformation $u = x + y$, $v = x - y$, under which the two-dimensional symmetric random walk executes two one-dimensional symmetric random walks independently. Hence $P_{00}^{(2n)}$ is the probability that both $u = 0$ and $v = 0$ after $2n$ steps, which equals $(P_{00}^{(2n)})^2$ for the one-dimensional walk, and the same asymptotic analysis yields recurrence.

**Dimension $n \geq 3$ (transience).** For the three-dimensional symmetric random walk, the coefficients $\binom{n}{j, k, n-j-k}$ are dominated by the central term $\binom{n}{n/3, n/3, n/3}$, where the gamma function may be used for $(n/3)!$ if $3$ does not divide $n$. The observation that the coefficients $\binom{n}{j, k, n-j-k}$ sum to $3^n$ implies that

$$P_{00}^{(2n)} \leq 2^{-2n} \binom{2n}{n} 3^{-n} \binom{n}{n/3, n/3, n/3}.$$

Summing on $n$ and using the approximations of Section 1-6a, the series $N_{00} = \sum P_{00}^{(2n)}$ is dominated by a multiple of $\sum 1/n^{3/2}$. Therefore $N_{00}$ is finite, and the process is transient.

If any higher-dimensional random walk were recurrent, then the process projected to a three-dimensional set would be recurrent, and the latter process watched only when it changes state would also be recurrent. But this last process is exactly the three-dimensional symmetric walk, already shown to be transient. Hence the random walk in all dimensions greater than or equal to three is transient.
