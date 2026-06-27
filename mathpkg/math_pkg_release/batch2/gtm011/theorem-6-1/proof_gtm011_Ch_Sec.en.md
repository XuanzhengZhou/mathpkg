---
role: proof
locale: en
of_concept: theorem-6-1
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Fix $x_0$ in $X$ and $\epsilon > 0$; we wish to find a $\delta > 0$ such that $\rho(f(x_0), f(x)) < \epsilon$ when $d(x_0, x) < \delta$. Since $f = u - \lim f_n$, there is a function $f_n$ with $\rho(f(x), f_n(x)) < \epsilon/3$ for all $x$ in $X$. Since $f_n$ is continuous there is a $\delta > 0$ such that $\rho(f_n(x_0), f_n(x)) < \epsilon/3$ when $d(x_0, x) < \delta$. Therefore, if $d(x_0, x) < \delta$, $\rho(f(x_0), f(x)) \leq \rho(f(x_0), f_n(x_0)) + \rho(f_n(x_0), f_n(x)) + \rho(f_n(x), f(x)) < \epsilon$.

Let us consider the special case where $\Omega = \mathbb{C}$. If $u_n: X \to \mathbb{C}$, let $f_n(x) = u_1(x) + \ldots + u_n(x)$. We say $f(x) = \sum_{n=1}^{\infty} u_n(x)$ iff $f(x) = \lim f_n(x)$ for each $

Chapter III

Elementary Properties and Examples of Analytic Functions

§1. Power series

In this section the definition and basic properties of a power series will be given. The power series will then be used to give examples of analytic functions. Before doing this it is necessary to give some elementary facts on infinite series in $\mathbb{C}$ whose statements for infinite series in $\mathbb{R}$ should be well known to the reader. If $a_n$ is in $\mathbb{C}$ for every $n \geq 0$ then the series $\sum_{n=0}^{\infty} a_n$ converges to $z$ iff for every $\epsilon > 0$ there is an integer $N$ such that $|\sum_{n=0}^{m} a_n - z| < \epsilon$ whenever $m \geq N$. The series $\sum a_n$ converges absolutely if $\sum |a_n|$ converges.
