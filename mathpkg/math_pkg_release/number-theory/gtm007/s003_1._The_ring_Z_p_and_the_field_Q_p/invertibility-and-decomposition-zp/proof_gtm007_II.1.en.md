---
role: proof
locale: en
of_concept: invertibility-and-decomposition-zp
source_book: gtm007
source_chapter: "II. p-Adic Fields"
source_section: "1. The ring Z_p and the field Q_p"
---

*Proof.* **(a)** It suffices to prove the statement for $A_n = \mathbb{Z}/p^n\mathbb{Z}$; the case of $\mathbb{Z}_p$ will follow by taking projective limits. If $x \in A_n$ does not belong to $pA_n$, its image in $A_1 = \mathbb{F}_p$ is nonzero, hence invertible. Thus there exist $y, z \in A_n$ such that $xy = 1 - pz$. Consequently,
$$xy(1 + pz + p^2 z^2 + \cdots + p^{n-1} z^{n-1}) = 1 - p^n z^n = 1 \quad \text{in } A_n,$$
which proves that $x$ is invertible. Conversely, if $x$ is divisible by $p$, its image in $A_1 = \mathbb{F}_p$ is zero, so $x$ cannot be invertible (otherwise multiplying by the inverse would give $1 \equiv 0 \pmod{p}$ in $A_n$, a contradiction).

**(b)** If $x \in \mathbb{Z}_p$ is nonzero, there exists a largest integer $n \geq 0$ such that $x_n = \varepsilon_n(x)$ is zero in $A_n$. Then $x = p^n u$ with $u$ not divisible by $p$, hence $u \in U$ by part (a). The uniqueness of the decomposition is clear: if $p^n u = p^m v$ with $u, v \in U$, then applying $v_p$ (the $p$-adic valuation) gives $n = m$, hence $u = v$. $\square$
