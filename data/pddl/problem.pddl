(define (problem elia-quest)
    (:domain elia-quest-for-magic-fountain)
    (:objects
        elia - protagonist
        village - village
        forest-edge - forest_edge
        forest-depths - forest_depths
        magic-fountain - magic_source
        story-of-hope - story
    )

    (:init
        ;; Initial state as per quest description: "Elia si trova nel suo villaggio..."
        (at elia village)
        ;; "...afflitto dalla siccità..."
        (village-afflicted-by-drought village)
        ;; "...e decide di intraprendere il viaggio per trovare e riattivare la Fonte Magica."
        ;; The fountain is initially inactive.
        (fountain-inactive magic-fountain)
        ;; Elia has the necessary story to awaken the fountain.
        (has-story-of-hope elia story-of-hope)
        ;; The quest is not yet active; Elia must decide to start it.
        (not (quest-active elia))
        ;; The fountain has not yet been found.
        (not (magic-fountain-found magic-fountain))
        ;; Rain has not returned to the village.
        (not (rain-returned village))
    )

    ;; Goal consistent with the quest: "Trovare la Fonte Magica nel cuore della foresta,
    ;; risvegliarla con una storia di speranza e far tornare la pioggia al villaggio."
    (:goal (and
        (magic-fountain-found magic-fountain) ; Elia finds the Magic Fountain.
        (fountain-active magic-fountain)      ; The Magic Fountain is awakened/reactivated.
        (rain-returned village)               ; Rain has returned to the village.
    ))
)