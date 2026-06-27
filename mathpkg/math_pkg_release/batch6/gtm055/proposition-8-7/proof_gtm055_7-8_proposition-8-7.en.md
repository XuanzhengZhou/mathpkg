---
role: proof
locale: en
of_concept: proposition-8-7
source_book: gtm055
source_chapter: "7-8"
source_section: "Section 09_Section_9"
---

Proof. It is obvious that $\mathcal{L}$ is a linear space and that integration with respect to $\zeta$ is a linear functional on $\mathcal{L}$. In order to verify (8) we note that this inequality is clearly valid when $f$ is a simple function. Indeed, if $s = \sum_{i=1}^{n} \alpha_i \chi_{E_i}$, where the sets $E_i$ are disjoint and measurable, then

$$\left| \int_X s d\zeta \right| = \left| \sum_{i=1}^{n} \alpha_i \zeta(E_i) \right| \leq \sum_{i=1}^{n} |\alpha_i| |\zeta(E_i)| \leq \sum_{i=1}^{n} |\alpha_i| |\zeta|(E_i) = \int_X |s| |d|\zeta|.$$

Since an arbitrary integrable function $f$ is the pointwise limit of a sequence $\{s_n\}$ of integrable simple functions such that $|s_n| \leq |f|$ for all $n$ (Prob. 6S), the proposition follows by the dominated convergence theorems (see Theorem 7.12 and Problem U).

Example K. Let $\alpha$ be a complex-valued function of bounded variation on the interval $[a, b]$, $a \leq b$ (Prob. 1I). Then there exists a unique complex measure $\zeta_\alpha$ on the $\sigma$-ring of Borel subsets of $[a, b]$ satisfying the conditions

$$\zeta_\alpha((s, t)) = \alpha(t-) - \alpha(s+), \quad a \leq s < t \leq b,$$

and

$$\zeta_\alpha(\

of the composition $f \circ \alpha$ with respect to $\alpha$ coincides with the line integral of $f$ along $\alpha$ introduced in Chapter 5:

$$\int_{a}^{b} f \circ \alpha d\zeta_{\alpha} = \int_{\alpha} f(\zeta) d\zeta.$$

Cf. Problem X and Problem 5D.

In Example A, at the very beginning of this chapter, we introduced the notion of Lebesgue measure on the real line $\mathbb{R}$. This historically important concept constitutes the root of the development of all modern real analysis. Up to this point we have concerned ourselves primarily with that portion of real analysis directly associated with the theory of abstract Lebesgue integration and, as a matter of fact, little of the rest of real analysis is needed for our purposes in this book. There are, however, some extremely useful results in the theory of differentiation that we shall want to use later and we conclude this chapter with a brief scrutiny of them. The attentive reader will observe that the arguments and constructions that follow consist largely of unsophisticated calculations depending on little more than elementary arithmetic. Indeed, the bulk of the following discussion might very well have been presented earlier, say in Chapter 3, where the structure of open subsets of $\mathbb{R}$ is set forth. It has been delayed until now because Lebesgue measure is also an essential ingredient in the discussion.

We shall be concerned primarily with continuous real-valued functions on real intervals and their derivatives and difference quotients. Let $f$ be a continuous real-valued function on the closed interval $[a, b]$. If $m$ is a real number and $(c, d)$ an open subinterval of $[a, b]$, then we define the set $R_m = R_m(f; (c, d))$ to consist of all those points $t$ of $(c, d)$ for which there exists a point $u$ in $(t, d)$ such that

$$\frac{f(u) - f(t)}{u - t} > m.$$

Similarly, the set $L_m = L_m(f; (c, d))$ is defined to consist of those points $t$ in $(c, d)$ for which there exists a point $s$ of $(c, t)$ such that

$$\frac{f(s
