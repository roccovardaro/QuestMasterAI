(define (domain eldoria-quest)
  (:requirements :strips :typing)

  (:types
    person location item - object
  )

  (:predicates
    ;; Predicate to indicate a person's current location
    (at ?p - person ?l - location)
    ;; Predicate to indicate a direct path connection between two locations
    (connected ?l1 ?l2 - location)
    ;; Predicate to indicate a person possesses an item
    (has ?p - person ?i - item)
    ;; Predicate to indicate an item's current location (e.g., on the ground)
    (at-item ?i - item ?l - location)

    ;; Quest state predicates
    ;; True if the protagonist has officially received the mission
    (mission-received)
    ;; True if the sword has been found and picked up by the protagonist
    (sword-found)
    ;; True if the sword has been successfully delivered to the king
    (sword-delivered)

    ;; Obstacle predicates
    ;; True if the path between two locations is blocked (e.g., by a fallen log)
    (path-blocked ?l1 ?l2 - location)
    ;; True if the sword is currently located on top of a tree at a specific location
    (sword-on-tree ?l - location)
    ;; True if the ground is slippery, making certain actions more difficult without the right tools
    (ground-slippery)
  )

  ;; Action: Move a person from one location to another
  (:action move
    :parameters (?p - person ?from ?to - location)
    :precondition (and
      (at ?p ?from)           ;; The person must be at the starting location
      (connected ?from ?to)   ;; There must be a direct connection between the locations
      (not (path-blocked ?from ?to)) ;; The path must not be blocked
    )
    :effect (and
      (not (at ?p ?from))     ;; The person leaves the starting location
      (at ?p ?to)             ;; The person arrives at the destination
    )
  )

  ;; Action: The protagonist officially receives the quest from the king
  (:action receive-quest
    :parameters (?p - person ?king - person ?village - location)
    :precondition (and
      (at ?p ?village)        ;; The protagonist must be in the village
      (at ?king ?village)     ;; The king must also be in the village
      (not (mission-received)) ;; The mission must not have been received yet
    )
    :effect (mission-received) ;; The mission is now received
  )

  ;; Action: A person picks up an item from its current location
  (:action pick-up-item
    :parameters (?p - person ?i - item ?l - location)
    :precondition (and
      (at ?p ?l)              ;; The person must be at the item's location
      (at-item ?i ?l)         ;; The item must be at that location
    )
    :effect (and
      (has ?p ?i)             ;; The person now has the item
      (not (at-item ?i ?l))   ;; The item is no longer at its original location
    )
  )

  ;; Action: Use an axe to clear a fallen log blocking a path
  (:action clear-log
    :parameters (?p - person ?axe - item ?loc1 ?loc2 - location)
    :precondition (and
      (at ?p ?loc1)           ;; The person must be at one end of the blocked path
      (has ?p ?axe)           ;; The person must possess an axe
      (path-blocked ?loc1 ?loc2) ;; The path must be blocked
    )
    :effect (and
      (not (path-blocked ?loc1 ?loc2)) ;; The path is no longer blocked (one way)
      (not (path-blocked ?loc2 ?loc1)) ;; The path is no longer blocked (other way, for bidirectional paths)
    )
  )

  ;; Action: Climb a tree to retrieve the sword
  (:action climb-tree-for-sword
    :parameters (?p - person ?sword - item ?tree-loc - location)
    :precondition (and
      (at ?p ?tree-loc)       ;; The person must be at the tree's location
      (sword-on-tree ?tree-loc) ;; The sword must be on the tree
      (or
        (not (ground-slippery)) ;; Can climb if the ground is not slippery
        (has ?p ladder)         ;; OR, can climb even if slippery, if they have a ladder
      )
    )
    :effect (and
      (has ?p ?sword)         ;; The person now has the sword
      (not (sword-on-tree ?tree-loc)) ;; The sword is no longer on the tree
      (sword-found)           ;; The sword has been found
    )
  )

  ;; Action: Deliver the sword to the king at the castle
  (:action deliver-sword
    :parameters (?p - person ?sword - item ?castle - location)
    :precondition (and
      (at ?p ?castle)         ;; The person must be at the castle
      (has ?p ?sword)         ;; The person must possess the sword
      (mission-received)      ;; The mission must have been received (to fulfill it)
      (sword-found)           ;; The sword must have been found first
    )
    :effect (sword-delivered) ;; The sword has been successfully delivered
  )
)