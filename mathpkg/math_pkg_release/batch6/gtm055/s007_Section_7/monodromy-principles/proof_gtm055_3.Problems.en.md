---
role: proof
locale: en
of_concept: monodromy-principles
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

It suffices to show that the analytic continuation of $f_0$ along the closed polygonal arc $\pi = \pi_1 + \tilde{\pi}_2$ returns to $f_0$ in a neighborhood of $\lambda_0$. By interpolating new vertices and function elements as needed, one may arrange things so that $\pi$ is a closed polygonal arc that intersects itself only at its vertices.

Such a polygonal arc decomposes as a formal sum of polygonal arcs of the form $\rho + \tilde{\rho}$ (which trivially return to the original function element) and polygonal Jordan loops. The crux is to handle the Jordan loops. Using Problem T (triangulation of the interior of a polygonal Jordan curve), each such loop can be partitioned into triangular regions. By induction on the number of edges, using the result of Problem S(i) for continuation along line segments, one shows that analytic continuation around each Jordan loop also returns to the original function element.

Since the closed arc $\pi$ is a sum of these elementary pieces, each of which preserves the function element, the continuation around $\pi$ returns $f_0$. Therefore the continuations along $\pi_1$ and $\pi_2$ agree at $\lambda$.
