(define (problem ulfrics-doomed-chase)
    (:domain whimsical-forest-chase)
    (:objects
        ulfric - wolf
        lillo - lamb

        clearing thicket riverbank cave - location ; Locations in the whimsical forest.

        mud-puddle thorny-bush tangled-vines - hazard ; Specific environmental hazards.
        
        culinary-advice fitness-advice ; Types of Lillo's critiques.
    )

    (:init
        ;; Initial state as per quest description:
        ;; "Ulfric, a wolf... spots Lillo... engrossed in gourmet grass-tasting, completely unaware..."
        (at ulfric clearing)
        (at lillo clearing)
        (not (is-aware lillo)) ; Lillo is initially unaware of Ulfric's intent.
        (not (is-chasing ulfric lillo)) ; The chase has not yet begun.
        (not (is-evading lillo))
        (not (is-caught lillo))

        ;; Ulfric's initial state: ready but prone to failure.
        (not (is-distracted ulfric))
        (not (is-clumsy ulfric))
        (not (is-immobilized ulfric))
        (is-focused ulfric) ; Ulfric is focused at the very start, before initiating the chase.

        ;; Setup of environmental hazards in the forest:
        (location-has-hazard thicket thorny-bush)
        (hazard-present thorny-bush) ; Indicates the thorny bush exists.

        (location-has-hazard riverbank mud-puddle)
        (hazard-present mud-puddle) ; Indicates the mud puddle exists.

        (location-has-hazard cave tangled-vines)
        (hazard-present tangled-vines) ; Indicates the tangled vines exist.
    )

    ;; Goal: "Ulfric's primary goal is to successfully capture and consume Lillo."
    (:goal (and
        (is-caught lillo)
        (is-satisfied ulfric)
    ))
)