---
role: proof
locale: en
of_concept: indicator-function-characterization
source_book: gtm002
source_chapter: "8"
source_section: "8"
---

The indicator function $\chi_E$ takes only the values $0$ and $1$. For any open set $U \subset \mathbb{R}$, we have four cases:

$$
\chi_E^{-1}(U) =
egin{cases}
\emptyset & 	ext{if } 0,1 
otin U, \[4pt]
E & 	ext{if } 1 \in U,\; 0 
otin U, \[4pt]
\mathbb{R} \setminus E & 	ext{if } 0 \in U,\; 1 
otin U, \[4pt]
\mathbb{R} & 	ext{if } 0,1 \in U.
\end{cases}
$$

Now $\emptyset$ and $\mathbb{R}$ are both measurable and have the property of Baire. If $E$ is measurable, then $\mathbb{R} \setminus E$ is measurable, so all four preimages are measurable, hence $\chi_E$ is measurable. Conversely, if $\chi_E$ is measurable, then taking $U = (1/2, 3/2)$ (an open set containing $1$ but not $0$) gives $\chi_E^{-1}(U) = E$, so $E$ is measurable.

The same argument applies verbatim with "has the property of Baire" in place of "measurable," since the family of sets with the property of Baire is also closed under complements and contains $\emptyset$ and $\mathbb{R}$.
