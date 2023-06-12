SELECT * FROM dojos_and_ninjas.ninjas;

dojosSELECT *
FROM dojos
LEFT JOIN ninjas
ON ninjas.dojos_id = dojos.id
WHERE dojos.id = 2
;