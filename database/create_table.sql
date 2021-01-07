DROP TABLE IF EXISTS public."chinese_word";

CREATE TABLE public."chinese_word" (
    word_id SERIAL NOT NULL,
    word VARCHAR(4) NOT NULL,
    PRIMARY KEY (word_id)
);