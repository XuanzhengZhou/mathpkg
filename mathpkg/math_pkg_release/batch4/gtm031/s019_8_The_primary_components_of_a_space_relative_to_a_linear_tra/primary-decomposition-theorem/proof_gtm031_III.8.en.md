---
role: proof
locale: en
of_concept: primary-decomposition-theorem
source_book: gtm031
source_chapter: "III"
source_section: "8"
---

Let $\mu(\lambda)$ be the minimum polynomial of $A$ with factorization
$$
\mu(\lambda) = \pi_1(\lambda)^{k_1} \pi_2(\lambda)^{k_2} \cdots \pi_s(\lambda)^{k_s}
$$
into powers of distinct irreducible polynomials with leading coefficient $1$. Set
$$
\mu_i(\lambda) = \mu(\lambda) / \pi_i(\lambda)^{k_i} = \prod_{j \neq i} \pi_j(\lambda)^{k_j}, \qquad i = 1, 2, \dots, s.
$$

The polynomials $\mu_1(\lambda), \mu_2(\lambda), \dots, \mu_s(\lambda)$ are relatively prime (any common divisor would have to contain some $\pi_i(\lambda)$, but $\mu_i(\lambda)$ omits $\pi_i(\lambda)^{k_i}$). Hence there exist polynomials $\phi_1(\lambda), \phi_2(\lambda), \dots, \phi_s(\lambda)$ such that
$$
\phi_1(\lambda)\mu_1(\lambda) + \phi_2(\lambda)\mu_2(\lambda) + \cdots + \phi_s(\lambda)\mu_s(\lambda) = 1.
$$

Define $E_i = \phi_i(A)\mu_i(A)$ for $i = 1, 2, \dots, s$. Since $\mu_i(\lambda)\mu_j(\lambda)$ is divisible by $\mu(\lambda)$ whenever $i \neq j$, we have $\mu_i(A)\mu_j(A) = 0$, and therefore
$$
E_i E_j = \phi_i(A)\mu_i(A)\phi_j(A)\mu_j(A) = \phi_i(A)\phi_j(A)\mu_i(A)\mu_j(A) = 0 \qquad (i \neq j).
$$

From the Bezout relation evaluated at $A$ we obtain
$$
E_1 + E_2 + \cdots + E_s = 1.
$$

Multiplying this relation by $E_i$ and using $E_iE_j = 0$ for $i \neq j$ yields
$$
E_i^2 = E_i.
$$

Thus the $E_i$ are pairwise orthogonal idempotents summing to $1$, so they are projections and
$$
\Re = \Re E_1 \oplus \Re E_2 \oplus \cdots \oplus \Re E_s.
$$

Since each $E_i$ is a polynomial in $A$, it commutes with $A$; consequently each subspace $\Re E_i$ is invariant under $A$.

We now show that $\Re E_i = \Re_i = \{\, x_i \in \Re \mid x_i \pi_i(A)^{k_i} = 0 \,\}$.

First, let $y_i \in \Re E_i$. Then $y_i = u E_i = u \phi_i(A)\mu_i(A)$ for some $u \in \Re$. Since $\mu_i(\lambda)\pi_i(\lambda)^{k_i} = \mu(\lambda)$, we have
$$
y_i \pi_i(A)^{k_i} = u \phi_i(A)\mu_i(A)\pi_i(A)^{k_i} = u \phi_i(A)\mu(A) = 0,
$$
because $\mu(A) = 0$ by definition of the minimum polynomial. Hence $y_i \in \Re_i$, proving $\Re E_i \subseteq \Re_i$.

Conversely, let $x = x_1 + x_2 + \cdots + x_s$ where $x_j \in \Re E_j$, and suppose $x \in \Re_i$, i.e., $x \pi_i(A)^{k_i} = 0$. Then
$$
0 = x \pi_i(A)^{k_i} = x_1 \pi_i(A)^{k_i} + x_2 \pi_i(A)^{k_i} + \cdots + x_s \pi_i(A)^{k_i}.
$$
Since $A$ (and hence $\pi_i(A)^{k_i}$) commutes with each $E_j$, each summand $x_j \pi_i(A)^{k_i}$ belongs to $\Re E_j$. By the direct sum decomposition, each component must vanish separately:
$$
x_j \pi_i(A)^{k_i} = 0 \qquad \text{for all } j.
$$

For $j = i$, this gives $x_i \pi_i(A)^{k_i} = 0$, which is consistent with $x_i \in \Re E_i \subseteq \Re_i$ (already shown above). For $j \neq i$, the polynomials $\pi_i(\lambda)^{k_i}$ and $\pi_j(\lambda)^{k_j}$ are relatively prime. Since $x_j \in \Re E_j \subseteq \Re_j$, we also have $x_j \pi_j(A)^{k_j} = 0$. Thus $x_j$ is annihilated by both $\pi_i(A)^{k_i}$ and $\pi_j(A)^{k_j}$. Because these polynomials are relatively prime, there exist $a(\lambda), b(\lambda)$ with
$$
a(\lambda)\pi_i(\lambda)^{k_i} + b(\lambda)\pi_j(\lambda)^{k_j} = 1.
$$
Evaluating at $A$ and applying to $x_j$, we obtain
$$
x_j = x_j a(A)\pi_i(A)^{k_i} + x_j b(A)\pi_j(A)^{k_j} = 0 + 0 = 0.
$$
Hence $x_j = 0$ for all $j \neq i$, and $x = x_i \in \Re E_i$. This proves $\Re_i \subseteq \Re E_i$.

Therefore $\Re_i = \Re E_i$ and we have the direct sum decomposition
$$
\Re = \Re_1 \oplus \Re_2 \oplus \cdots \oplus \Re_s.
$$

To determine the minimum polynomial of $A|_{\Re_i}$, let $m_i(\lambda)$ be this polynomial. Since $\Re_i$ consists of vectors annihilated by $\pi_i(A)^{k_i}$, we have $\pi_i(A|_{\Re_i})^{k_i} = 0$, so $m_i(\lambda) \mid \pi_i(\lambda)^{k_i}$. On the other hand, because $\Re = \bigoplus \Re_i$, the minimum polynomial $\mu(\lambda)$ of $A$ is the least common multiple of the $m_i(\lambda)$. Since the $\pi_i(\lambda)$ are distinct irreducibles and $\mu(\lambda) = \prod \pi_i(\lambda)^{k_i}$, the only way this can happen is if $m_i(\lambda) = \pi_i(\lambda)^{k_i}$ for each $i$. Thus the minimum polynomial of the induced transformation on $\Re_i$ is $\pi_i(\lambda)^{k_i}$, completing the proof.
