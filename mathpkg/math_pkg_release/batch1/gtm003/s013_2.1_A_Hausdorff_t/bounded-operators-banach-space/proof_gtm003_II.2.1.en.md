---
role: proof
locale: en
of_concept: bounded-operators-banach-space
source_book: gtm003
source_chapter: "II"
source_section: "2.1"
---

It is immediate that the bounded sets in a normed space $L$ are exactly those subsets on which $x \mapsto \|x\|$ is bounded. Thus if $L$, $N$ are normed spaces over $K$ and $u$ is a continuous linear map from $L$ into $N$, it follows from (I, 5.4) that the number
$$\|u\| = \sup\{\|u(x)\| : x \in L,\ \|x\| \leq 1\}$$
is finite.

It is easy to show that $u \mapsto \|u\|$ is a norm on the vector space $\mathcal{L}(L, N)$ over $K$ of all continuous linear maps from $L$ into $N$. $\mathcal{L}(L, N)$ is a Banach space under this norm if $N$ is a Banach space; in particular, if $N$ is taken to be the one-dimensional Banach space $(K_0, |\cdot|)$ (cf. Chapter I, Section 3), then $L' = \mathcal{L}(L, K_0)$ is a Banach space, called the \textit{dual} (or \textit{adjoint}) of $L$.
