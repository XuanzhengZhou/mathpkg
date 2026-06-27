---
role: proof
locale: en
of_concept: hecke-fp-operator-automorphy
source_book: gtm041
source_chapter: "4"
source_section: "4.5"
---

*Proof.* First we compute the Fourier expansion of $f_p$. Substituting the expansion of $f$ into the definition of $f_p$,

$$
\begin{aligned}
f_p(\tau) &= \frac{1}{p} \sum_{\lambda=0}^{p-1} f\!\left(\frac{\tau + \lambda}{p}\right) \\
&= \frac{1}{p} \sum_{\lambda=0}^{p-1} \sum_{n=-m}^{\infty} a(n) \exp\!\left(2\pi i n \frac{\tau + \lambda}{p}\right) \\
&= \sum_{n=-m}^{\infty} a(n) e^{2\pi i n \tau/p} \cdot \frac{1}{p} \sum_{\lambda=0}^{p-1} e^{2\pi i n \lambda/p}.
\end{aligned}
$$

The inner sum over $\lambda$ is a geometric series:

$$
\sum_{\lambda=0}^{p-1} e^{2\pi i n \lambda/p} =
\begin{cases}
0 & \text{if } p \nmid n, \\[4pt]
p & \text{if } p \mid n.
\end{cases}
$$

Hence only terms with $n$ divisible by $p$ survive. Writing $n = kp$ and summing over $k$,

$$
f_p(\tau) = \sum_{k=-[m/p]}^{\infty} a(kp) e^{2\pi i k \tau}.
$$

This shows that $f_p$ has the correct behavior at the cusp $\tau = i\infty$: its $q$-expansion ($q = e^{2\pi i\tau}$) involves only integer powers of $q$, as required for an automorphic function under $\Gamma_0(p)$. Moreover, $f_p$ is clearly meromorphic in the upper half-plane $H$ because it is a finite linear combination of functions meromorphic in $H$.

It remains to prove the transformation property

$$
f_p(V\tau) = f_p(\tau) \quad \text{for all } V \in \Gamma_0(p).
$$

Let $T_\lambda \tau = (\tau + \lambda)/p$. Then

$$
f_p(V\tau) = \frac{1}{p} \sum_{\lambda=0}^{p-1} f\!\left(\frac{V\tau + \lambda}{p}\right) = \frac{1}{p} \sum_{\lambda=0}^{p-1} f(T_\lambda V \tau).
$$

By Lemma 1, for each $\lambda$ there exist $\mu$ (with $0 \leq \mu \leq p-1$) and $W_\mu \in \Gamma_0(p^2)$ such that $T_\lambda V = W_\mu T_\mu$. Since $f$ is automorphic under the full group $\Gamma$ and $\Gamma_0(p^2) \subset \Gamma$, we have $f(W_\mu T_\mu \tau) = f(T_\mu \tau)$. Therefore

$$
\frac{1}{p} \sum_{\lambda=0}^{p-1} f(T_\lambda V \tau) = \frac{1}{p} \sum_{\lambda=0}^{p-1} f(W_\mu T_\mu \tau) = \frac{1}{p} \sum_{\lambda=0}^{p-1} f(T_\mu \tau).
$$

Lemma 1 also asserts that as $\lambda$ runs through a complete residue system modulo $p$, so does $\mu$. Hence the right-hand sum is exactly $f_p(\tau)$, and we obtain $f_p(V\tau) = f_p(\tau)$ for all $V \in \Gamma_0(p)$. ∎
