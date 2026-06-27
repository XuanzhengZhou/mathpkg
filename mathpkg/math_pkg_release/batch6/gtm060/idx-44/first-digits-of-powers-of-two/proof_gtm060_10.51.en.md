---
role: proof
locale: en
of_concept: first-digits-of-powers-of-two
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

The first digit of $2^n$ equals $d$ (with $d \in \{1, \ldots, 9\}$) precisely when

$$d \cdot 10^k \leq 2^n < (d+1) \cdot 10^k$$

for some integer $k$. Taking logarithms base 10:

$$\log_{10} d + k \leq n \log_{10} 2 < \log_{10}(d+1) + k,$$

which means the fractional part $\{n \log_{10} 2\}$ lies in the interval $[\log_{10} d, \log_{10}(d+1))$ modulo 1.

Since $\log_{10} 2$ is irrational, the sequence $\{n \log_{10} 2\}$ is uniformly distributed on $[0,1)$ by the uniform distribution corollary. Therefore the asymptotic frequency of digit $d$ is

$$\operatorname{mes}[\log_{10} d, \log_{10}(d+1)) = \log_{10}\left(1 + \frac{1}{d}\right).$$

In particular, the ratio of the frequency of $7$ to that of $8$ is

$$\frac{\log_{10}(8/7)}{\log_{10}(9/8)} = \frac{\log 8 - \log 7}{\log 9 - \log 8}.$$
