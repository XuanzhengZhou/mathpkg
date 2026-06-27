---
role: proof
locale: en
of_concept: newton-method-p-adic
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "2. p-adic equations"
---

*Proof.* Write the Taylor expansion of $f$ about $x$:
$$f(x + p^{\,n-k}t) = f(x) + p^{\,n-k}t f'(x) + p^{\,2n-2k}R,$$
where $R \in \mathbb{Z}_p[t]$, since the higher-order terms of the expansion involve binomial coefficients that are integers. The condition $f(x) \equiv 0 \pmod{p^n}$ means $f(x) = p^n a$ for some $a \in \mathbb{Z}_p$. The condition $v_p(f'(x)) = k$ means $f'(x) = p^k b$ with $b \in \mathbb{Z}_p^\times$ (a $p$-adic unit). We seek $t \in \mathbb{Z}_p$ such that
$$f(x + p^{\,n-k}t) \equiv 0 \pmod{p^{n+1}}.$$
Substituting:
$$p^n a + p^{\,n-k}t \cdot p^k b \equiv 0 \pmod{p^{n+1}},$$
i.e., $p^n(a + t b) \equiv 0 \pmod{p^{n+1}}$, which reduces to $a + tb \equiv 0 \pmod{p}$. Since $b$ is invertible modulo $p$, we can solve $t \equiv -a b^{-1} \pmod{p}$. Set $y = x + p^{\,n-k}t$ for this choice of $t$; then $f(y) \equiv 0 \pmod{p^{n+1}}$, and one verifies that $v_p(f'(y)) = v_p(f'(x)) = k$ (since $y \equiv x \pmod{p^{\,n-k}}$ and $n-k > k$ by the condition $2k < n$).

Applying the lemma to $x^{(0)} = x$ yields $x^{(1)} = y$. Iterating with $n$ replaced by $n+1, n+2, \ldots$, we construct a sequence $x^{(q)}$ satisfying
$$x^{(q+1)} \equiv x^{(q)} \pmod{p^{\,n+q-k}}, \quad f(x^{(q)}) \equiv 0 \pmod{p^{\,n+q}}.$$
This is a Cauchy sequence in $\mathbb{Z}_p$. If $y$ is its limit, we have $f(y) = 0$ and $y \equiv x \pmod{p^{\,n-k}}$, which completes the proof. $\square$
