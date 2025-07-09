(define (domain eldoria-quest)
    (:requirements :strips :typing)
    (:types
        person ; Generic type for characters
        location ; Places in the world
        object ; Generic type for items and other entities
        king protagonist - person ; Specific types of persons
        sword log tree - object ; Specific types of objects
    )

    (:predicates
        (at ?o - object ?l - location) ; An object (person or item) is at a specific location.
        (mission-active ?p - protagonist) ; Indicates the protagonist has received and is on the mission.
        (has ?p - protagonist ?i - sword) ; Indicates the protagonist possesses the sword.

        ;; Obstacle predicates
        (path-blocked ?from ?to - location ?obs - log) ; A path between two locations is blocked by a log.
        (sword-on-tree ?s - sword ?t - tree) ; The sword is located on a specific tree.
        (ground-slippery ?l - location) ; The ground at a certain location is slippery.

        ;; Overcome obstacle predicates
        (path-cleared ?from ?to - location) ; Indicates a specific path has been cleared of a physical block (like a log).
        (can-traverse-slippery-ground ?p - protagonist) ; Indicates protagonist has learned/adapted to move on slippery ground.
        (king-has-sword ?k - king ?s - sword) ; Goal predicate: The king has the sword.
    )

    ;; Action: Start the quest (receiving the mission from the king).
    ;; This action sets the main quest objective as active for the protagonist.
    (:action start-quest
        :parameters (?p - protagonist ?k - king ?village - location)
        :precondition (and
            (at ?p ?village)
            (at ?k ?village)
        )
        :effect (and
            (mission-active ?p)
        )
    )

    ;; Action: Clear a fallen log blocking a path.
    ;; This action represents the protagonist physically removing an obstacle from a path.
    (:action clear-fallen-log
        :parameters (?p - protagonist ?log_obs - log ?from ?to - location)
        :precondition (and
            (at ?p ?from)
            (path-blocked ?from ?to ?log_obs)
            (mission-active ?p)
        )
        :effect (and
            (not (path-blocked ?from ?to ?log_obs))
            (path-cleared ?from ?to)
        )
    )

    ;; Action: Move between locations.
    ;; This action allows movement if the path is physically clear and
    ;; if the protagonist can handle the ground conditions (i.e., not slippery, or has adapted).
    (:action go
        :parameters (?p - protagonist ?from ?to - location)
        :precondition (and
            (at ?p ?from)
            (mission-active ?p)
            (path-cleared ?from ?to) ; Requires the path to be cleared if it was blocked by a log.
            (or
                (not (ground-slippery ?to)) ; If the destination location is not slippery, OR
                (can-traverse-slippery-ground ?p) ; If protagonist has adapted to slippery ground.
            )
        )
        :effect (and
            (not (at ?p ?from))
            (at ?p ?to)
        )
    )

    ;; Action: Retrieve the sword from the tree where the crow dropped it.
    ;; This action implies the protagonist climbs the tree and takes the sword.
    (:action retrieve-sword-from-tree
        :parameters (?p - protagonist ?s - sword ?t - tree ?forest - location)
        :precondition (and
            (at ?p ?forest)
            (sword-on-tree ?s ?t)
            (mission-active ?p)
        )
        :effect (and
            (not (sword-on-tree ?s ?t))
            (has ?p ?s)
        )
    )

    ;; Action: Adapt to slippery ground conditions.
    ;; This action represents the protagonist finding a way (e.g., changing boots, learning a technique)
    ;; to effectively move on slippery terrain. Once done, they can traverse any slippery ground.
    (:action adapt-to-slippery-ground
        :parameters (?p - protagonist ?loc - location)
        :precondition (and
            (at ?p ?loc)
            (ground-slippery ?loc)
            (mission-active ?p)
        )
        :effect (and
            (can-traverse-slippery-ground ?p)
        )
    )

    ;; Action: Return the sword to the king at the castle.
    ;; This action completes the quest and achieves the final goal.
    (:action return-sword-to-king
        :parameters (?p - protagonist ?s - sword ?k - king ?castle - location)
        :precondition (and
            (at ?p ?castle)
            (at ?k ?castle)
            (has ?p ?s)
            (mission-active ?p)
        )
        :effect (and
            (not (has ?p ?s))
            (king-has-sword ?k ?s)
        )
    )
)