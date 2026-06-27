---
role: proof
locale: en
of_concept: conditional-convergence-rth-mean
source_book: gtm046
source_chapter: "VIII"
source_section: "28.1"
---

**Proof.** Suppose $X_n \xrightarrow{r} X$ for some $r \geq 1$, i.e., $E|X_n - X|^r \to 0$. By the conditional Jensen inequality (or the conditional $c_r$-inequality),

$$E^\mathfrak{B}|E^\mathfrak{B}X_n - E^\mathfrak{B}X|^r = E^\mathfrak{B}|E^\mathfrak{B}(X_n - X)|^r \leq E^\mathfrak{B}E^\mathfrak{B}|X_n - X|^r = E^\mathfrak{B}|X_n - X|^r \quad \text{a.s.}$$

Taking expectations on both sides,

$$E|E^\mathfrak{B}X_n - E^\mathfrak{B}X|^r \leq E|X_n - X|^r \to 0.$$

Thus $E^\mathfrak{B}X_n \xrightarrow{r} E^\mathfrak{B}X$. The inequality uses the fact that $E^\mathfrak{B}$ is a contraction in $L_r$ for $r \geq 1$, which follows from the conditional Jensen inequality since $\varphi(x) = |x|^r$ is convex for $r \geq 1$.
