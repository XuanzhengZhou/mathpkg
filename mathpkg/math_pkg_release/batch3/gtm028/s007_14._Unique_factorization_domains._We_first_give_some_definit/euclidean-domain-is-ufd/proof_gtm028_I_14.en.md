---
role: proof
locale: en
of_concept: euclidean-domain-is-ufd
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

We show that a euclidean domain $E$ satisfies UF1 and UF3 (see the equivalence theorem for UFD conditions).

**Verification of UF1.** Let $a$ be an arbitrary non-unit. If $\varphi(a) = \varphi(1)$, this equality is impossible for a non-unit by the unit characterization. We use induction on $\varphi(a)$. Assume UF1 holds for all elements $a'$ with $\varphi(a') < \varphi(a)$. If $a$ is irreducible, UF1 is trivially satisfied. Otherwise $a = bc$ where neither $b$ nor $c$ is an associate of $a$. Then by E1 and property (c) of the unit characterization, $\varphi(b) < \varphi(a)$ and $\varphi(c) < \varphi(a)$. By the induction hypothesis, both $b$ and $c$ are finite products of irreducible factors, hence so is $a$. This completes the induction.

**Verification of UF3.** We first prove the following lemma (written separately as gcd-linear-combination-euclidean): any two non-zero elements $a, b \in E$ have a GCD $d$, and $d$ is a linear combination $d = \alpha a + \beta b$ with $\alpha, \beta \in E$.

Using this lemma, we prove UF3. Let $p$ be irreducible and suppose $p \mid ab$. If $p \nmid a$, then the GCD of $p$ and $a$ is a unit (since $p$ is irreducible). By the lemma, there exist $\alpha, \beta \in E$ such that $1 = \alpha p + \beta a$. Multiplying by $b$ gives $b = \alpha p b + \beta a b$. Since $p \mid ab$, $p$ divides the right-hand side, so $p \mid b$. Thus UF3 holds.

Since UF1 and UF3 are equivalent to UF1 and UF2, $E$ is a UFD.
