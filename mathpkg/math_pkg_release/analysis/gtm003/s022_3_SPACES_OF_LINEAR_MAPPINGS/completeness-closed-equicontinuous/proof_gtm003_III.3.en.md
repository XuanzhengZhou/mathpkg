---
role: proof
locale: en
of_concept: completeness-closed-equicontinuous
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Let \(H \subset \mathcal{L}_\mathfrak{S}(E, F)\) be closed and equicontinuous, and let \(\mathfrak{F}\) be a Cauchy filter on \(H\). Then \(\mathfrak{F}\) is a fortiori a Cauchy filter on \(H\) for the uniformity of simple convergence. For each \(x \in E\), the sets \(\{u(x) : u \in \Phi\}\) for \(\Phi \in \mathfrak{F}\) are bounded (since \(H\) is bounded) and form a base of a Cauchy filter in \(F\) (since \(u \mapsto u(x)\) is linear and continuous). 

Since \(F\) is quasi-complete, this filter base converges to an element \(u_1(x) \in F\). By Proposition 4.3, the pointwise limit \(x \mapsto u_1(x)\) is in \(\mathcal{L}(E, F)\). Moreover, since \(\mathfrak{F}\) is a Cauchy filter for the \(\mathfrak{S}\)-topology, given \(S \in \mathfrak{S}\) and a \(0\)-neighborhood \(V\) in \(F\), there exists \(\Phi \in \mathfrak{F}\) such that \(u(x) - v(x) \in V\) for all \(u, v \in \Phi\) and \(x \in S\). Passing to the limit in \(v\), we obtain \(u(x) - u_1(x) \in \overline{V}\) for all \(u \in \Phi\) and \(x \in S\). By choosing a suitable closed neighborhood, this shows convergence in the \(\mathfrak{S}\)-topology. Since \(H\) is closed, the limit \(u_1\) belongs to \(H\), proving completeness.
