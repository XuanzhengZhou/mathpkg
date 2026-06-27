---
role: proof
locale: en
of_concept: generic-extension-model-zf
source_book: gtm008
source_chapter: "10"
source_section: "10"
---

The proof proceeds by specializing the general $B$-valued construction to the case where $K = B$ and $f_0: B \to B$ is the identity (or $K = P$ and $f_0(p) = [p]^{-0}$). In both cases, the denotation operator $D$ maps constant terms of the $B$-valued language to elements of $M[G]$.

The Boolean algebra $B$ is the $M$-complete Boolean algebra of regular open sets of $P$ (relativized to $M$). The generic filter $G$ corresponds to an $M$-complete homomorphism $h: |B| \to |2|$ via $h([p]^{-0}) = 1$ iff $p \in G$. Then $M[G] = \{D(t) \mid t \in T\}$ where $T = \{T_{\alpha}^M \mid \alpha \in M\}$.

Since $M$ itself is a $B$-valued model of $\mathsf{ZF}$ (by Theorem 9.26 in the case $B = 2$), the relativized construction $(V[f_0])^M$ yields a $B$-valued model. Passing through the $M$-complete homomorphism $h$ produces the two-valued model $M[G]$ which satisfies $\mathsf{ZF}$. The preservation of the ordinals follows from the definition of the rank function on constant terms.
