---
role: proof
locale: en
of_concept: polynomial-ring-over-ufd-is-ufd
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** Throughout this proof one should bear in mind the various assertions of Theorem 6 of §16 (characterizations of UFDs).

**Step 1: Factorization into irreducibles (UF1).** It is clear that an element of $R$ is irreducible (or a unit) in $R[x]$ if and only if it is irreducible (or a unit) in $R$. From this it follows (since $R$ is a UFD) that every polynomial of $R[x]$ of degree zero factors into irreducibles. Suppose $f(x)$ has positive degree $n$ and that factorization has been proved for polynomials of lower degree. Write $f(x) = c f_1(x)$, where $c = c(f) \in R$ and $f_1(x)$ is primitive. Since $c$ factors into irreducibles in $R$ (hence in $R[x]$), we need only prove that $f_1(x)$ is a product of irreducible polynomials.

If $f_1(x)$ is already irreducible, we are done. Otherwise, $f_1(x) = g(x) h(x)$ where neither $g$ nor $h$ is a unit. Since $f_1$ is primitive, both $g$ and $h$ have positive degree (if one had degree zero, it would be a non-unit in $R$, contradicting primitivity of $f_1$). Thus $\partial g < n$ and $\partial h < n$. By the induction hypothesis, $g$ and $h$ factor into irreducibles, hence so does $f_1$. This proves UF1.

**Step 2: Gauss's Lemma (Lemma 1).** $c(fg) = c(f)c(g)$ up to units, and the product of primitive polynomials is primitive. (Proved separately.)

**Step 3: Lemma 2.** If $g(x)$ is primitive and $g(x) \mid b f(x)$ in $R[x]$ with $b \in R$, then $g(x) \mid f(x)$ in $R[x]$. (Proved separately.)

**Step 4: UF3 (prime divisor property).** Suppose $p(x)$ is irreducible in $R[x]$ and $p(x) \mid f(x) g(x)$. We show $p(x) \mid f(x)$ or $p(x) \mid g(x)$.

*Case 1:* $\partial p(x) = 0$. Then $p(x) = p \in R$ is irreducible in $R$, hence prime in $R$. Write $f = c(f) f_1$, $g = c(g) g_1$ with $f_1, g_1$ primitive. Then $p \mid fg = c(f)c(g) f_1 g_1$. By Gauss's Lemma, $f_1 g_1$ is primitive, so the content of $fg$ is $c(f)c(g)$ (up to units). Since $p$ divides this content, and $p$ is prime in $R$, $p \mid c(f)$ or $p \mid c(g)$, hence $p \mid f$ or $p \mid g$ in $R[x]$.

*Case 2:* $\partial p(x) > 0$. Then $p(x)$ is necessarily primitive. Consider the field of fractions $K$ of $R$. In $K[x]$, which is a PID (hence a UFD), irreducible elements are prime. Since $p(x)$ is irreducible in $R[x]$ and primitive, it remains irreducible in $K[x]$, hence is prime in $K[x]$. From $p(x) \mid f(x) g(x)$ in $R[x] \subset K[x]$, we get $p(x) \mid f(x)$ or $p(x) \mid g(x)$ in $K[x]$. Suppose $p(x) \mid f(x)$ in $K[x]$, so $f(x) = p(x) \cdot (a(x)/b)$ with $a(x) \in R[x]$ primitive and $b \in R$. Then $b f(x) = p(x) a(x)$, and by Lemma 2, $p(x) \mid f(x)$ in $R[x]$.

Thus all UF conditions hold for $R[x]$, and $R[x]$ is a unique factorization domain.
