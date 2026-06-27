---
role: proof
locale: en
of_concept: laplace-capture-recapture
source_book: gtm095
source_chapter: "1"
source_section: "5"
---

# Proof of Laplace Capture-Recapture Method

**Problem 5 (Section 5).** Laplace (1786) proposed the following method to estimate the population size $N$ without a complete census.

**Procedure.** Draw a sample of size $M$ from the population and mark its elements. Return them to the population and assume they become "well mixed" with the unmarked elements. Then draw a second sample of size $n$ from the mixed population. Let $X$ be the number of marked elements in the second sample.

**Step 1: Probability model.** The probability that exactly $m$ marked elements appear in the second sample follows the hypergeometric distribution (cf. formula (4)):
$$\mathrm{P}_{N,M;n}\{X = m\} = \frac{\binom{M}{m} \binom{N-M}{n-m}}{\binom{N}{n}}. \tag{*}$$

This is the probability of choosing $m$ marked elements from the $M$ marked ones and $n-m$ unmarked elements from the $N-M$ unmarked ones, divided by the total number of ways to choose $n$ elements from $N$.

**Step 2: Maximum likelihood estimator.** For fixed $M$, $n$, and observed $m$, find $N$ that maximizes the probability (*). The "most likely" population size $\hat{N}$ is the integer $N \geq M + (n-m)$ (since there must be at least $M$ marked and $n-m$ unmarked individuals) that maximizes:
$$L(N) = \frac{\binom{M}{m} \binom{N-M}{n-m}}{\binom{N}{n}}.$$

Consider the ratio:
$$\frac{L(N)}{L(N-1)} = \frac{\binom{N-M}{n-m} \binom{N-1}{n}}{\binom{N}{n} \binom{N-1-M}{n-m}} = \frac{(N-M)(N-n)}{N(N-M-n+m)}.$$

The function $L(N)$ is increasing as long as this ratio exceeds $1$, i.e.,
$$\frac{(N-M)(N-n)}{N(N-M-n+m)} > 1.$$

Simplifying:
$$(N-M)(N-n) > N(N-M-n+m),$$
$$N^2 - Nn - MN + Mn > N^2 - MN - Nn + Nm,$$
$$Mn > Nm,$$
$$N < \frac{Mn}{m}.$$

Thus $L(N)$ increases for $N < Mn/m$ and decreases for $N > Mn/m$. The maximum is attained at $N = Mn/m$. Since $N$ must be an integer, the maximum likelihood estimator is:
$$\hat{N} = \left\lfloor \frac{Mn}{m} \right\rfloor,$$
where $[\cdot]$ denotes the integral part (floor).

**Interpretation.** The estimate $\hat{N} = [Mn/m]$ is intuitive: the proportion of marked individuals in the second sample ($m/n$) should approximately equal the proportion of marked individuals in the entire population ($M/N$), giving $m/n \approx M/N$, hence $N \approx Mn/m$.

**Remark.** The problem is continued in Section 7 (Problem 4) of the textbook, where further properties of this estimator are studied.
