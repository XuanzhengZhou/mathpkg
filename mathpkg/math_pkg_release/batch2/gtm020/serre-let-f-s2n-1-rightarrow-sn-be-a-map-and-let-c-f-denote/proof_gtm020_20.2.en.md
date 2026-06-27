---
locale: en
of_concept: serre-let-f-s2n-1-rightarrow-sn-be-a-map-and-let-c-f-denote
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '2'
---

Let $S^{2n-1} \rightarrow M_f \rightarrow S^n$ be the mapping cylinder factorization of $f$ where $M_f/S^{2n-1} = C_f$ the mapping cone and $S^n \rightarrow M_f$ is a homotopy equivalence. Then $H^n(C_f) = H^n(M_f, S^{2n-1}) = Zv$ and $H^{2n}(C_f) = H^{2n}(M_f, S^{2n-1}) = Zw$ are the only nonzero cohomology groups in this two cell complex. If $v^2 = hw$, then we must show $h = \pm H([f])$.

Let $E \rightarrow M_f$ be the path space fibration and let $E' \rightarrow S^{2n-1}$ be its restriction to $S^{2n-1}$. The fibre can be taken to be $\Omega S^n \subset E' \subset E$ because $S^n \rightarrow M_f$ is a homotopy equivalence. Now the groups $H^{2n-1}(E') \rightleftharpoons H^{2n}(E, E')$ isomorphic, and we will prove that $\pm h = H([f])$ by showing that $H^{2n-1}(E') = Z/H([f

4.6 Remark. If $f: S^{2n-1} \rightarrow S^n$ is a map, if $v: S^n \rightarrow S^n$ has degree $a$, and if $u: S^{2n-1} \rightarrow S^{2n-1}$ has degree $b$, then $H([vfu]) = a^2bH([f])$.

The Hopf construction on a map $g: X \times Y \rightarrow Z$ is a map $g^0: X \ast Y \rightarrow SZ$ where $X \ast Y$ is the join of $X$ and $Y$ defined as the quotient of $X \times [0,1] \times Y$ where $(x,0,y)$ and $(x',0,y)$ are identified and $(x,1,y)$ and $(x,1,y')$ are identified, and $g^0$ is given by $g^0(x,t,y) = \langle g(x,y),t \rangle \in S(Z)$. Note that $S^p \ast S^q$ is homeomorphic to $S^{p+q+1}$.

The bidegree of a map $g: S^{n-1} \times S^{n-1} \rightarrow S^{n-1}$ is $(d_1,d_2)$ provided $x \mapsto g(x,y)$ has degree $d_1$ and $y \mapsto g(x,y)$ has degree $d_2$.

4.7 Remark. If $g: S^{n-1} \times S^{n-1} \rightarrow S^{n-1}$ is a map of bidegree $(d_1,d_2)$, then for the Hopf construction $g^0: S^{2n-1} \rightarrow S^n$ the Hopf invariant $H([g^0]) = d_1d_2$, see 14(3.5).

4.8 Example. In 8(10.2) we prove the existence of a map $S^{n-1} \times S^{n-1} \rightarrow S^{n-1}$ of bidegree $(+1+(-1)^n,-1)$. Hence for $n=2m$, there
