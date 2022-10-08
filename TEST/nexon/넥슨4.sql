WITH WIN_VOTE AS(
    SELECT re.constituency_id as const, MAX(re.votes) AS result FROM Results AS re
    LEFT JOIN Candidates AS ca
    ON re.candidate_id = ca.id
    GROUP BY constituency_id )

SELECT ca.party, COUNT(ca.party) AS count FROM WIN_VOTE AS win LEFT JOIN Results AS re ON win.result = re.votes LEFT JOIN Candidates AS ca ON re.candidate_id = ca.id GROUP BY ca.party ORDER BY count DESC