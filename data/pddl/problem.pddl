(define (problem elia-magic-fountain-quest)
    (:domain elia-quest-for-magic-fountain)
    (:objects
        elia - person
        village - location
        forest - location
        magic-fountain-location - location
        lantern - item
    )

    (:init
        ;; Initial state: Elia is in her village.
        (at elia village)
        ;; Elia possesses her lantern, as per the lore ("armata solo della sua lanterna").
        (has elia lantern)

        ;; Initial problem states reflecting the quest description:
        ;; The village and land are suffering from drought.
        (drought-present)
        ;; The Magic Fountain in the forest is dried up.
        (fountain-dried magic-fountain-location)
        ;; The forest itself presents an oppressive silence.
        (forest-silence-oppressive forest)

        ;; Elia has not yet officially embarked on the quest at the very start of planning.
        ;; The 'embark-quest' action will set (quest-active elia).
    )

    (:goal (and
        ;; Primary goal: The Magic Fountain is awakened.
        (fountain-awakened magic-fountain-location)
        ;; Secondary goal: The drought has ended, as a consequence of the fountain's awakening.
        (not (drought-present))
    ))
)