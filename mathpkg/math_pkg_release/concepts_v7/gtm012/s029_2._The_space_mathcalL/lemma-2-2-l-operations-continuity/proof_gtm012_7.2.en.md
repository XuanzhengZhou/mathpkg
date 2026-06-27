---
role: proof
locale: en
of_concept: lemma-2-2-l-operations-continuity
source_book: gtm012
source_chapter: "7"
source_section: "§2. The space $\mathcal{L}$"
---

# Proof of Continuity of Operations on $\mathcal{L}$

**Lemma 2.2.** The operations of differentiation, translation, complex conjugation, and integration are continuous from $\mathcal{L}$ to $\mathcal{L}$ with respect to convergence in the sense of $\mathcal{L}$. Moreover, if $u \in \mathcal{L}$ then the difference quotient

$$s^{-1}(T_{-s}u - u) \rightarrow Du \quad (\mathcal{L})$$

as $s \rightarrow 0$.

**Proof.** These statements chiefly involve routine verifications. We shall prove the final statement. Given an integer $k \geq 0$, let $v = D^k u$. Suppose $t \geq M$ and $0 < |s| \leq 1$. The Mean Value Theorem implies

$$s^{-1}[T_{-s}v(t) - v(t)] = Dv(r)$$

where $|t - r| < |s|$. Then

$$D^k \{s^{-1}[T_{-s}u(t) - u(t)]\} - D^k Du(t) = Dv(r) - Dv(t)$$
$$= D^{k+1}u(r) - D^{k+1}u(t).$$

But

$$|D^{k+1}u(r) - D^{k+1}u(t)| \leq c(a, M)e^{-at}, \quad t \geq M.$$

This follows because $u \in \mathcal{L}$ implies each derivative $D^{k+1}u$ decays faster than any $e^{-at}$, and by the Mean Value Theorem, the difference $|D^{k+1}u(r) - D^{k+1}u(t)|$ is controlled by the supremum of $|D^{k+2}u|$ on an interval, which itself satisfies such a bound.

The left side of the inequality above converges to zero as $s \rightarrow 0$, uniformly on bounded intervals. It follows that

$$|s^{-1}[T_{-s}u - u] - Du|_{k,a',M} \rightarrow 0$$

as $s \rightarrow 0$, for any $a' < a$. $\square$

**Explanation.** The proof uses the seminorm characterization of convergence in $\mathcal{L}$: $u_n \rightarrow u$ in $\mathcal{L}$ iff $|u_n - u|_{k,a,M} \rightarrow 0$ for all $k, a, M$. The key technical point is the bound (8), which relies on the rapid decay property of functions in $\mathcal{L}$: if $u \in \mathcal{L}$ then for any $a$, $D^{k+1}u(t)$ is $O(e^{-at})$ as $t \rightarrow +\infty$, uniformly on $[M, \infty)$. By reducing $a$ slightly to $a'$, the same bound holds for the difference quotient, establishing convergence in all seminorms.
