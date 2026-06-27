---
role: proof
locale: en
of_concept: characterization-of-liminf-and-limsup
source_book: gtm012
source_chapter: "3"
source_section: "3. Sequences of real and complex numbers"
---

# Proof of Characterization of liminf and limsup (Proposition 3.4)

**Proposition 3.4.** Suppose $(x_n)_{n=1}^{\infty}$ is a bounded sequence in $\mathbb{R}$. Then:

$\liminf_{n \to \infty} x_n$ is the unique number $x'$ such that

(i)$'$  for any $\varepsilon > 0$, there is an $N$ such that $x_n > x' - \varepsilon$ whenever $n \geq N$,

(ii)$'$ for any $\varepsilon > 0$ and any $N$, there is an $n \geq N$ such that $x_n < x' + \varepsilon$.

$\limsup_{n \to \infty} x_n$ is the unique number $x''$ with the properties

(i)$''$  for any $\varepsilon > 0$, there is an $N$ such that $x_n < x'' + \varepsilon$ whenever $n \geq N$,

(ii)$''$ for any $\varepsilon > 0$ and any $N$, there is an $n \geq N$ such that $x_n > x'' - \varepsilon$.

**Proof.**

**Part 1: Lower limit.** Recall that $\liminf x_n = \lim_{n \to \infty} x'_n$ where $x'_n = \inf\{x_m : m \geq n\}$.

First we verify that $x' = \liminf x_n$ satisfies (i)$'$ and (ii)$'$.

For (i)$'$: Since $x'_n \to x'$, given $\varepsilon > 0$ there exists $N$ such that $|x'_n - x'| < \varepsilon$ for $n \geq N$. In particular, $x'_n > x' - \varepsilon$ for $n \geq N$. By definition of infimum, $x_n \geq x'_n$ for all $n$, so $x_n > x' - \varepsilon$ for all $n \geq N$.

For (ii)$'$: Given $\varepsilon > 0$ and $N$, since $x'_n \to x'$, there exists $n \geq N$ such that $x'_n < x' + \varepsilon$. By definition of infimum, $x'_n = \inf\{x_m : m \geq n\}$, so there exists $m \geq n \geq N$ such that $x_m < x'_n + \varepsilon$. But $x'_n < x' + \varepsilon$, so $x_m < x' + 2\varepsilon$. Since $\varepsilon$ is arbitrary, this establishes (ii)$'$ (up to re-scaling $\varepsilon$).

Next we prove uniqueness. Suppose $y_1$ and $y_2$ both satisfy (i)$'$ and (ii)$'$. We show $y_1 = y_2$. Assume $y_1 < y_2$ and set $\varepsilon = (y_2 - y_1)/2 > 0$. By (i)$'$ for $y_1$, there exists $N_1$ such that $x_n > y_1 - \varepsilon$ for $n \geq N_1$. By (ii)$'$ for $y_2$ (with $N = N_1$), there exists $n \geq N_1$ such that $x_n < y_2 + \varepsilon$. But then $y_1 + \varepsilon = y_2 - \varepsilon < x_n$, contradicting $x_n < y_2 + \varepsilon = y_1 + 3\varepsilon$. The symmetric argument rules out $y_1 > y_2$. Hence $y_1 = y_2$.

**Part 2: Upper limit.** Recall that $\limsup x_n = \lim_{n \to \infty} x''_n$ where $x''_n = \sup\{x_m : m \geq n\}$.

We verify that $x'' = \limsup x_n$ satisfies (i)$''$ and (ii)$''$.

For (i)$''$: Since $x''_n \to x''$, given $\varepsilon > 0$ there exists $N$ such that $|x''_n - x''| < \varepsilon$ for $n \geq N$. In particular, $x''_n < x'' + \varepsilon$ for $n \geq N$. By definition of supremum, $x_n \leq x''_n$ for all $n$, so $x_n < x'' + \varepsilon$ for all $n \geq N$.

For (ii)$''$: Given $\varepsilon > 0$ and $N$, since $x''_n \to x''$, there exists $n \geq N$ such that $x''_n > x'' - \varepsilon$. By definition of supremum, $x''_n = \sup\{x_m : m \geq n\}$, so there exists $m \geq n \geq N$ such that $x_m > x''_n - \varepsilon > x'' - 2\varepsilon$. Re-scaling $\varepsilon$ yields (ii)$''$.

Uniqueness for $x''$ follows by an argument entirely dual to the one for $x'$. $\square$
