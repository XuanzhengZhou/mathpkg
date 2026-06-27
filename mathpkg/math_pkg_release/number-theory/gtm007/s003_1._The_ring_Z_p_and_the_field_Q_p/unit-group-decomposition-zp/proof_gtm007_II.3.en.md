---
role: proof
locale: en
of_concept: unit-group-decomposition-zp
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "3. The multiplicative group of Q_p"
---

*Proof.* Consider the reduction map modulo $p$:
$$\varepsilon_1: U \longrightarrow \mathbb{F}_p^*, \quad x \mapsto x \bmod p.$$
The kernel of $\varepsilon_1$ is precisely $U_1 = \{x \in U : x \equiv 1 \pmod{p}\}$. The map $\varepsilon_1$ is surjective: for any $a \in \mathbb{F}_p^*$, lift $a$ to an integer $\tilde{a} \in \mathbb{Z}$ not divisible by $p$; then $\tilde{a} \in U$ by Proposition 2(a) and $\varepsilon_1(\tilde{a}) = a$. Thus we have an exact sequence
$$0 \longrightarrow U_1 \longrightarrow U \longrightarrow \mathbb{F}_p^* \longrightarrow 0.$$
Now, $|\mathbb{F}_p^*| = p-1$ and we will see that $U_1$ is a pro-$p$ group (its order, as a projective limit, involves only powers of $p$). Since $p-1$ and $p$ are coprime, we can apply the lemma on group extensions with coprime orders. The $(p-1)$-torsion subgroup $V$ of $U$ is given by
$$V = \{x \in U : x^{p-1} = 1\}.$$
By the lemma, $U = V \times U_1$ and $V$ is the unique subgroup of $U$ isomorphic to $\mathbb{F}_p^*$. The elements of $V$ are precisely the Teichmüller representatives of $\mathbb{F}_p^*$ in $\mathbb{Z}_p$.

For completeness, we also describe the filtration: $U_n = \{x \in U : x \equiv 1 \pmod{p^n}\}$ for $n \geq 1$. The map $x \mapsto (x-1)/p^n$ induces an isomorphism
$$U_n/U_{n+1} \xrightarrow{\sim} \mathbb{Z}/p\mathbb{Z},$$
which follows from the formula $(1+p^n x)(1+p^n y) \equiv 1 + p^n(x+y) \pmod{p^{n+1}}$. By induction, $U_1/U_n$ has order $p^{n-1}$. $\square$
