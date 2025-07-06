(define (problem retrieve-royal-sword)
  (:domain eldoria-quest)

  (:objects
    hero king - person             ;; The protagonist and the king
    village forest-edge forest-clearing castle old-shed carpenters-shop - location ;; Various locations in Eldoria
    sword axe ladder - item        ;; Items crucial for the quest
  )

  (:init
    ;; Initial positions of characters
    (at hero village)
    (at king village)

    ;; Define connections between locations (bidirectional for simplicity)
    (connected village forest-edge)
    (connected forest-edge village)
    (connected village old-shed)
    (connected old-shed village)
    (connected village carpenters-shop)
    (connected carpenters-shop village)
    (connected village castle)
    (connected castle village)
    (connected forest-edge forest-clearing)
    (connected forest-clearing forest-edge)

    ;; Initial locations of items
    (at-item axe old-shed)             ;; The axe is in the old shed
    (at-item ladder carpenters-shop)   ;; The ladder is at the carpenter's shop

    ;; Initial state of obstacles and the sword
    (sword-on-tree forest-clearing)    ;; The sword is on a tree in the forest clearing
    (path-blocked forest-edge forest-clearing) ;; The path from forest-edge to forest-clearing is blocked
    (path-blocked forest-clearing forest-edge) ;; The path from forest-clearing to forest-edge is also blocked

    ;; Environmental condition: ground is slippery due to rain
    (ground-slippery)

    ;; Initial quest status (nothing achieved yet)
    (not (mission-received))
    (not (sword-found))
    (not (sword-delivered))
  )

  (:goal
    (and
      (sword-delivered)   ;; The primary goal: the sword must be delivered
      (at hero castle)    ;; The hero must be at the castle after delivering the sword
    )
  )
)