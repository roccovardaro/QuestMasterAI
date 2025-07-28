(define (problem elias-quest-for-magic-spring)
    (:domain elias-quest)
    (:objects
        elia - person ; The protagonist of the quest.
        village - location ; The starting location and the place suffering from drought.
        forest - location ; The location where the Magic Spring is found.
        magic-spring - spring ; The magical entity Elia needs to awaken.
    )

    (:init
        ;; Initial state as per quest description: "Elia si trova nel suo villaggio, afflitto da una grave siccità."
        (at elia village)
        (drought-active village) ; The village is suffering from drought (Obstacle 1).

        ;; Setup for the forest and the spring.
        (in-forest forest) ; Designates 'forest' as a forest area.
        (spring-dormant magic-spring) ; The Magic Spring is initially inert and lifeless (Obstacle 4).

        ;; Elia's inherent ability.
        (has-storytelling-skill elia) ; Elia possesses her unique skill, crucial for the quest.
    )

    ;; Goal consistent with the quest: "Risvegliare la Fonte Magica nel cuore della foresta per far tornare la pioggia e salvare il villaggio dalla siccità, dimostrando il potere delle storie."
    (:goal (and
        (spring-awakened magic-spring) ; The Magic Spring must be awakened.
        (village-saved village) ; The village must be saved from the drought.
    ))
)