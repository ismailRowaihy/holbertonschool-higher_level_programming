-- script that list all shows and genres linked to it
SELECT ts.title AS title,
       tg.name AS name
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY title ASC,name;