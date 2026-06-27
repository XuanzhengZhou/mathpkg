---
role: proof
locale: en
of_concept: proposition-31
source_book: gtm026
source_chapter: "1"
source_section: "4.11"
---

Let $(e, m)$ be the E-M factorization of $t$. Then there exists $h$:

$$\begin{array}{cccc}
C & e & \text{Im}(t) \\
\mathrm{id}_C & h & m \\
C & t & D
\end{array}$$

$\text{Im}(t) \longrightarrow C$ such that $e.h = \mathrm{id}_C$. As $e$ is epi, $h.t = m$. Since $m$ is mono and $h.e.m = h.t = m$, $h.e = \mathrm{id}_{\text{Im}(t)}$. Therefore $h$ is an isomorphism. Using 4.4 and 4.2 we have $t = h^{-1}m \in M$.

Propositions 4.10 and 4.11 show that $M$ is determined by $E$ in a straightforward way. This is useful in a context where there is a natural candidate for $E$ since there is only one $M$ to try! Dually, $E$ is determined by $M$ and similar comments apply.

4.12 Stability Proposition. If $m_i: C_i \longrightarrow D_i$ is a family in $M$ and if $\prod C_i$ and $\prod D_i$ exist in $\mathcal{K}$ then $\prod m_i: \prod C_i \longrightarrow \prod D_i$ (defined by $(\prod m_i).p_j = p_j.m_j)$ is in $M$. Given a pullback square

$$\begin{array}{cccc}
C & t & D

We use 4.11 to prove both statements. Consider a commutative square $f. \prod m_i = e.g$ with $e \in E$ as shown below. By 4.10, there exists $h_j$:

$$B \longrightarrow C_j$$ with $e.h_j = f.p_j$ for all $j$. Let $h$ be the unique morphism such that $h.p_j = h_j$. Then $e.h.p_j = f.p_j$ for all $j$, so $e.h = f$. Turning to the second statement, consider a commutative square $f.t = e.g$ with $e \in E$.

$$B \longrightarrow \text{id}_B$$
