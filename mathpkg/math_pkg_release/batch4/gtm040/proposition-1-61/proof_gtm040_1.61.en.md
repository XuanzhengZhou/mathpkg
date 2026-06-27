---
role: proof
locale: en
of_concept: proposition-1-61
source_book: gtm040
source_chapter: "1"
source_section: "61"
---

**Proof:** Let $f$ be the column vector whose $n$th entry is $a_n - L$, and let $\pi^{(n)}$ be the row vector defined by

$$\pi^{(n)} = \begin{cases} 1/n & \text{for } 1 \leq j \leq n \\ 0 & \text{for } n > j. \end{cases}$$

Then

$$b_n = \pi^{(n)}f + L.$$

Now $|\pi^{(n)}| = 1$, $\lim_n \pi^{(n)} = 0$, and $f$ is a column vector with entries tending to 0. Hence by Proposition 1-58, $\lim_n \pi^{(n)}f = 0$. Therefore $\lim_n b_n = L$.

The converse of Proposition 1-61 is false. The sequence $\{a_n\}$ defined by $a_{2n} = 0, a_{2n+1} = 1$ does not converge, but it is Cesaro summable.

Let $\{c_n\}$ be a sequence of real numbers. (In most applications the partial sums $c_0 + \cdots + c_n$ are assumed bounded.) If the limit

$$\lim_{t \to 1} \sum_{n=0}^{\infty} c_n t^n$$

exists, the limit is called the **Abel sum** of the series $\sum c_n$ and the series is said to be **Abel summable**. Abel’s Theorem is the following result.
