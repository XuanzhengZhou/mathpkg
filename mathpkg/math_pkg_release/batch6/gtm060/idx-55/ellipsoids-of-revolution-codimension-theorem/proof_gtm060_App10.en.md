---
role: proof
locale: en
of_concept: ellipsoids-of-revolution-codimension-theorem
source_book: gtm060
source_chapter: "Appendix 10"
source_section: "Multiplicities of characteristic frequencies and ellipsoids of revolution"
---

Consider an ellipsoid in $n$-dimensional space which has two equal axes, and whose other axes are distinct. Such an ellipsoid is defined by the directions of the distinct axes, which gives

$$(n-1) + (n-2) + \cdots + 2 = \frac{(n+1)(n-2)}{2}$$

different parameters, and also by the magnitudes of the axes, which gives $n-1$ parameters. Thus the total number of parameters is

$$\frac{n^2 - n - 2 + 2n - 2}{2} = \frac{n(n+1)}{2} - 2,$$

which is two less than the dimension of the space of all ellipsoids (which is $n(n+1)/2$).

The proof reduces to the same kind of parameter count as in the special case analyzed above (which corresponds to multiplicity pattern $v_2 = 1$, $v_3 = v_4 = \cdots = 0$). One notes first that the dimension of the manifold of all $k$-dimensional subspaces in an $n$-dimensional vector space is equal to $k(n - k)$ (since a $k$-dimensional plane in general position in an $n$-dimensional space can be thought of as the graph of a mapping from a $k$-dimensional space to an $(n - k)$-dimensional space, and such a mapping is given by a rectangular $k \times (n - k)$ matrix).

Carrying out the parameter count for each possible multiplicity pattern of axes yields that the codimension is at least $2$ in every case. The "finite union" assertion follows from the fact that there are only finitely many possible patterns of axis multiplicities (partition types of $n$), and each pattern determines a smooth submanifold whose codimension is computed by the parameter count.
