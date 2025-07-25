(define (problem elia-quest-for-hope)
    (:domain elia-magic-source-quest)
    (:objects
        elia - person
        village - location
        forest - location
        magic-source - magic-source
        lantern - item
    )

    (:init
        ;; Initial state: Elia is in her village, afflicted by drought.
        ;; She has her lantern and storytelling gift, ready to venture into the forest.
        (at elia village)
        (has-item elia lantern)
        (can-storytell elia)

        ;; Obstacles and initial conditions:
        (source-is-dry magic-source)        ; The Magic Source is initially dry due to drought.
        (village-afflicted)                 ; The village is suffering from drought and despair.
        (forest-intimidating)               ; The forest is dark, silent, and intimidating, making finding the source difficult.
        
        ;; Predicate for Magic Source being distinct from the general forest area.
        ;; It's a specific location within the forest that needs to be 'found'.
        (at magic-source forest) ; The magic-source is conceptually within the forest.
    )

    (:goal (and
        (at elia magic-source)      ; Elia must reach the Magic Source.
        (source-is-active magic-source) ; The Magic Source must be awakened.
        (village-restored)          ; Hope must be restored to the village.
    ))
)