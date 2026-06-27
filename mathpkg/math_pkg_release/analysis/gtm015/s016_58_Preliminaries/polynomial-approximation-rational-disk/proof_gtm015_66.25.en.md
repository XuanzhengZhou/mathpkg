---
role: proof
locale: en
of_concept: polynomial-approximation-rational-disk
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of Polynomial approximation of rational functions on the disk

Proof. Observe that $f(T)$ exists. {Proof: $r(T) \leq \|T\| \leq 1$, therefore $\sigma(T) \subset \Delta_1$.} Explicitly, if $f = p/q$ in reduced form, then $f(T) = p(T)q(T)^{-1}$ (53.5).

If $f$ is already a polynomial, there is nothing to prove. Otherwise $g = 1/q$ is a nonconstant rational function whose poles are exterior to $\Delta_1$; if $a$ is the distance from the origin to the nearest pole of $g$, then $a > 1$ and $g$ has a Taylor expansion

$$g(\lambda) \equiv \sum_{k=0}^{\infty} c_k \lambda^k,$$

valid for $|\lambda| < a$. For $n = 1, 2, 3, \ldots$ let $g_n$ be the polynomial defined by

$$g_n(\lambda) \equiv \sum_{k=0}^{n} c_k \lambda^k;$$

since $a > 1$ we have $g_n(\lambda) \rightarrow g(\lambda)$ uniformly on $\Delta_1$, that is,

(1) $$\|g_n - g\|_{\Delta_1} \rightarrow 0.$$

Form the operators $g_n(T)$ and $g(T) = q(T)^{-1}$. We assert that

(*)

From (2) and (4) we see that $Sq(T) = I$, therefore $S = q(T)^{-1} = g(T)$. This completes the proof of (*).

It follows from (*) that $\|p(T)g_n(T) - p(T)g(T)\| \to 0$; thus, writing $f_n = pg_n$, we have $f_n \in \mathbb{C}[t]$ and $\|f_n(T) - f(T)\| \to 0$.

Von Neumann’s fundamental theorem on spectral sets follows easily:
