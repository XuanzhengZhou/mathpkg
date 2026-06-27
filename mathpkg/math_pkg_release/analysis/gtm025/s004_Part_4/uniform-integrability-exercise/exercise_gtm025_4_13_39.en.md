---
role: exercise
locale: en
chapter: "4"
section: "13"
exercise_number: 39
---

Let $(X, \mathcal{A}, \mu), p, (f_n)$, and $f$ be as in (13.38). Suppose that $f_n \to f$ $\mu$-a.e. For each $(n, k) \in N \times N$ let $B_{n,k} = \{x \in X : |f_n(x)|^p \ge k\}.$

(a) Suppose that condition (13.38.i) holds [as it does, for example, if $\mu(X) < \infty$]. Prove that the following four assertions are equivalent:

(i) $f \in \mathfrak{L}_p$ and $\|f - f_n\|_p \to 0;$

(ii) if $(E_k)_{k=1}^{\infty} \subset \mathcal{A}, E_1 \supset E_2 \supset \cdots,$ and $\bigcap_{k=1}^{\infty} E_k = \varnothing,$ then $\lim_{k \to \infty} \int_{E_k} |f_n|^p d\mu = 0$ uniformly in $n;$

(iii) $\lim_{k \to \infty} \sup_{n \in N} \int_{B_{n,k}} |f_n|^p d\mu = 0;$

(iv) condition (13.38.ii) holds.