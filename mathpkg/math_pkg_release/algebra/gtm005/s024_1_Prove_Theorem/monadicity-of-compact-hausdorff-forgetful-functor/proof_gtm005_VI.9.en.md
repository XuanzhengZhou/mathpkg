---
role: proof
locale: en
of_concept: monadicity-of-compact-hausdorff-forgetful-functor
source_book: gtm005
source_chapter: "VI"
source_section: "9"
---

We already know that $G$ has a left adjoint $F$; indeed, we may take each $FX$ to be the Stone-\v{C}ech compactification (V:6.2) of the set $X$ with the discrete topology.

For the remainder of the proof (given in a form due to R. Par\'{e} [1971]) it is convenient to regard a topological space as a pair $(X, (\overline{\cdot})_X)$ consisting of a set $X$ and a closure operation $S \mapsto \overline{S}$ defined for all subsets $S, T \subset X$ with the standard properties

$$\overline{\emptyset} = \emptyset, \quad S \subset \overline{S}, \quad \overline{\overline{S}} = \overline{S}, \quad \overline{S \cup T} = \overline{S} \cup \overline{T},$$

with $\emptyset$ the empty subset. A continuous map $f: (X, (\overline{\cdot})_X) \to (Y, (\overline{\cdot})_Y)$ is then a function $f: X \to Y$ such that $f(\overline{S}) \subset \overline{f(S)}$ for all $S \subset X$.

Now consider a $G$-split coequalizer pair

$$X \overset{f}{\underset{g}{\rightrightarrows}} Y$$

in $\text{Cmpt Haus}$, and let $e: Y \to W$ be its coequalizer in $\text{Set}$. Since $e$ is an absolute coequalizer, $Pe$ is still a coequalizer, in the diagram (of sets)

$$PX \underset{Pg}{\overset{Pf}{\rightrightarrows}} PY \xrightarrow{Pe} PW$$

where $P$ denotes the power-set functor. Since $f$ and $g$ are both continuous maps, both squares on the left (the square with $f$, and that with $g$) are commutative. It follows that

$$Pe \circ (\overline{\cdot})_Y \circ Pf = Pe \circ (\overline{\cdot})_Y \circ Pg.$$

But $Pe$ is a coequalizer, so $Pe \circ (\overline{\cdot})_Y$ factors through $Pe$. This gives a unique function $(\overline{\cdot})_W$ --- the dotted arrow in the diagram --- which makes the right hand square commute. This function may thus be described as follows: Given a subset $T \subset W$, choose any subset $S \subset Y$ with $(Pe)S = T$; then $\overline{T} = (Pe)\overline{S}$, independent of the choice of $S$. In particular, if $e^{-1}T \subset Y$ is the usual inverse image of $T$, then $\overline{T} = Pe(\overline{e^{-1}T})$. It is now routine to verify that this is a closure operation on $W$, hence that $W$ is a topological space.

By the commutativity of the diagram, $e$ is then continuous and closed. Since $Y$ is compact and $e: Y \to W$ is surjective, $W$ is also compact. Since $Y$ is Hausdorff, each point in $Y$ is a closed set there; since $e$ is a closed map and is surjective, the points of $W$ are closed. To show $W$ is Hausdorff, consider two points $w_1 \neq w_2 \in W$. They are closed in $W$, so $e^{-1}w_1$ and $e^{-1}w_2$ are disjoint closed sets in $Y$. By a familiar property of the compact Hausdorff space $Y$, disjoint closed sets can be separated by disjoint open neighborhoods; consequently $w_1$ and $w_2$ have disjoint open neighborhoods in $W$, so $W$ is Hausdorff.

It remains to verify that the Eilenberg--Moore comparison functor is an isomorphism. Suppose $h: Y \to Z$ is a continuous map of compact Hausdorff spaces which coequalizes $f$ and $g$ in $\text{Set}$. Since $e$ is a coequalizer in $\text{Set}$, there is a unique function $h': W \to Z$ with $h = h' \circ e: Y \to Z$; it remains to show $h'$ is continuous. Take $T \subset W$ and $S \subset Y$ with $(Pe)S = T$. Then $\overline{T} = (Pe)\overline{S}$, so

\begin{align*}
(Ph')\overline{T} &= (Ph')(Pe)\overline{S} = P(h)\overline{S} = \overline{P(h)S} \\
&= \overline{(Ph')(Pe)S} = \overline{(Ph')T}.
\end{align*}

Therefore $h'$ is continuous (and closed). The proof is complete.
