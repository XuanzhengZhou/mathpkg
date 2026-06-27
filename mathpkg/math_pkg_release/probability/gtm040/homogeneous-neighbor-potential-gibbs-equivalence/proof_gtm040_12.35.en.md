---
role: proof
locale: en
of_concept: homogeneous-neighbor-potential-gibbs-equivalence
source_book: gtm040
source_chapter: "12"
source_section: "5"
---

The statements and proofs of Proposition 12-14 and Corollary 12-15 are easily modified to apply to neighbor potentials on an infinite parameter set by replacing $T$ with $\bar{A}$. If $U'$ and $U''$ are homogeneous neighbor potentials such that $u'_k = u''_k = 0$ for all $k$ and $u'_{ij} = \ln Q'_{ij}$, $u''_{ij} = \ln Q''_{ij}$, then $U'$ and $U''$ determine the same Gibbs fields if and only if
$$
\sum_{B \subset A \subset D \subset \bar{A}} (-1)^{|A-B|} \Delta_D(\iota^B) = 0 \quad \text{for every } A = \{m\}, \{m, m + 1\},
$$
where $\Delta_A = U'_A - U''_A$. Setting $\delta_{ij} = u'_{ij} - u''_{ij}$, these equations become
\begin{align}
\delta_{k0} + \delta_{0k} - 2\delta_{00} &= 0 \tag{1}\\
\delta_{ij} - \delta_{i0} - \delta_{0j} + \delta_{00} &= 0 \tag{2}
\end{align}
The combination (2) $+ \frac{1}{2}(1\text{ with }k = i) + \frac{1}{2}(1\text{ with }k = j)$ yields
$$
(u'_{ij} - u''_{ij}) + w_i - w_j - z = 0, \tag{3}
$$
where $w_k = \frac{1}{2}(\delta_{0k} - \delta_{k0})$, $z = \delta_{00}$. Defining $h_k = e^{w_k}$ and $c = e^z$, the desired equation $Q''_{ij} = c(h_j/h_i)Q'_{ij}$ follows. Conversely, if $Q''_{ij} = c(h_j/h_i)Q'_{ij}$ holds, then
$$
\frac{Q'_{ij} Q'_{jk}}{(Q'^2)_{ik}} = \frac{c^2 Q'_{ij} (h_j/h_i) Q'_{jk} (h_k/h_j)}{c^2 \sum_s Q'_{is} (h_s/h_i) Q'_{sk} (h_k/h_s)} = \frac{Q'_{ij} Q'_{jk}}{(Q'^2)_{ik}},
$$
so the local characteristics determined by $Q'$ and $Q''$ agree, and hence the Gibbs fields are identical.
