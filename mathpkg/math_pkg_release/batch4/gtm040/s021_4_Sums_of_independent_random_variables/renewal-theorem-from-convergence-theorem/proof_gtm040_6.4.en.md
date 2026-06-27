---
role: proof
locale: en
of_concept: renewal-theorem-from-convergence-theorem
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Let the renewal sequence $\{f_n\}_{n \geq 1}$ be given, with $f_n \geq 0$, $\sum_{n=1}^\infty f_n = 1$, and $\gcd\{n : f_n > 0\} = 1$. Define $r_i = \sum_{k > i} f_k$ for $i \geq 0$; note that $r_i 	o 0$ because $\sum f_k = 1$.

As long as $r_i > 0$, define
$$p_{i+1} = rac{r_{i+1}}{r_i} \quad 	ext{for } i = 0, 1, 2, \ldots$$
If $r_i = 0$ for some $i$, set $p_i = 0$ and the remaining $p_k$ are irrelevant. Set $q_i = 1 - p_i$, and let these $p_i, q_i$ be the transition probabilities of the basic example (birth-and-death chain on non-negative integers).

Compute $eta_i = p_1 p_2 \cdots p_i$:
$$eta_i = rac{r_1}{r_0} \cdot rac{r_2}{r_1} \cdots rac{r_i}{r_{i-1}} = rac{r_i}{r_0} = r_i.$$
Since $r_i 	o 0$, we have $eta_i 	o 0$, and therefore the basic example with these parameters is recurrent.

Now the first return probabilities in this chain are:
$$ar{F}_{00}^{(n)} = eta_{n-1} q_n = eta_{n-1}(1 - p_n) = eta_{n-1} - eta_n = r_{n-1} - r_n$$
$$= \sum_{k > n-1} f_k - \sum_{k > n} f_k = f_n.$$

Thus $ar{F}_{00}^{(n)} = f_n$ and consequently $\mu = \sum_n n f_n = ar{M}_{00}$.

The Markov chain is noncyclic by Lemma 6-35, since $\gcd\{n : f_n > 0\} = 1$. Therefore, by the hypothesis (convergence for noncyclic recurrent chains), $\lim_n P_{00}^{(n)}$ exists.

On the other hand, by Lemma 6-34 (the renewal equation), $u_n = P_{00}^{(n)}$ satisfies $u_0 = 1$ and $u_n = \sum_{k=1}^n f_k u_{n-k}$. The existence of $\lim_n u_n$ together with $\sum f_n = 1$ and the noncyclicity condition ($\gcd\{n : f_n > 0\} = 1$) establishes the Renewal Theorem, which asserts that $\lim_n u_n = 1/\mu$ (or 0 if $\mu = \infty$).
