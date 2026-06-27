---
role: proof
locale: en
of_concept: kummer-prime-factor-theorem
source_book: gtm050
source_chapter: "4"
source_section: "4.3"
---

The proof proceeds in several steps.

**Step 1: The case $p = \lambda$.** One proves directly that $\alpha - 1$ is prime. Since $\alpha - 1$ divides $N(\alpha - 1) = \lambda$ but does not divide $1$, an integer is divisible by $\alpha - 1$ only if it is divisible by $\lambda$. Moreover, $\alpha \equiv 1 \pmod{\alpha - 1}$. If $\alpha - 1$ divides $f(\alpha)g(\alpha)$, then $f(\alpha)g(\alpha) \equiv 0 \pmod{\alpha - 1}$, so $f(1)g(1) \equiv 0 \pmod{\alpha - 1}$. Since $f(1)g(1)$ is an integer, this implies $f(1)g(1) \equiv 0 \pmod{\lambda}$. Because $\lambda$ is prime, either $f(1) \equiv 0 \pmod{\lambda}$ or $g(1) \equiv 0 \pmod{\lambda}$, hence $f(1) \equiv 0 \pmod{\alpha - 1}$ or $g(1) \equiv 0 \pmod{\alpha - 1}$. By the congruence $\alpha \equiv 1 \pmod{\alpha-1}$, this gives $f(\alpha) \equiv 0 \pmod{\alpha-1}$ or $g(\alpha) \equiv 0 \pmod{\alpha-1}$, so $\alpha-1$ is prime. Any $h(\alpha)$ with $Nh(\alpha) = \lambda$ must be a unit multiple of $\alpha-1$, and the value of $k$ must satisfy $k \equiv 1 \pmod{\lambda}$.

**Step 2: Reduction to $p \equiv 1 \pmod{\lambda}$.** Since $p = Nh(\alpha) \equiv 0$ or $1 \pmod{\lambda}$ (as already established from divisibility of binomials), we may assume $p \equiv 1 \pmod{\lambda}$. Write $p - 1 = \mu \lambda$.

**Step 3: The congruence $k^\lambda \equiv 1 \pmod{p}$.** Since $\alpha^{\lambda-1} + \alpha^{\lambda-2} + \cdots + \alpha + 1 = 0$ is divisible by $h(\alpha)$, we have $k^{\lambda-1} + k^{\lambda-2} + \cdots + k + 1 \equiv 0 \pmod{p}$, hence $k^\lambda \equiv 1 \pmod{p}$.

**Step 4: Existence of $\lambda$ distinct solutions.** Let $\gamma$ be a primitive root modulo $p$. Then $\gamma^i$ satisfies $(\gamma^i)^\lambda \equiv 1 \pmod{p}$ if and only if $(p-1)/\lambda = \mu$ divides $i$, i.e., $i = \mu, 2\mu, \ldots, \lambda\mu = p-1$. Setting $m = \gamma^\mu$, the values $k = m, m^2, \ldots, m^\lambda \equiv 1$ are $\lambda$ distinct solutions modulo $p$.

**Step 5: The Lemma.** $h(m)h(m^2) \cdots h(m^{\lambda-1}) \equiv 0 \pmod{p}$. This follows from the factorization $N(\alpha - k) = (k^\lambda - 1)/(k - 1)$. Since $k^\lambda \equiv 1 \pmod{p}$ for each $k = m^j$, we have $N(\alpha - m^j) \equiv 0 \pmod{p}$ for $j = 1, 2, \ldots, \lambda-1$. Consequently, $h(\alpha)$ must divide some $\alpha - m^j$, and thus $h(\alpha)$ divides $\alpha - k$ for some $k$.

**Step 6: $h(\alpha)$ is prime.** If $h(\alpha)$ divides $f(\alpha)g(\alpha)$, then $f(\alpha)g(\alpha) \equiv 0 \pmod{h(\alpha)}$. Since $\alpha \equiv k \pmod{h(\alpha)}$, we have $f(k)g(k) \equiv 0 \pmod{h(\alpha)}$. Because $f(k)g(k)$ and $p$ are integers, if $f(k)g(k) \not\equiv 0 \pmod{p}$, then $1$ can be written as a combination of $f(k)g(k)$ and $p$, which would imply $1 \equiv 0 \pmod{h(\alpha)}$, a contradiction. Hence $f(k)g(k) \equiv 0 \pmod{p}$. Since $p$ is prime, $f(k) \equiv 0 \pmod{p}$ or $g(k) \equiv 0 \pmod{p}$, which gives $f(k) \equiv 0 \pmod{h(\alpha)}$ or $g(k) \equiv 0 \pmod{h(\alpha)}$, and finally $f(\alpha) \equiv 0 \pmod{h(\alpha)}$ or $g(\alpha) \equiv 0 \pmod{h(\alpha)}$. Thus $h(\alpha)$ is prime.
