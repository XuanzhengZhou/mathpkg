---
role: exercise
locale: en
chapter: "6"
section: "6"
exercise_number: 5
---

([Lawvere '63], [Freyd '66], [Manes '67]). A **semiadditive category** is a category $\mathcal{A}$ together with the structure of an abelian monoid on the set $\mathcal{A}(A, B)$ for each pair $(A, B)$ of objects, such that composition is bilinear.

(a) Show that a semiadditive category has finite biproducts (products which are also coproducts) and that on each $\mathcal{A}(A, B)$, the given abelian monoid structure is the one induced by the biproduct structure.

(b) Show that if $\mathbf{Set}^T$ is semiadditive then
\[
\begin{CD}
X @>{(\operatorname{id}_X,0)}>> X \times X @<{(0,\operatorname{id}_X)}<< X
\end{CD}
\]
is a coproduct diagram in $\mathcal{A}$. [Hint: add the pieces.]

(c) If $\mathbf{Set}^T$ is semiadditive (respectively, additive) show that $\mathbf{T} \otimes \mathbf{AM}$ ($\mathbf{T} \otimes \mathbf{AG}$) exists and coincides with $\mathbf{T}$. [Hint: using (b), define the necessary operations as $\mathbf{T}$-homomorphisms.]

(d) If $\mathbf{T}$ is finitary and $\mathbf{Set}^T$ is semiadditive (respectively, additive) show that $\mathbf{Set}^T$ coincides with the category of semimodules (modules) over the semiring (ring) $1T$. [Hint: if $(x_1, \ldots, x_n)\omega$ is a $\mathbf{T}$-operation, it decomposes as $(0, x_2, \ldots, x_n)\omega + \cdots + (x_1, \ldots, x_{n-1}, 0)\omega$.]

(e) For any theory $\mathbf{T}$ in $\mathbf{Set}$, prove that an epimorphism in the category of $\mathbf{T}$-$\mathbf{AG}$ bialgebras is a coequalizer. [Hint: given an epimorphism $f \colon X \to Y$, set $q = \operatorname{coeq}(f, 0)$ in the category of abelian groups; then $q$ is obtained by dividing out by the abelian group congruence $R = \{(y_1, y_2): y_1 - y_2 \in \operatorname{Im}(f)\}$; since ``minus'' $Y \times Y \to Y$ is a $\mathbf{T}$-homomorphism, $R$ is also a $\mathbf{T}$-congruence, and $q = \operatorname{coeq}(f, 0)$ in the category of bialgebras; as $f$ is epi, $q = 0$.]

(f) Let $\mathcal{A}$ be the additive category of torsion-free abelian groups. Show that $\mathbf{Z} \to \mathbf{Z}$, $n \mapsto 2n$ is an epimorphism which is not a coequalizer.
