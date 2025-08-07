# Spécification technique de la **Rose dorée**

## Introduction

Bienvenue dans l'équipe de **La rose dorée**. Comme vous le savez, nous sommes une petite auberge idéalement située, tenue par une aubergiste sympathique nommée Allison. Nous achetons et vendons uniquement les meilleurs produits !

Malheureusement, nos articles perdent constamment en **qualité** à mesure qu'ils approchent de leur date limite de vente.

Nous avons un système en place qui met à jour notre inventaire automatiquement. Il a été développé par un certain Leeroy, un type sérieux qui est maintenant parti vers de nouvelles aventures. Votre mission est d’ajouter une nouvelle fonctionnalité à notre système afin que nous puissions commencer à vendre une nouvelle catégorie d’articles.

## Spécifications

### Existant

Voici d'abord une introduction à notre système :

- [x] Tous les `items` ont une valeur `sell_in` qui indique le nombre de jours qu’il nous reste pour les vendre  
- [x] Tous les `items` ont une valeur de `quality` qui indique à quel point l’article est précieux  
- [x] À la fin de chaque journée, notre système diminue ces deux valeurs pour chaque item

Assez simple, non ? C’est là que ça devient intéressant :

- [x] Une fois la date limite dépassée, la `quality` diminue deux fois plus vite  
- [x] La `quality` d’un item n’est jamais négative  
- [x] `"Aged Brie"` augmente en fait en `quality` avec le temps
- [x] La `quality` d’un item ne dépasse jamais `50`
- [x] `"Sulfuras"`, en tant qu’item légendaire, n’a jamais besoin d’être vendu et ne perd jamais en `quality`
- [x] Les `"Backstage passes"`, comme le `"Aged Brie"`, augmentent en `quality` à mesure que leur `sell_in` approche :
  - [x] La `quality` augmente de `2` lorsqu’il reste `10` jours ou moins, et de `3` lorsqu’il reste `5` jours ou moins, mais
  - [x] La `quality` tombe à `0` après le concert
- [x] un item ne peut jamais voir sa `quality` dépasser `50`, cependant `"Sulfuras"` est un item légendaire et, en tant que tel, sa `quality` est de `80` et elle ne change jamais

### Nouvelle fonctionnalité

Nous avons récemment signé un contrat avec un fournisseur d’items conjurés. Cela nécessite une mise à jour de notre système :

- [ ] Les items `"Conjured"` se détériorent en `quality` deux fois plus vite que les items normaux

## Cadre

N’hésitez pas à modifier la méthode `update_quality` et à ajouter du nouveau code tant que tout fonctionne correctement.

Cependant, ne modifiez pas la classe `Item` ni la propriété `Items`, car elles appartiennent au gobelin dans le coin, qui entrerait instantanément en rage et vous tuerait d’un seul coup — il ne croit pas au partage de code (vous pouvez rendre la méthode `UpdateQuality` et la propriété `Items` statiques si vous le souhaitez, nous vous couvrirons).
