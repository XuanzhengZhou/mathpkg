---
role: proof
locale: en
of_concept: proposition-1-55
source_book: gtm040
source_chapter: "1"
source_section: "55"
---

Proof: The result follows from Corollary 1-50.

A harder problem arises with a sequence of non-negative row vectors $\pi^{(k)}$ converging to a row vector $\pi$. It is not sufficient for $\pi^{(k)} 1 \leq M$ and $|f| \leq c1$ in order for $\pi f = \lim_k \pi^{(k)} f$. For set

$$\pi^{(1)} = (1 \quad 0 \quad 0 \quad 0 \quad \ldots)$$

$$\pi^{(2)} = (0 \quad 1 \quad 0 \quad 0 \quad \ldots)$$

$$\pi^{(3)} = (0 \quad 0 \quad 1 \quad 0 \quad \ldots)$$

$$\vdots$$

and take $f = 1$. Then $\pi = 0$ so that $\pi f = 0$, while $\lim_k \pi^{(k)} f = 1$. We give two sufficient conditions for

$$\pi f = \lim_k \pi^{(k)} f;$$

our integration theorems do not provide us with quick proofs, however. The second proposition is closely related to the Silverman–Toeplitz Theorem on summability methods.

Proposition 1-57: If $\{\pi^{(k)}\}$ is a sequence of non-negative row vectors converging to $\pi$, if $f$ is a column vector such that $0 \leq f \leq c1$ for some $c$, and if $\pi 1 = \lim_k \pi^{(k)} 1$ with $\pi 1$ finite, then

$$\pi f = \lim_k \pi^{(k)} f.$$

Proof: Take $f$ as a measure and $\{\pi^{(k)}\}$ as a sequence of non-negative functions and apply Fatou

Proposition 1-58: Let $\{\pi^{(k)}\}$ be a sequence of row vectors converging to $\pi$ and satisfying $|\pi^{(k)}|1 \leq M$. Suppose $f$ is a column vector with the property that for any $\delta > 0$ only finitely many entries of $f$ have absolute value greater than $\delta$. Then

$$\pi f = \lim_{k} \pi^{(k)}f.$$

Proof: The entries of $f$ are clearly bounded, say by $c$. Numbering the entries, we have for every $N$

$$|\pi f - \pi^{(k)}f| \leq \sum_{j=1}^{N} |\pi_j - \pi_j^{(k)}| |f_j| + \sum_{j>N} (|\pi_j| + |\pi_j^{(k)}|)|f_j|.$$

Let $\epsilon > 0$ be given. Choose $N$ sufficiently large that $|f_j| < \epsilon/4M$ for $j > N$. Choose $k$ sufficiently large that $|\pi_j - \pi_j^{(k)}| < \epsilon/2cN$ for $j \leq N$. Then $|\pi f - \pi^{(k)}f| < \epsilon$, and the result is established.

As we noted in Section 1, results about general denumerable matrices can be reduced to results about row and column vectors. In particular, the propositions of the present section apply equally well to sequences of the forms $\{A^{(k)}f\}$ and $\{\pi A^{(k)}\}$.

6. Some general theorems from analysis

In this section we collect a variety of results from analysis which we shall need in later chapters. We prove only some of them. At first reading the reader may find it wise to skip this section, returning to it later as the material is required.

a. Stirling's formula. Stirling's formula gives an asymptotic expression for $m!$. The approximation is

$$m! \sim \frac{m^m}{e^m} \sqrt{2\pi m},$$

where the symbol $\sim$ indicates that the ratio of the two quantities tends to one as $m$ increases. For a proof, see Courant and Hilbert [1953],

The multinomial coefficient $\binom{a}{b, c, \ldots, d}$ is defined to be $\frac{a!}{b!c! \ldots d!}$.

b. Difference equations. An $n$th order linear difference equation with constant coefficients is an expression of the form

$$y_{k+n} + c_{n-1}y_{k+n-1} + \cdots + c_1y_{k+1} + c_0y_k = r_k,$$

where $y_k$ and $r_k$ are functions defined on the integers and where the $c_{n-1}, \ldots, c_0$ are complex numbers. The equation is homogeneous if $r_k = 0$ and nonhomogeneous otherwise. For a nonhomogeneous solution, we refer to any single function $y_k$ satisfying the equation as a particular solution, and we call the set of functions satisfying the same equation with $r_k = 0$ the homogeneous solution. The totality of solutions to any difference equation is known as the general solution.

Proposition 1-60: Every solution of the difference equation

$$y_{k+n} + c_{n-1}y_{k+n-1} + \cdots + c_0y_k = 0$$

is a linear combination of $n$ fixed functions, obtained as follows: If $a$ is a root of multiplicity $q$ of the characteristic equation

$$x^n + c_{n-1}x^{n-1} + \cdots + c_1x + c_0 = 0,$$

then $q$ of the functions are

$$a^k, ka^k, k^2a^k, \ldots, k^{q-1}a^k.$$

Conversely, each of these functions is a solution of the difference equation. Furthermore, each solution of the equation

$$y_{k+n} + c_{n-1}y_{k+n-1} + \cdots + c_0y_k = r_k$$

is the sum of a fixed particular solution and some solution of

$$y_{k+n} + c_{n-1}y_{k+n-1} + \cdots + c_0y_k = 0.$

is defined entry-by-entry: $B_{ij}^{(n)}$ is the Cesaro average of $A_{ij}^{(1)}, A_{ij}^{(2)}, \ldots, A_{ij}^{(n)}$. The basic fact about Cesaro summability is the following proposition.
