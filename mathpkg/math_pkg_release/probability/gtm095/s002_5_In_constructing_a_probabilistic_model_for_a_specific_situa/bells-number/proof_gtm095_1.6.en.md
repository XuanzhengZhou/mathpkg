---
role: proof
locale: en
of_concept: bells-number
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of Bell Number Formula

**Problem 2 (Section 6).** Let $\Omega$ contain $N$ elements. Show that the Bell number $B_N$, counting the number of different decompositions (partitions) of $\Omega$, is given by the formula
$$B_N = e^{-1} \sum_{k=0}^{\infty} \frac{k^N}{k!}. \tag{12}$$

**Hint from the text.** Show that
$$B_N = \sum_{k=0}^{N-1} \binom{N-1}{k} B_k, \quad \text{where } B_0 = 1,$$
and then verify that the series in (12) satisfies the same recurrence relation.

**Proof following the hint.**

**Step 1: Recurrence relation.** Consider a particular element $x \in \Omega$. In any partition of $\Omega$, the element $x$ belongs to some block. Suppose this block has size $N - k$ (where $k = 0, \ldots, N-1$). The other $k$ elements not in $x$'s block form a subset of $\Omega \setminus \{x\}$ that is partitioned arbitrarily among themselves. To construct a partition:
- Choose the $k$ elements that are NOT in $x$'s block: there are $\binom{N-1}{k}$ ways (from the $N-1$ other elements).
- Partition those $k$ elements arbitrarily: there are $B_k$ ways.

Summing over all possible $k$ yields:
$$B_N = \sum_{k=0}^{N-1} \binom{N-1}{k} B_k, \quad B_0 = 1.$$

**Step 2: Verification that (12) satisfies the recurrence.** Define
$$\tilde{B}_N = e^{-1} \sum_{k=0}^{\infty} \frac{k^N}{k!}.$$
Then $\tilde{B}_0 = e^{-1} \sum_{k=0}^{\infty} \frac{1}{k!} = e^{-1} \cdot e = 1$. Now compute:
$$\sum_{k=0}^{N-1} \binom{N-1}{k} \tilde{B}_k = \sum_{k=0}^{N-1} \binom{N-1}{k} e^{-1} \sum_{m=0}^{\infty} \frac{m^k}{m!} = e^{-1} \sum_{m=0}^{\infty} \frac{1}{m!} \sum_{k=0}^{N-1} \binom{N-1}{k} m^k.$$

The inner sum is $(m+1)^{N-1}$ by the binomial theorem. Hence:
$$\sum_{k=0}^{N-1} \binom{N-1}{k} \tilde{B}_k = e^{-1} \sum_{m=0}^{\infty} \frac{(m+1)^{N-1}}{m!} = e^{-1} \sum_{m=0}^{\infty} \frac{m^{N-1}}{(m-1)!} \cdot \text{(reindex)} = \tilde{B}_N.$$

Thus $\tilde{B}_N$ satisfies the same recurrence and initial condition as $B_N$, so $B_N = \tilde{B}_N = e^{-1} \sum_{k=0}^{\infty} k^N / k!$. This is **Dobinski's formula** for Bell numbers.

**Remark.** The sum in (12) is in fact finite in the sense that $k^N/k! \to 0$ rapidly, but it is expressed as an infinite series. The first few values are $B_1 = 1$, $B_2 = 2$, $B_3 = 5$, $B_4 = 15$, $B_5 = 52$.
