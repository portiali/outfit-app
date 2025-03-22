

CREATE DATABASE IF NOT EXISTS outfitapp;

USE outfitapp;

-- DROP TABLE IF EXISTS clothing;
-- DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS clothingData;

-- CREATE TABLE users
-- (
--     userid       int not null AUTO_INCREMENT,
--     username     varchar(64) not null,
--     PRIMARY KEY  (userid),
--     UNIQUE(username)
-- );

-- ALTER TABLE users AUTO_INCREMENT = 80001;  -- starting value


-- CREATE TABLE clothing
-- (
--     clothingid        int not null AUTO_INCREMENT,
--     url               varchar(256) not null, 
--     userid            int not null,
--     PRIMARY KEY (clothingid),
--     FOREIGN KEY (userid) REFERENCES users(userid)
-- );
-- ALTER TABLE clothing AUTO_INCREMENT = 1001;  -- starting value


CREATE TABLE clothingData
(
    dataid            int not null AUTO_INCREMENT,
    clothingid        int not null,
    -- gender            varchar(256) not null,  -- female, male for now
    category          varchar(256) not null,  -- casual, formal etc. 
    articleType       varchar(256) not null,  -- shirt, pants, long sleeve etc. 
    color             varchar(256) not null,  -- 
    season            varchar(256) not null,  -- 
    -- usage             varchar(256) not null,  -- 
    PRIMARY KEY (dataid),
    FOREIGN KEY (clothingid) REFERENCES clothing(clothingid)
);
ALTER TABLE clothingData AUTO_INCREMENT = 2001;

DROP USER IF EXISTS 'outfitapp-read-only';
DROP USER IF EXISTS 'outfitapp-read-write';


CREATE USER 'outfitapp-read-only' IDENTIFIED BY 'abc123!!';
CREATE USER 'outfitapp-read-write' IDENTIFIED BY 'def456!!';


GRANT SELECT, SHOW VIEW ON outfitapp.* 
      TO 'outfitapp-read-only';
GRANT SELECT, SHOW VIEW, INSERT, UPDATE, DELETE, DROP, CREATE, ALTER ON outfitapp.* 
      TO 'outfitapp-read-write';
      
FLUSH PRIVILEGES;

--
-- done
--