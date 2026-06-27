---
role: proof
locale: en
of_concept: "approximate-units-in-ideals"
source_book: gtm039
source_chapter: "1"
source_section: "1.3"
---
For $x = x^* \in J$, use $f_n(t) = nt^2(1+nt^2)^{-1}$ in the unitized algebra. Since $f_n(0)=0$, $f_n$ is uniformly approximable on $\text{sp}(x)$ by polynomials without constant term, so $e_n = f_n(x) \in J$. $\text{sp}(e_n) \subseteq [0,1]$ because $0 \leqslant f_n \leqslant 1$. The estimate $t^2(1-f_n(t)) = t^2(1+nt^2)^{-1} \leqslant 1/n$ gives $\|xe_n-x\|^2 \leqslant \|x^2(e-e_n)\| \leqslant 1/n \to 0$. For general $x$, apply to $x^*x$. $\square$
