---
role: proof
locale: en
of_concept: separate-continuity-implies-hypocontinuity
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Let \(S\) be a bounded subset of \(E\) and \(W\) a \(0\)-neighborhood in \(G\). Since \(f\) is separately continuous, for each \(s \in S\) the linear map \(f_s : F \to G\) is continuous. Consider the family \(\{f_s : s \in S\} \subset \mathcal{L}(F, G)\).

For each \(y \in F\), the set \(\{f(s, y) : s \in S\}\) is bounded in \(G\) because \(s \mapsto f(s, y)\) is a continuous linear map on \(E\) (by separate continuity) and \(S\) is bounded. Thus \(\{f_s : s \in S\}\) is simply bounded in \(\mathcal{L}(F, G)\).

If \(F\) is barreled or a Baire space, Theorem 4.2 (Banach-Steinhaus) implies that \(\{f_s : s \in S\}\) is equicontinuous. This means there exists a \(0\)-neighborhood \(V\) in \(F\) such that \(f_s(V) \subset W\) for all \(s \in S\), i.e., \(f(S \times V) \subset W\). This is precisely \(\mathfrak{B}\)-hypocontinuity.
