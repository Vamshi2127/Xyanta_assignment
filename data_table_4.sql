SELECT
  CASE
    WHEN occupation = "Doctor" THEN Name || "(D)"
    WHEN occupation = "Actor" THEN Name || "(A)"
    WHEN occupation = "Professor" THEN Name || "(P)"
    WHEN occupation = "Singer" THEN Name || "(S)"
  END
FROM
  OCCUPATIONS
ORDER BY
  name;

SELECT
  "There are total of " || COUNT(*) || " " || LOWER(occupation) || "s."
FROM
  OCCUPATIONS
GROUP BY
  occupation
ORDER BY
  COUNT(occupation)