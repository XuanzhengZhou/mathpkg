---
role: proof
locale: en
of_concept: gleason-desarguesian-characterization
source_book: gtm006
source_chapter: "XIII"
source_section: "4"
---

**Proof.** Let $l$ be any line of $\mathcal{P}$. By hypothesis every point of $\mathcal{P}$ is the centre of a non-trivial elation in $\Pi$. Given any point $P$ on $l$, let $\alpha_P$ be a non-trivial elation with centre $P$. By Corollary 1 to Lemma 4.11, we may conjugate $\alpha_P$ by elements of $\Pi$ to obtain elations with any centre. 

Now suppose first that $\Pi$ contains an elation. If there is a point $P$ and axis $a$ such that $\Pi$ contains an $(P, a)$-elation, then by transitivity (Chapter IV) $\Pi$ contains all $(P, a)$-elations. Using Lemma 13.9 and the fact that every point is a centre of an elation, we can build up the full elation group. The dual argument (using that every line is an axis of an elation) and Theorem 4.25 then imply that $\mathcal{P}$ is $(P, l)$-transitive for all flags $(P, l)$, which makes $\mathcal{P}$ desarguesian (by the Lenz-Barlotti classification). Since $\Pi$ contains all elations with all axes, it contains the little projective group.

Now suppose every perspectivity in $\Pi$ is a homology. Then by hypothesis every point is the centre of a homology in $\Pi$ and every line is the axis of a homology in $\Pi$. If any line is a homology axis for two centres, or dually if any point is a homology centre for two axes, then by Corollary 2 to Theorem 4.25 (or its dual) $\Pi$ contains an elation. Thus for each point $P$ of $\mathcal{P}$ there is a unique line $P'$ such that $P'$ is the axis of all non-trivial homologies with centre $P$, and $P$ is the centre of all non-trivial homologies with axis $P'$.

Define $\theta$ by $P^\theta = P'$. Clearly $\theta^2 = 1$. Suppose $A$ is on $l$ but $l'$ is not on $A'$. If $\alpha$ is a non-trivial $(l', l)$-homology, then $A^\alpha = A$ but $A^{l \alpha} \neq A^{l}$, so if $\delta$ is any non-trivial $(A, A')$-homology, $\alpha^{-1}\delta\alpha$ is an $(A^\alpha, A^{l\alpha})$-homology (by Lemma 4.11). Since $A^\alpha = A$, this means $A^{l\alpha}$ and $A^{l}$ are distinct homology axes for $A$, a contradiction. Hence $A$ is on $l$ if and only if $l'$ is on $A'$; i.e., $\theta$ is a polarity. But by definition of $\theta$, $A$ is not on $A'$ for any $A$, so $\theta$ is a polarity without absolute points, contrary to Theorem 12.3 (which says every polarity of a finite plane has at least one absolute point). Hence $\Pi$ must contain an elation, and the theorem follows from the first case.
