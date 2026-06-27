---
role: proof
locale: en
of_concept: theorem-1-48
source_book: gtm040
source_chapter: "1"
source_section: "48"
---

Proof: Set $g_n(x) = \inf_{k \geq n} f_k(x)$. Then $0 \leq g_1(x) \leq g_2(x) \leq \cdots$, and $g_n$ is measurable on $E$. We have $g_n(x) \leq f_n(x)$ and

$$\lim_n g_n(x) = \liminf_n f_n(x).$$

By Theorem 1-44,

$$\int_E \liminf_n f_n d\mu = \int_E \liminf_n g_n d\mu = \lim_n \int_E g_n d\mu.$$

The result now follows from the inequality $\int_E g_n d\mu \leq \int_E f_n d\mu$.

The fourth basic integration theorem is the Lebesgue Dominated Convergence Theorem.

Theorem 1-49: Let $E$ be a measurable set, and suppose $\{f_n\}$ is a sequence of measurable functions such that for some integrable $g$, $|f_n| \leq g$ for all $n$. If $f(x) = \lim_n f_n(x)$, then $\lim_n \int_E f_n d\mu$ exists and

$$\int_E f d\mu = \lim_n \int_E f_n d\mu.$$

Proof: By property (7) of Proposition 1-39, $f$ is integrable and so is $f_n$ for every $n$. Apply Fatou’s Theorem first to $f_n + g \geq 0$ to obtain $\int_E (f + g) d\mu \leq \liminf \int_E (f_n + g) d\mu$ or

$$\int_E f d\mu \leq \liminf \int_E f_n d\mu.$$

Apply the theorem once more to $g - f_n \geq 0$ to obtain

$$\int_E (g - f) d\mu \leq \liminf \int_E (g - f_n) d\mu$$

or

$$- \int_E f d

Corollary 1-50: Let $E$ be a set of finite measure and suppose $\{f_n\}$ is a sequence of measurable functions such that $|f_n| \leq c$ for all $n$. If $f(x) = \lim_n f_n(x)$, then $\int_E fd\mu = \lim_n \int_E f_nd\mu$.

Much of the discussion of this section has dealt with the following problem: A sequence of integrable functions $f_n$ converges a.e. to a function $f$; we want to be able to conclude that $\int f_n d\mu$ tends to $\int fd\mu$. First we should note that at almost all points $f_n^+ \rightarrow f^+$ and $f_n^- \rightarrow f^-$, and hence it is sufficient to check the convergence of the integral separately for these two sequences. Thus we may consider the case $f_n \geq 0$ alone. For non-negative functions Fatou’s inequality is the only general result; one cannot conclude equality without a further hypothesis. Two sufficient conditions are given by monotone and dominated convergence.

But if we restrict our attention to a space of finite total measure, then we can give a necessary and sufficient condition.

Definition 1-51: A sequence $\{f_n\}$ of non-negative integrable functions is said to be uniformly integrable if for each $\epsilon > 0$ there is a number $k$ such that

$$\int_{\{x | f_n(x) > k\}} f_n d\mu < \epsilon$$

holds for every $n$.

Equivalently we may require that the inequality holds for all sufficiently large $n$. For suppose it holds for $n > N$ and for the number $c$. Then since each $f_n$ is integrable, there is a $k_n$ depending on $n$ (and, of course, $\epsilon$) such that

$$\int_{\{x | f_n(x) > k_n\}} f_n d\mu < \epsilon$$

and we may choose $k = \sup \{k_1, k_2, \ldots, k_N, c\}$.

Proposition 1-52: If $\{f_n\}$ is a sequence of

Proof: We shall use the notation $f^{(k)}$ for the function truncated at $k$; that is, $f^{(k)}(x) = \inf(f(x), k)$. Let

$$A_n = \int_E f d\mu - \int_E f_n d\mu$$

$$B^k = \int_E f d\mu - \int_E f^{(k)} d\mu$$

$$C_n^k = \int_E f^{(k)} d\mu - \int_E f_n^{(k)} d\mu$$

$$D_n^k = \int_E f_n d\mu - \int_E f_n^{(k)} d\mu = \int_{\{x | f_n > k\}} (f_n - k) d\mu.$$

We have

$$A_n = B^k + C_n^k - D_n^k.$$

Clearly $f^{(k)}$ increases monotonically to $f$, so that $B^k$ tends to 0 by monotone convergence. Since $f_n \to f, f_n^{(k)} \to f^{(k)}$. But $f_n^{(k)}$ is bounded by $k$. Thus, on the totally finite measure space $E$, $\lim_n C_n^k = 0$ by Corollary 1-50. Hence by choosing a large $k$ and then a sufficiently large $n$ (depending on $k$), we can make the first two terms on the right side as small as desired. If the functions are uniformly integrable, then we can find a large $k$ (perhaps larger than the one already chosen) for which $D_n^k$ will be small for all $n$. Hence, for all sufficiently large $n$, the left side is small. Thus the integrals converge.

Conversely, suppose that $A_n \to 0$. Then there is a $k$ such that for all sufficiently large $n$, $D_n^k < \epsilon/2$. Thus for all $n$ sufficiently large, we have

$$\epsilon/2 > \int_{\{x | f_n > k\}} (f_n - k) d\mu$$

$$\geq \int_{\{x | f_n > 2k\}} (f_n - k

$\pi f^{(k)}$ converges to $\pi f$. Our object in this section is to obtain sufficient criteria to justify saying that $\pi f = \lim_{k \to \infty} \pi f^{(k)}$.

In the examples of Lebesgue integration, we noted that non-negative row vectors are measures and column vectors are functions. Functions are integrated by forming the matrix product of the measure and the function. Thus, the theorems of Section 4 immediately give us the following four results. In each of them it should be borne in mind that:

(1) There is a corresponding result if row vectors are thought of as functions and column vectors are thought of as measures.

(2) These results imply corresponding results about matrices which are not just row or column vectors. (Recall the discussion in Section 1 about proving matrix equalities entry-by-entry.)
