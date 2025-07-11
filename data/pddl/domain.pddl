(define (domain elia-quest-for-magic-fountain)
    (:requirements :strips :typing)
    (:types
        person
        location
        magic_source
        story
        protagonist - person
        village forest_edge forest_depths - location
    )

    (:predicates
        (at ?p - person ?l - location) ; Indicates a person's current location.
        (quest-active ?p - protagonist) ; True when Elia has decided to start her quest.
        (magic-fountain-found ?f - magic_source) ; True when the Magic Fountain has been located.
        (fountain-inactive ?f - magic_source) ; True when the Magic Fountain is dry and not active.
        (fountain-active ?f - magic_source) ; True when the Magic Fountain has been awakened and is flowing.
        (village-afflicted-by-drought ?l - village) ; True if the village is suffering from drought.
        (rain-returned ?l - village) ; True if rain has returned to the village.
        (has-story-of-hope ?p - protagonist ?s - story) ; True if Elia knows a story of hope.
        ;; Obstacles:
        ;; "La siccità" is represented by `village-afflicted-by-drought`.
        ;; "Il timore e la reticenza degli altri" is implicitly overcome by Elia's decision to act.
        ;; "Il silenzio e l'oscurità della foresta" is implicitly handled by the 'explore-forest-depths' action's success.
        ;; "La Fonte Magica è inattiva" is represented by `fountain-inactive`.
    )

    ;; Action: Elia decides to embark on her quest.
    ;; This action marks the beginning of her active pursuit of the Magic Fountain,
    ;; overcoming any initial hesitation or the "timore" of others.
    (:action decide-to-start-quest
        :parameters (?p - protagonist ?v - village)
        :precondition (and
            (at ?p ?v)
            (not (quest-active ?p)) ; Ensure quest isn't already active
        )
        :effect (and
            (quest-active ?p)
        )
    )

    ;; Action: Elia travels from the village to the edge of the forest.
    ;; This represents the initial journey away from the familiar.
    (:action go-to-forest-edge
        :parameters (?p - protagonist ?from - village ?to - forest_edge)
        :precondition (and
            (at ?p ?from)
            (quest-active ?p)
        )
        :effect (and
            (not (at ?p ?from))
            (at ?p ?to)
        )
    )

    ;; Action: Elia explores the deeper parts of the forest to find the Magic Fountain.
    ;; This action implicitly involves navigating through the "silence and darkness"
    ;; of the forest, leading her directly to the location of the dormant fountain.
    (:action explore-forest-depths
        :parameters (?p - protagonist ?from - forest_edge ?to - forest_depths ?f - magic_source)
        :precondition (and
            (at ?p ?from)
            (quest-active ?p)
            (not (magic-fountain-found ?f)) ; Only explore if not yet found
        )
        :effect (and
            (not (at ?p ?from))
            (at ?p ?to)
            (magic-fountain-found ?f)
        )
    )

    ;; Action: Elia tells a story of hope to awaken the Magic Fountain.
    ;; This is the core magical act that revitalizes the source, fulfilling the
    ;; quest's emphasis on the "power of stories".
    (:action tell-story-and-awaken-fountain
        :parameters (?p - protagonist ?f - magic_source ?s - story ?loc - forest_depths)
        :precondition (and
            (at ?p ?loc)
            (magic-fountain-found ?f)
            (fountain-inactive ?f)
            (has-story-of-hope ?p ?s)
        )
        :effect (and
            (not (fountain-inactive ?f))
            (fountain-active ?f)
        )
    )

    ;; Action: The magic fountain's awakening causes rain to return to the village.
    ;; This represents the ultimate success of the quest, resolving the drought
    ;; and bringing hope back to the village. It's a magical consequence, not
    ;; requiring Elia to be physically present in the village.
    (:action magically-restore-rain-to-village
        :parameters (?v - village ?f - magic_source)
        :precondition (and
            (fountain-active ?f)
            (village-afflicted-by-drought ?v)
        )
        :effect (and
            (not (village-afflicted-by-drought ?v))
            (rain-returned ?v)
        )
    )
)