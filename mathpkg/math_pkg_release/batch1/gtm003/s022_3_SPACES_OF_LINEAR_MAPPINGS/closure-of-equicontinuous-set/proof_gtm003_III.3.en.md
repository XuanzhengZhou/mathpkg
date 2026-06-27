---
role: proof
locale: en
of_concept: closure-of-equicontinuous-set
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Since \(F\) is assumed to be Hausdorff and the evaluation map \(f \mapsto f(x)\) is continuous on \(F^E\) for each \(x \in E\), the set \(\{f \in F^E : f(\lambda x + \mu y) = \lambda f(x) + \mu f(y)\}\) is closed in \(F^E\) for each \(x, y \in E\) and \(\lambda, \mu \in K\) (as the inverse image of the diagonal under a continuous map into a Hausdorff space). Since \(L(E, F)\) is the intersection of all such sets, it is closed in \(F^E\).

For the second assertion, let \(H\) be equicontinuous and let \(f\) belong to the closure \(\overline{H}\) of \(H\) in \(F^E\). For a given \(0\)-neighborhood \(V\) in \(F\), choose a closed \(0\)-neighborhood \(W\) with \(W + W \subset V\). By equicontinuity of \(H\), there exists a \(0\)-neighborhood \(U\) in \(E\) such that \(u(U) \subset W\) for all \(u \in H\). For \(x \in U\), since \(f(x)\) is in the closure of \(\{u(x) : u \in H\} \subset W\), we have \(f(x) \in \overline{W} = W\). Hence \(f(U) \subset W \subset V\). This shows \(f\) is continuous (\(f \in \mathcal{L}(E, F)\)) and that \(\overline{H}\) is equicontinuous.
