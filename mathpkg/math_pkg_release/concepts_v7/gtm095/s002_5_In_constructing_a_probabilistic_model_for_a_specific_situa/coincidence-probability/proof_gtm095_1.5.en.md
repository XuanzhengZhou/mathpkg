---
role: proof
locale: en
of_concept: coincidence-probability
source_book: gtm095
source_chapter: "1"
source_section: "5"
---

# Proof of Coincidence Problem (Birthday Problem)

**Example 7 (Coincidence Problem).** Let an urn contain $M$ balls numbered $1, 2, \ldots, M$. We draw an ordered sample of size $n$ with replacement.

**Sample space.** The sample space is
$$\Omega = \{\omega : \omega = (a_1, \ldots, a_n),\; a_i = 1, \ldots, M\}$$
with $N(\Omega) = M^n$. Using the classical assignment of probabilities, all $M^n$ outcomes are equally probable.

**Event of no repetition.** Consider the event $A$ in which there is no repetition (all elements of the sample are distinct):
$$A = \{\omega : \omega = (a_1, \ldots, a_n),\; a_i \neq a_j \text{ for } i \neq j\}.$$

The number of outcomes in $A$ is the number of ordered $n$-tuples of distinct elements from $\{1, \ldots, M\}$:
$$N(A) = M(M-1) \cdots (M-n+1) = (M)_n.$$

**Probability of no repetition.** By the classical formula $\mathrm{P}(A) = N(A) / N(\Omega)$:
$$\mathrm{P}(A) = \frac{(M)_n}{M^n} = \left(1 - \frac{1}{M}\right)\left(1 - \frac{2}{M}\right) \cdots \left(1 - \frac{n-1}{M}\right). \tag{11}$$

**Birthday problem interpretation.** Suppose there are $n$ students in a class and each student's birthday is equally likely to fall on any of the 365 days of the year. Interpreting the selection of birthdays as drawing $n$ balls from an urn with $M = 365$ balls (with replacement), the probability $P_n$ that at least two students share a birthday is the complement of the event of all distinct birthdays:
$$P_n = 1 - \mathrm{P}(A) = 1 - \frac{(365)_n}{365^n}.$$

**Numerical values.** The text provides the following values:

| $n$ | 4 | 16 | 22 | 23 | 40 | 64 |
|-----|---|----|----|----|----|----|
| $P_n$ | 0.016 | 0.284 | 0.476 | 0.507 | 0.891 | 0.997 |

Remarkably, a class of only 23 students already has probability approximately $\frac{1}{2}$ of containing at least two students with the same birthday. For $n = 40$ the probability exceeds 0.89, and for $n = 64$ it is virtually 1.

**Remark on the complement formulation.** The probability of *at least one coincidence* is $1 - \mathrm{P}(A)$. The coincidence problem illustrates how intuition can fail: the number of people needed for a high probability of a shared birthday is much smaller than one might expect, because the number of *pairs* of people grows as $\binom{n}{2} \sim n^2/2$, and each pair provides an opportunity for a match.
