---
role: proof
locale: en
of_concept: simplified-form-existence
source_book: gtm010
source_chapter: "7"
source_section: "7"
---

Apply (7.3) repeatedly, starting from the lowest-dimensional cells. Each application raises the minimum dimension of cells by one, at the cost of increasing the number of cells in the next dimension. After finitely many steps, all cells concentrate in two adjacent dimensions $r$ and $r+1$. 

To make the $r$-cells trivially attached: by (7.3), there are no cells of dimension $< r$. Let $\hat{K}$ be the resulting complex. Since $\hat{K} \supset L$, there is a retraction $R: \hat{K} \to L$. Each attaching map $\hat{\psi}_j|\partial I^r$ for an $r$-cell factors through $L$, and since $\hat{K}^{r-1} \subset L$, this map is null-homotopic in $L$. By (7.1), each $r$-cell with its original attaching map can be replaced by an $r$-cell trivially attached at $e^0$, without changing the formal deformation type.
