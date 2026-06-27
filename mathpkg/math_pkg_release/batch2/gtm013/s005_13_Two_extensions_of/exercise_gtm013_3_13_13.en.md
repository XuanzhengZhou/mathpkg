---
role: exercise
locale: en
chapter: "3"
section: "13"
exercise_number: 13
---
**Exercise 13 (Two extensions of $K$ by $N$).**

Consider two extensions of $K$ by $N$:
$$0 \rightarrow K \xrightarrow{f} M \xrightarrow{g} N \rightarrow 0$$
$$0 \rightarrow K \xrightarrow{f'} M' \xrightarrow{g'} N \rightarrow 0$$
These are equivalent if there is a homomorphism $h: M \rightarrow M'$ such that the diagram

\[
\begin{CD}
0 @>>> K @>f>> M @>g>> N @>>> 0 \\
@. @| @VhVV @| @. \\
0 @>>> K @>>f'> M' @>>g'> N @>>> 0
\end{CD}
\]

commutes.

1. Prove that if the above two extensions are equivalent (via $h$), then $h$ is an isomorphism.
2. Prove that the relation of "being equivalent" is an equivalence relation on the class of all extensions of $K$ by $N$.
3. Given $K$ and $N$, there is at least one extension of $K$ by $N$:
   $$0 \rightarrow K \xrightarrow{\iota} K \times N \xrightarrow{\pi} N \rightarrow 0$$
   where $\iota: k \mapsto (k, 0)$ and $\pi: (k, n) \mapsto n$.
4. Prove that there are (at least) two inequivalent extensions of $\mathbb{Z}_2$ by $\mathbb{Z}_4$.
