---
role: proof
locale: en
of_concept: isomorphism-of-categories
source_book: gtm026
source_chapter: "3"
source_section: "3.2"
---

The characterization follows directly from the definitions:

Let $U: \mathcal{A} \to \mathcal{B}$ be a functor that is a subcategory inclusion.

- $U$ is **full** means that for every pair of objects in $\mathcal{A}$, all $\mathcal{B}$-morphisms between their images lie in $U$. This is exactly surjectivity on hom-sets.
- $U$ is **representative** means every object of $\mathcal{B}$ is isomorphic to some $AU$. This is essential surjectivity on objects.
- $U$ is **replete** means that if an object of $\mathcal{B}$ is isomorphic to an object in the image of $U$, it is already in the image. This ensures injectivity on objects up to isomorphism.

Taken together, fullness (surjectivity on homs) + being a faithful subcategory (injectivity on homs, automatic for a subcategory inclusion) + representative (essential surjectivity on objects) + replete (injectivity on objects up to iso) = an isomorphism of categories. The text notes that without repleteness, the functor would only be an equivalence of categories — a more fundamental notion for "nearly isomorphic" categories that is discussed in Mac Lane '71.
