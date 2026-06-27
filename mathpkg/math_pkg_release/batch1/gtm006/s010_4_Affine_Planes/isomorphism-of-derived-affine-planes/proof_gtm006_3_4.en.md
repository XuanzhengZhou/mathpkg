---
role: proof
locale: en
of_concept: isomorphism-of-derived-affine-planes
source_book: gtm006
source_chapter: "3"
source_section: "4"
---

**Proof.** ($\Leftarrow$) If $\alpha$ is an isomorphism of $\mathcal{P}$ with $l^\alpha = m$, then $\alpha$ maps points of $l$ to points of $m$, and points not on $l$ to points not on $m$. Thus $\alpha$ restricts to a bijection from $\mathcal{P}^l$ to $\mathcal{P}^m$ that preserves incidence. Hence $\mathcal{P}^l \cong \mathcal{P}^m$.

($\Rightarrow$) Suppose $\theta$ is an isomorphism from $\mathcal{P}^l$ onto $\mathcal{P}^m$. Define $\alpha$ on $\mathcal{P}$ as follows:
\begin{itemize}
\item For any point $X$ not on $l$, set $X^\alpha = X^\theta$ (this is well-defined since $\theta$ acts on points of $\mathcal{P}^l$, which are exactly the points of $\mathcal{P}$ not on $l$).
\item For any point $Y$ on $l$, pick any line $h$ through $Y$ different from $l$. In $\mathcal{P}^l$, $h$ is an affine line; under $\theta$, $h^\theta$ is a line of $\mathcal{P}^m$ which, when considered as a line of $\mathcal{P}$, intersects $m$ in a unique point. Define $Y^\alpha = h^\theta \cap m$.
\end{itemize}
One verifies that this definition of $Y^\alpha$ is independent of the choice of $h$, and that $\alpha$ is a bijection on points and on lines preserving incidence, with $l^\alpha = m$. Thus $\alpha$ is the required isomorphism of $\mathcal{P}$. $\square$
