DROP TABLE IF EXISTS public."chinese_words";

CREATE TABLE public."chinese_words" (
    word_id SERIAL NOT NULL,
    word VARCHAR(4) NOT NULL,
    PRIMARY KEY (word_id)
);