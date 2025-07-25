(define (domain elia-magic-source-quest)
    (:requirements :strips :typing)
    (:types
        person ; Represents characters in the story, specifically Elia.
        location ; Represents places in the world (village, forest, magic source).
        item ; Represents objects Elia can possess, like the lantern.
        magic-source ; A specific type of location that is the quest's objective.
    )

    (:predicates
        (at ?p - person ?l - location) ; Indicates that a person is at a specific location.
        (has-item ?p - person ?i - item) ; Indicates a person possesses a specific item.
        (can-storytell ?p - person) ; Indicates Elia's unique innate gift of storytelling.

        (source-is-dry ?s - magic-source) ; Represents the initial state of the Magic Source (drought).
        (source-is-active ?s - magic-source) ; Represents the goal state of the Magic Source (water flowing, rain returns).

        (village-afflicted) ; Represents the initial despair and drought affecting the village.
        (village-restored) ; Represents the goal state where hope and rain return to the village.

        (forest-intimidating) ; Represents the combined obstacle of "silence, darkness, and nobody dares to seek."
                              ; This predicate means the direct path or finding the source within the forest is difficult.
        (source-found ?s - magic-source) ; Indicates that Elia has successfully navigated the forest
                                         ; and located the specific spot of the Magic Source.
    )

    ;; Action: Move between general locations.
    ;; This action allows Elia to travel from her current location to an adjacent one.
    ;; It implicitly handles general path traversal but not specific obstacles like "forest-intimidating".
    (:action go
        :parameters (?p - person ?from ?to - location)
        :precondition (and
            (at ?p ?from)
            ;; No specific path-cleared predicates needed for general movement,
            ;; as specific obstacles are handled by other actions for finding the source.
        )
        :effect (and
            (not (at ?p ?from))
            (at ?p ?to)
        )
    )

    ;; Action: Find the Magic Source within the intimidating forest.
    ;; This action represents Elia overcoming the "silence and darkness" (with her lantern)
    ;; and the "nobody dares to seek" aspect (with her unique bravery and perhaps storytelling gift,
    ;; though storytelling is only a direct precondition for awakening).
    (:action find-magic-source
        :parameters (?p - person ?forest-loc - location ?s - magic-source ?l - item)
        :precondition (and
            (at ?p ?forest-loc) ; Elia must be in the forest.
            (has-item ?p ?l)    ; Elia needs the lantern to navigate the darkness.
            (forest-intimidating) ; The forest is initially an intimidating obstacle.
        )
        :effect (and
            (source-found ?s)       ; Elia successfully locates the Magic Source.
            (not (forest-intimidating)) ; The immediate intimidation/mystery of the forest is overcome for Elia.
        )
    )

    ;; Action: Awaken the Magic Source with a story.
    ;; This is the climax action where Elia uses her unique gift to revive the source,
    ;; bringing rain and hope back to the village.
    (:action awaken-source
        :parameters (?p - person ?s - magic-source)
        :precondition (and
            (at ?p ?s)             ; Elia must be at the Magic Source.
            (source-is-dry ?s)     ; The source must be in its dry state.
            (can-storytell ?p)     ; Elia must use her storytelling gift.
        )
        :effect (and
            (source-is-active ?s)  ; The Magic Source is now active and flowing.
            (not (source-is-dry ?s)) ; It is no longer dry.
            (village-restored)     ; The village regains hope and rain.
        )
    )
)