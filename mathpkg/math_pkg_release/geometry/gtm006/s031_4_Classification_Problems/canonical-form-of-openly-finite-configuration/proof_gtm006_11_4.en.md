---
role: proof
locale: en
of_concept: canonical-form-of-openly-finite-configuration
source_book: gtm006
source_chapter: "11"
source_section: "4. Classification Problems"
---

Among all the o.f. configurations free equivalent to $\mathcal{A}$, choose one, $\mathcal{C}$ say, which has (1) the minimal number of 1-incident elements which are not incident with an element of $\mathcal{K}$, and (2) has no 2-incident elements. That (2) can be satisfied is evident, since any decreasing sequence of free equivalent o.f. configurations must be stationary after a certain point.

Suppose $\mathcal{C}$ has a 1-incident element not incident with $\mathcal{K}$, and let $X$ be such a one, incident with $m$ say. Choose $Q$ in $\mathcal{K}$ and not on $m$, construct the configuration $\mathcal{C}_1$ consisting of $\mathcal{C}$ plus the line $QX$, and then the configuration $\mathcal{C}_2$ which results from deleting $X$ from $\mathcal{C}_1$. Clearly $\mathcal{C}_2$ is free equivalent to $\mathcal{C}$, and hence to $\mathcal{A}$, and has fewer 1-incident elements not incident with $\mathcal{K}$. So all the 1-incident elements of $\mathcal{C}$ are in fact incident with elements of $\mathcal{K}$.

Suppose that $X$ is a 3-incident element, incident with $k, m, n$ say, and suppose that $X$ is not in $\mathcal{K}$. Then none of $k, m, n$ can be 1-incident elements, since then $X$ would be their only incidence, which is impossible, as $X$ is not in $\mathcal{K}$. So all of $k, m, n$ are 3-incident.

Now the core of $\mathcal{C}$ must be $\mathcal{K}$. But if we let $\mathcal{L}$ be the set of all 3-incident elements of $\mathcal{C}$, then certainly $\mathcal{L}$ includes $\mathcal{A}$ as well as the finitely many 3-incident elements (as above) not in $\mathcal{K}$. Let $\mathcal{S}$ be the set of all 3-incident elements in $\mathcal{L}$ and not in $\mathcal{K}$; $\mathcal{S}$ is finite, so if we adjoin to it any finite set of elements we can apply the technique of Lemma 11.9 to reduce all non-core elements to points on a single line.

The 0-incident and 1-incident elements can be shifted to points on the line $k$ by the same method as in Lemma 11.9: 1-incident elements contribute one point on $k$, 0-incident elements contribute two points on $k$, consistent with the invariance of open rank.
