---
role: proof
locale: en
of_concept: bienayme-equality
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "3. Independence"
---
Since $E(X_k - EX_k) = EX_k - EX_k = 0$ and independence of the $X_k$ implies independence of the $X_k - EX_k$, it follows that

$$\sigma^2 \sum_{k=1}^{n} X_k = E\left(\sum_{k=1}^{n} X_k - \sum_{k=1}^{n} EX_k\right)^2 = E\left\{\sum_{k=1}^{n} (X_k - EX_k)\right\}^2$$

$$= \sum_{k=1}^{n} E(X_k - EX_k)^2 + \sum_{j \neq k} E(X_j - EX_j)(X_k - EX_k)$$

$$= \sum_{k=1}^{n} \sigma^2 X_k,$$

where the cross terms vanish because, for $j \neq k$, by the multiplication property,
$E(X_j - EX_j)(X_k - EX_k) = E(X_j - EX_j) \cdot E(X_k - EX_k) = 0 \cdot 0 = 0$.
