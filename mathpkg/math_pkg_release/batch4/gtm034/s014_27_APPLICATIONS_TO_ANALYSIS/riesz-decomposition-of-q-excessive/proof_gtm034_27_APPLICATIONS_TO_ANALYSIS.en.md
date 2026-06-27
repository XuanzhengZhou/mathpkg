---
role: proof
locale: en
of_concept: riesz-decomposition-of-q-excessive
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

\textbf{Proof of T1:}

Let $\psi(x) = f(x) - Qf(x)$. Since $f$ is $Q$-excessive, $\psi(x) \geq 0$ for all $x \in S$. For any $k \geq 0$,
$$Q_k f(x) - Q_{k+1} f(x) = Q_k \psi(x) \geq 0, \quad x \in S.$$

Define the truncated Green function $g_n(x,y) = \sum_{k=0}^{n} Q_k(x,y)$. Then
$$g_n \psi(x) = \sum_{k=0}^{n} Q_k \psi(x) = \sum_{k=0}^{n} [Q_k f(x) - Q_{k+1} f(x)] = f(x) - Q_{n+1} f(x).$$

Now $g_n(x,y)$ increases monotonically to $g(x,y)$. Since $f$ is non-negative and finite,
$$g_n \psi(x) = f(x) - Q_{n+1} f(x) \leq f(x) < \infty, \quad x \in S.$$
By monotone convergence, $\lim_n g_n \psi(x) = g \psi(x) = u(x) < \infty$, and $u$ is by definition a $Q$-potential.

The existence of $\lim_n g_n \psi$ also implies $\lim_n Q_{n+1} f(x) = h(x) < \infty$. Since $Q_n f$ and $Q_{n+1} f = Q_n(Qf)$ have the same limit,
$$Qh(x) = \lim_{n \to \infty} Q_{n+1} f(x) = h(x), \quad x \in S,$$
so $h$ is $Q$-regular. The decomposition $f = h + u$ follows by taking $n \to \infty$ in $f = Q_{n+1} f + g_n \psi$.

\textit{Uniqueness.} If $f = h' + u'$ with $h'$ regular, $u'$ a potential, then $v = u' - u = h - h'$ satisfies $Qv = v$, hence $Q_n v = v$ for all $n$. But $v$ is the difference of two potentials, so by P1(3), $\lim_n Q_n v = 0$. Thus $v \equiv 0$, giving $h = h'$ and $u = u'$.
