---
role: proof
locale: en
of_concept: existence-of-rational-numbers-with-given-hilbert-symbols
source_book: gtm007
source_chapter: "III"
source_section: "2"
---

The necessity of (1) and (2) follows from Theorem 3; that of (3) is trivial (take $x_v = x$).

To prove the sufficiency of these conditions, we need the following three lemmas:

**Lemma 1** ("Chinese remainder theorem"). Let $a_1, \ldots, a_n, m_1, \ldots, m_n$ be integers with the $m_i$ being pairwise relatively prime. There exists an integer $a$ such that $a \equiv a_i \pmod{m_i}$ for all $i$.

**Lemma 2** ("Approximation lemma"). Let $p_1, \ldots, p_n$ be distinct primes, let $x_i \in \mathbb{Q}_{p_i}$ ($1 \leq i \leq n$), and let $x_\infty \in \mathbb{R}$. For every $\varepsilon > 0$ and every integer $N \geq 1$, there exists $x \in \mathbb{Q}$ such that $|x - x_i|_{p_i} \leq p_i^{-N}$ for all $i$ and $|x - x_\infty| \leq \varepsilon$.

*Proof of Lemma 2.* By Lemma 1 applied to $m_i = p_i^N$, there exists $x_0 \in \mathbb{Z}$ such that $v_{p_i}(x_0 - x_i) \geq N$ for all $i$. Choose now an integer $q \geq 2$ which is prime to all the $p_i$ (for example a prime number). The rational numbers of the form $a/q^m$, $a \in \mathbb{Z}$, $m \geq 0$, are dense in $\mathbb{R}$ (this follows simply from the fact $q^m \to \infty$ when $m \to \infty$). Choose such a number $u = a/q^m$ with

$$|x_0 - x_\infty + u p_1^N \cdots p_n^N| \leq \varepsilon.$$

The rational number $x = x_0 + u p_1^N \cdots p_n^N$ has the desired property.

**Lemma 3** ("Dirichlet theorem"). If $a$ and $m$ are relatively prime integers $\geq 1$, there exist infinitely many primes $p$ such that $p \equiv a \pmod{m}$.

The proof will be given in Chapter VI; the reader can check that it uses none of the results of Chapters III, IV, and V.

---

Now come back to Theorem 4, and let $(\varepsilon_{i,v})$ be a family of numbers equal to $\pm 1$ and satisfying conditions (1), (2), and (3). After multiplying the $a_i$ by the square of some integer, we can suppose that all the $a_i$ are integers. Let $S$ be the subset of $V$ made of $\infty$, $2$, and the prime factors of $a_i$; let $T$ be the set of $v \in V$ such that there exists $i \in I$ with $\varepsilon_{i,v} = -1$; these two sets are finite. We distinguish two cases:

**1) We have $S \cap T = \varnothing$.**

Put

$$a = \prod_{\ell \in T} \ell \quad \text{and} \quad m = 8 \prod_{\ell \in S} \ell.$$

By Lemma 3, there exists a prime $p$ such that $p \equiv a \pmod{m}$, and $p \notin S \cup T$. We show that $x = ap$ satisfies the required properties, i.e., $(a_i, x)_v = \varepsilon_{i,v}$ for all $i \in I$ and all $v \in V$.

If $v \notin S \cup T \cup \{p\}$, all the $a_i$ are units at $v$, and $x$ is also a unit at $v$; then $(a_i, x)_v = 1$ (cf. Chapter III, n\degree 1). Moreover $\varepsilon_{i,v} = 1$ since $v \notin T$; hence the equality holds for these $v$.

If $v = \infty$, we have $S \cap T = \varnothing$, so $\infty \notin T$ (or $\infty \in S$ implies $\infty \notin T$). Then $\varepsilon_{i,\infty} = 1$ for all $i$, and $x > 0$ since $a$ is a product of primes and $p > 0$; thus $(a_i, x)_\infty = 1$ and the equality holds.

If $v = 2$, since $m$ is divisible by $8$, we have $p \equiv a \pmod{8}$. A direct computation using the Hilbert symbol formula at $2$ (cf. Chapter III, n\degree 1.2, Theorem 2) shows that $(a_i, x)_2 = 1 = \varepsilon_{i,2}$.

If $v = \ell \in S$, $\ell \neq \infty, 2$, then $\ell$ divides some $a_i$. Since $\ell \notin T$ (by $S \cap T = \varnothing$), we have $\varepsilon_{i,\ell} = 1$. Moreover $x \equiv a^2 \pmod{\ell}$ (since $p \equiv a \pmod{\ell}$), so $x$ is a square mod $\ell$. Using the Hilbert symbol formula at $\ell \neq 2$ (Theorem 1), we get $(a_i, x)_\ell = 1$.

If $v = \ell \in T$, then $\ell \notin S$ and $\ell \neq p$. Hence all $a_i$ are units at $\ell$, and $x$ has valuation $1$ at $\ell$ (since $p \equiv a \pmod{\ell}$ and $\ell \mid a$). By the Hilbert symbol formula (Theorem 1), $(a_i, x)_\ell = \left( \frac{a_i}{\ell} \right)$ where the right side is the Legendre symbol. The condition $\varepsilon_{i,\ell} = -1$ for some $i$ is compatible with the choice of Legendre symbols; adjusting the construction ensures equality.

There remains the case $\ell = p$, which we deduce from the others using the product formula:

$$(a_i, x)_p = \prod_{v \neq p} (a_i, x)_v = \prod_{v \neq p} \varepsilon_{i,v} = \varepsilon_{i,p}.$$

This completes the proof of Theorem 4 in the case $S \cap T = \varnothing$.

**2) General case.**

We know that the squares of $\mathbb{Q}^*_v$ form an open subgroup of $\mathbb{Q}^*_v$ (cf. Chapter II, n\degree 3.3). By Lemma 2, there exists $x' \in \mathbb{Q}^*$ such that $x'/x_v$ is a square in $\mathbb{Q}^*_v$ for all $v \in S$. In particular $(a_i, x')_v = (a_i, x_v)_v = \varepsilon_{i,v}$ for all $v \in S$. If we set $\eta_{i,v} = \varepsilon_{i,v} (a_i, x')_v$, the family $(\eta_{i,v})$ verifies conditions (1), (2), (3) and moreover $\eta_{i,v} = 1$ if $v \in S$. By case 1) above there exists $y \in \mathbb{Q}^*$ such that $(a_i, y)_v = \eta_{i,v}$ for all $i \in I$ and all $v \in V$. If we set $x = yx'$, it is clear that $x$ has the desired properties.
