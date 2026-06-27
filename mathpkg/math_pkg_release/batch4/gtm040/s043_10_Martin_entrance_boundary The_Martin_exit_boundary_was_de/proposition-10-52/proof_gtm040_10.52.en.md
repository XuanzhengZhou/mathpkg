---
role: proof
locale: en
of_concept: proposition-10-52
source_book: gtm040
source_chapter: "10"
source_section: "52"
---

**Proof:** Form the reverse process and call its measure $\Pr'$. Its transition matrix restricted to the states of $S$ is the $\nu$-dual of $P$, denoted $\hat{P}$. Form the exit and entrance boundaries of $\hat{P}$ relative to $\hat{\pi} = \nu\text{-dual } f$ and $\hat{f} = \nu\text{-dual } \pi$. By Proposition 10-51, the limit

$$z_v = \lim_{n \uparrow v} z_n$$

exists in $\hat{S}^*$ a.e. $[\Pr']$, and either $v$ is finite and $z_v \in S$ or else $v$ is infinite and a.e. $z_v \in \hat{B}_e$. Therefore

$$z_u = \lim_{n \uparrow u} z_n$$

exists in $\hat{S}^*$ a.e. $[\Pr]$, and either $u$ is finite and $z_u \in S$ or else $u$ is infinite and a.e. $z_u \in \hat{B}_e$. Since $\hat{S}^*$ and $*S$ are canonically identified according to Lemma 10-49, the first part of the proposition follows. Moreover, we have

$$\Pr[z_u \in C] = \Pr'[z_v \in C] = \int_C \lim_{E \uparrow S} [\mu^E \hat{K}(\cdot, x)] d\mu^\nu(x),$$

where $\mu^\nu$ is the representing measure from Theorem 10-48. By Lemma 10-50, this limit equals $p(x)$, yielding the desired formula.
