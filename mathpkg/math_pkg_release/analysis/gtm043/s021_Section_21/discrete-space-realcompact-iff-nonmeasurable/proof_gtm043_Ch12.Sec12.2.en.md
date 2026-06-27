---
role: proof
locale: en
of_concept: discrete-space-realcompact-iff-nonmeasurable
source_book: gtm043
source_chapter: "12"
source_section: "12.2"
---
Let $X$ be a discrete space. An ultrafilter $\mathcal{U}$ on $X$ has characteristic function $\chi_{\mathcal{U}}$. The characteristic function $\chi_{\mathcal{U}}$ is countably additive (i.e., a measure) precisely when $\mathcal{U}$ is closed under countable intersections. Such an ultrafilter is called a \emph{real} ultrafilter.

By the basic theory of realcompactness for discrete spaces, $X$ is realcompact if and only if every real ultrafilter on $X$ is fixed (i.e., contains a singleton).

Now, $|X|$ is nonmeasurable if every $\{0,1\}$-valued measure $\mu$ on $X$ with $\mu(X) = 1$ is trivial, meaning $\mu(\{x\}) = 1$ for some $x \in X$. Via the ultrafilter correspondence, this means every real ultrafilter is fixed, which is exactly the condition that $X$ is realcompact.