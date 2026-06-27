---
role: proof
locale: en
of_concept: properties-of-reflexive-spaces
source_book: gtm036
source_chapter: "20"
source_section: "20.5"
---

\textit{(i)} If $E$ is reflexive, then the evaluation map $e \colon E \to E^{**}$ is a topological isomorphism onto. This implies that the adjoint evaluation map $e^* \colon E^{***} \to E^*$ is also a topological isomorphism. Moreover, $E^*$ with the strong topology $\beta(E^*, E)$ coincides with $\beta(E^*, E^{**})$ since the topology on $E$ and $E^{**}$ coincide. It follows that the evaluation map of $E^*$ into $E^{***}$ is a topological isomorphism, so $E^*$ is reflexive.

\textit{(ii)} If $E$ is reflexive, then $E$ is evaluable by Theorem 20.6, which implies every strongly bounded subset of $E^*$ is equicontinuous, hence $E$ is barrelled. For the second assertion, a closed bounded subset $B$ of a reflexive space $E$ is weakly compact (since $E$ is semi-reflexive), and completeness follows from the fact that in a locally convex space, a weakly compact set is complete.

\textit{(iii)} For an arbitrary product $\prod_{\alpha} E_\alpha$ of reflexive spaces, each $E_\alpha$ is semi-reflexive and evaluable. The product is semi-reflexive because bounded weakly closed sets in the product correspond componentwise. The product is evaluable because strongly bounded subsets of the adjoint (which is the direct sum $\bigoplus_\alpha E_\alpha^*$) are equicontinuous. Similarly, a direct sum $\bigoplus_\alpha E_\alpha$ is semi-reflexive and evaluable, hence reflexive. The result follows from Theorem 20.6 in both cases.
