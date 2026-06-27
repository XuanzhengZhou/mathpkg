---
role: proof
locale: en
of_concept: proposition-13
source_book: gtm026
source_chapter: "1"
source_section: "1.55"
---

Let $f:(A, \alpha) \longrightarrow (B, \beta)$ be a $\text{T}$-homomorphism. Let $f = (p:A \longrightarrow C).(i:C \longrightarrow B)$ be the usual image factorization at the level of sets. By 1.4.31, there exists a unique $\text{T}$-algebra structure $\gamma:CT \longrightarrow C$ on $C$ such that $p$ and $i$ become $\text{T}$-homomorphisms. Let $a, b:E \longrightarrow A$ be the kernel pair of $f$ in $\text{Set}$. By analyzing the proof of 1.22 in the context of 1.11 and 1.14, it is clear that there exists a unique $\delta:ET \longrightarrow E$ by virtue of which $a$ and $b$ become $\text{T}$-homomorphisms, (and then $a, b:(E, \delta) \longrightarrow (A, \alpha)$ is in fact the kernel pair of $

To prove 1.56, we use just the sort of diagram that appeared in the advertisement for epimorphisms of 1.36+, namely:

$$\begin{align*}
AT & \rightarrow CT \rightarrow C'T \\
pT & \rightarrow gT \\
\alpha.p & \rightarrow \gamma \\
C & \rightarrow g \\
C' & \rightarrow C'
\end{align*}$$

Crucial is the use of 1.4.29 which guarantees that $pT$ is epi. $\square$
