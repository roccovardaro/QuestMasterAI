(define (domain elia-quest-for-magic-fountain)
    (:requirements :strips :typing)
    (:types
        person ; Represents characters in the story, like Elia.
        location ; Represents distinct places in the world.
        item ; Represents objects or tools Elia might carry.
    )

    (:predicates
        (at ?p - person ?l - location) ; Indicates a person's current location.
        (has ?p - person ?i - item) ; Indicates a person possesses an item.
        (quest-active ?p - person) ; True when the protagonist has embarked on the quest.

        ;; Obstacle/Initial State Predicates
        (drought-present) ; Indicates the village and land are suffering from drought.
        (fountain-dried ?l - location) ; Indicates the Magic Fountain is dried up.
        (forest-silence-oppressive ?l - location) ; Indicates the deep forest's silence is an oppressive obstacle.

        ;; Overcoming Obstacle/Goal-related Predicates
        (silence-broken ?l - location) ; Indicates the oppressive forest silence has been overcome.
        (fountain-awakened ?l - location) ; Indicates the Magic Fountain has been revived.
        ;; (not (drought-present)) is the ultimate goal, handled by the fountain awakening effect.
    )

    ;; Action: Elia decides to embark on the quest.
    ;; This action marks the formal beginning of the adventure, driven by the drought.
    (:action embark-quest
        :parameters (?p - person ?v - location)
        :precondition (and
            (at ?p ?v)
            (drought-present) ; The presence of drought motivates the quest.
        )
        :effect (and
            (quest-active ?p)
        )
    )

    ;; Action: Move between different locations.
    ;; Represents Elia travelling from one place to another.
    (:action go
        :parameters (?p - person ?from ?to - location)
        :precondition (and
            (at ?p ?from)
            (quest-active ?p) ; Elia must be on her quest to travel to new areas.
        )
        :effect (and
            (not (at ?p ?from))
            (at ?p ?to)
        )
    )

    ;; Action: Elia uses her voice (telling stories) to break the oppressive silence of the forest.
    ;; This action specifically addresses the "silenzio opprimente" obstacle.
    ;; The lantern is also needed, symbolizing her tools for the task.
    (:action tell-story-to-forest
        :parameters (?p - person ?f - location ?l - item)
        :precondition (and
            (at ?p ?f)
            (quest-active ?p)
            (has ?p ?l) ; Requires the lantern, symbolizing her means to focus or illuminate her stories.
            (forest-silence-oppressive ?f) ; This obstacle must be present to be overcome.
        )
        :effect (and
            (not (forest-silence-oppressive ?f)) ; The silence is no longer an oppressive force.
            (silence-broken ?f) ; Indicates the challenge has been overcome.
        )
    )

    ;; Action: Elia awakens the Magic Fountain, leading to the end of the drought.
    ;; This is the core action to achieve the quest's primary goal.
    ;; It requires the fountain to be dried and the forest's oppressive silence to have been broken,
    ;; implying the environment is now receptive.
    (:action awaken-magic-fountain
        :parameters (?p - person ?mf - location ?f - location) ; mf=magic fountain location, f=forest location where silence was broken
        :precondition (and
            (at ?p ?mf)
            (quest-active ?p)
            (fountain-dried ?mf) ; The fountain must be dried to be awakened.
            (silence-broken ?f) ; The forest's silence must be broken for the fountain to respond.
        )
        :effect (and
            (not (fountain-dried ?mf)) ; The fountain is no longer dried.
            (fountain-awakened ?mf) ; The fountain is now awake and flowing.
            (not (drought-present)) ; Resolves the main problem: the drought ends.
        )
    )
)