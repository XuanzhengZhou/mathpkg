---
role: proof
locale: en
of_concept: pi-is-well-founded-iff-there-are-no-sequences-langle-i-n-n-omega-rangle-and-lang
source_book: gtm001
source_chapter: "15"
source_section: ""
---

If such sequences exist, then $\langle \pi_{i_n \infty}(\sigma_n) | n < \omega \rangle$ is an infinite descending sequence in $M/\equiv$. Thus $\Pi$ is not well founded. Suppose $\Pi$ is not well founded and $\langle [j_n, \tau_n] | n < \omega \rangle$ is an infinite descending sequence in $\lim \Pi$. Then we can find a sequence $\langle i_n | n < \omega \rangle$ such that $i_0 \leq i_1 \leq \cdots \leq i_n \leq \cdots$ and $j_n \leq i_n$ for all $n < \omega$. Let $\sigma_n = \pi_{j_n i_n}(\tau_n)$. Then for all $n < \omega$,

$$\pi_{i_n i_{n+1}}(\sigma_n) = \pi_{i_n i_{n+1}}(\pi_{j_n i_n}(\tau_n)) = \pi_{j_n i_{n+1}}(\tau_n)$$

$$> \pi_{j_{n+1} i_{n+1}}(\tau_{n+1}) = \sigma_{n+1}.$$
