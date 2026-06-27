---
role: proof
locale: en
of_concept: lemma-projective-limit-no-p-torsion
source_book: gtm059
source_chapter: "Iwasawa Theory of Local Units"
source_section: "2"
---

**Proof.** Suppose, for contradiction, that there exists a nontrivial $\mathbb{Z}_p$-torsion element in $U$. Then there is a fixed power $p^m$ and a nonzero element $u = \varprojlim u_n \in U$ such that $p^m u = 0$ in $U$, i.e., $p^m u_n = 0$ for all $n$. Since each $U_n$ is the group of principal units congruent to $1$ modulo the maximal ideal in $K_n$, its torsion subgroup consists precisely of the $p$-power roots of unity $\mu_{p^n}$ contained in $K_n$.

Now, if $u \neq 0$ in $U$, then for sufficiently large $n$, the component $u_n$ is a nontrivial $p^m$-torsion element in $U_n$. By the structure of the torsion in $U_n$, this implies $u_n$ is a primitive $p^r$-th root of unity for some $r \le m$. For $m \ge n$, the norm maps $N_{m,n}: U_m \to U_n$ act on roots of unity by raising to the power $[K_m:K_n] = p^{m-n}$. Hence the projective limit of torsion elements would correspond to a compatible system of roots of unity of unbounded order, which cannot exist in a fixed $K_n$. This contradiction proves that $U$ has no $\mathbb{Z}_p$-torsion. $\square$
