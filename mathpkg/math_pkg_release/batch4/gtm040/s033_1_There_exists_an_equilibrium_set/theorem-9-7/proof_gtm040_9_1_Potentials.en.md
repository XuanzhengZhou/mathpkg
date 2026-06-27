---
role: proof
locale: en
of_concept: theorem-9-7
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

We may assume that neither $i$ nor $j$ equals $k$, since otherwise both sides are clearly zero. We begin by establishing four equations:
\begin{align}
N_{kk}^{(n)} &= \sum_{v=0}^{\infty} F_{ik}^{(v)} N_{kk}^{(n-v)} \\
N_{ik}^{(n)} &= \sum_{v=0}^{n} F_{ik}^{(v)} N_{kk}^{(n-v)} \\
N_{kj}^{(n)} &= \sum_{v=0}^{n} F_{ik}^{(v)} N_{kj}^{(n-v)} \\
N_{ij}^{(n)} &= {}_k N_{ij}^{(n)} + \sum_{v=0}^{n} F_{ik}^{(v)} N_{kj}^{(n-v)}.
\end{align}

Multiply (1) by $\alpha_j/\alpha_k$, (2) by $-\alpha_j/\alpha_k$, (3) by $-1$, and (4) by $1$, and add. We obtain
$$(N_{kk}^{(n)} - N_{ik}^{(n)})\alpha_j/\alpha_k + (N_{ij}^{(n)} - N_{kj}^{(n)})$$
$$= {}_k N_{ij}^{(n)} + \sum_{v=0}^{n} F_{ik}^{(v)}(b_n - b_{n-v}) + \sum_{v=n+1}^{\infty} F_{ik}^{(v)} b_n,$$
where $b_n = N_{kk}^{(n)}\alpha_j/\alpha_k - N_{kj}^{(n)}$, and $\{b_n\}$ is a bounded sequence by Lemma 9-2. The first term ${}_k N_{ij}^{(n)}$ on the right tends to ${}_k N_{ij}$, and the third term tends to zero since $\{b_n\}$ is bounded and $\sum F_{ik}^{(v)}$ is finite.

It remains to show $\lim_n \sum_{v=0}^{n} a_v (b_n - b_{n-v}) = 0$ where $a_v = F_{ik}^{(v)}$. Since $a_n \geq 0$, $\sum a_n = 1$, and $\{b_n\}$ is bounded, by Lemma 9-6 it suffices to show $(b_n - b_{n-1}) \to 0$. But
$$b_n - b_{n-1} = (N_{kk}^{(n)} - N_{kk}^{(n-1)})\frac{\alpha_j}{\alpha_k} - (N_{kj}^{(n)} - N_{kj}^{(n-1)})$$
$$= P_{kk}^{(n)}\frac{\alpha_j}{\alpha_k} - P_{kj}^{(n)} \to L_{kk}\frac{\alpha_j}{\alpha_k} - L_{kj} = 0.$$
