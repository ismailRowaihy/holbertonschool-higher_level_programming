-- script that CREATEs table with defaul vale for id
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
)